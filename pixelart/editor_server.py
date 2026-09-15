#!/usr/bin/env python3
"""Local dev server for the pixel-art editor.

Serves the editor bundle, maps /icons/* onto the repo's icons/ dir, and is
the only writer of sprites/: POST /api/save applies the payload through
apply_grid (decompile, verify the rebuild, atomic replace, preview
rebuild). Binds 127.0.0.1 only and touches nothing outside pixelart/ and
icons/ reads; no git operations happen here. Run:

    python3 pixelart/editor_server.py

then open http://localhost:8642 . editor/_data/data.json is rebuilt
automatically whenever sprites/*.py is newer than the bundle.
"""

import json
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import apply_grid
from decompile import DecompileError

HERE = Path(__file__).resolve().parent
EDITOR = HERE / "editor"
ICONS = HERE.parent / "icons"
PORT = 8642

TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
         ".js": "text/javascript; charset=utf-8", ".json": "application/json",
         ".png": "image/png"}

rebuild_lock = threading.Lock()


def data_is_stale():
    data = EDITOR / "_data" / "data.json"
    if not data.exists():
        return True
    stamp = data.stat().st_mtime
    for p in (HERE / "sprites").glob("*.py"):
        if p.stat().st_mtime > stamp:
            return True
    return False


def rebuild_data():
    with rebuild_lock:
        if not data_is_stale():
            return
        subprocess.run(
            [sys.executable, str(HERE / "build_editor_data.py")],
            check=True, capture_output=True,
        )


def safe_under(path, root):
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} {fmt % args}")

    def _send(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _file(self, path):
        if not path.exists() or not path.is_file():
            self._send(404, b"not found", "text/plain; charset=utf-8")
            return
        body = path.read_bytes()
        self._send(200, body, TYPES.get(path.suffix, "application/octet-stream"))

    def do_GET(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        if path == "/api/ping":
            self._send(200, b'{"ok": true}', "application/json")
            return
        if path.startswith("/icons/"):
            rel = path[len("/icons/"):]
            target = ICONS / rel
            if ".." in rel.split("/") or not safe_under(target, ICONS):
                self._send(403, b"forbidden", "text/plain; charset=utf-8")
                return
            self._file(target)
            return
        if path.startswith("/_data/"):
            rebuild_data()
            self._file(EDITOR / path.lstrip("/"))
            return
        if path.startswith(("/js/", "/css/")) or path in ("/", "/index.html",
                                                          "/editor.css",
                                                          "/selftest.html"):
            name = "index.html" if path in ("/", "/index.html") else path.lstrip("/")
            self._file(EDITOR / name)
            return
        self._send(404, b"not found", "text/plain; charset=utf-8")

    def do_POST(self):
        if self.path != "/api/save":
            self._send(404, b"not found", "text/plain; charset=utf-8")
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length))
        except (ValueError, json.JSONDecodeError):
            self._send(400, b'{"ok": false, "error": "bad json"}',
                       "application/json")
            return
        try:
            report = apply_grid.apply(payload, rebuild=True)
        except DecompileError as e:
            self._send(400, json.dumps({"ok": False, "error": str(e)}).encode(),
                       "application/json")
            return
        except SystemExit as e:
            self._send(400, json.dumps({"ok": False, "error": str(e)}).encode(),
                       "application/json")
            return
        except RuntimeError as e:
            self._send(500, json.dumps({"ok": False, "error": str(e)}).encode(),
                       "application/json")
            return
        rebuild_data()
        if not report["changed"]:
            hint = ""
        else:
            verb = "update" if report["existed"] else "add"
            hint = f"feat: {verb} {payload['slug']} sprite"
        body = json.dumps({
            "ok": True,
            "file": report["file"],
            "changed": report["changed"],
            "log": report["log"],
            "commit": hint,
        }).encode()
        self._send(200, body, "application/json")


def main():
    rebuild_data()
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"editor at http://localhost:{PORT} (ctrl-c to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
