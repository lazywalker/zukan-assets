# zukan-assets dev tasks. The ETL itself is plain scripts (see
# tools/README.md); this file only wraps the editor loop.

# The repo venv has Pillow (system python3 is PEP 668 externally managed
# and must stay clean); fall back to PATH when there is no venv.
PY ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

.PHONY: editor editor-data editor-static test check

editor: ## rebuild the data bundle and serve the editor at :8642
	$(PY) pixelart/build_editor_data.py
	$(PY) pixelart/editor_server.py

editor-data: ## rebuild editor/_data/data.json only
	$(PY) pixelart/build_editor_data.py

editor-static: ## self-contained bundle (editor + icons) for static hosting
	$(PY) pixelart/build_editor_data.py --static

test: ## editor chain self-checks (synthesis, round trip, save refusals)
	$(PY) pixelart/test_editor.py

check: ## byte-verify icons-pixelart against the configs
	$(PY) pixelart/build_sprites.py --check icons-pixelart
