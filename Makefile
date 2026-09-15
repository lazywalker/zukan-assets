# zukan-assets dev tasks. The ETL itself is plain scripts (see
# tools/README.md); this file wraps the editor and sprite loops.

# The repo venv has Pillow (system python3 is PEP 668 externally managed
# and must stay clean); fall back to PATH when there is no venv.
PY ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

.DEFAULT_GOAL := help
.PHONY: help install editor editor-data editor-static sprites pipeline-fetch pipeline-build test check

help: ## list available targets
	@grep -hE '^[a-z-]+:.*## ' $(MAKEFILE_LIST) \
	  | awk -F '## ' '{ sub(/:$$/, "", $$1); printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2 }'

install: ## create .venv and install tools/requirements.txt into it
	test -d .venv || python3 -m venv .venv
	.venv/bin/python -m pip install -r tools/requirements.txt

editor: ## rebuild the data bundle and serve the editor at :8642
	$(PY) pixelart/build_editor_data.py
	$(PY) pixelart/editor_server.py

editor-data: ## rebuild editor/_data/data.json only
	$(PY) pixelart/build_editor_data.py

sprites: ## regenerate every dev preview png (monsters + endemic life)
	$(PY) pixelart/build_sprites.py
	$(PY) pixelart/build_sprites.py --endemic

editor-static: ## self-contained bundle (editor + icons) for static hosting
	$(PY) pixelart/build_editor_data.py --static

pipeline-fetch: ## fetch network sources (apis, fandom icons; needs network)
	$(PY) tools/fetch_external.py
	$(PY) tools/fetch_item_icons.py

pipeline-build: ## offline ETL from cached sources into data/, icons/ and icons-pixelart/
	$(PY) tools/extract_mhgu.py
	$(PY) tools/extract_mh4u.py
	$(PY) tools/clean_mhst2.py
	$(PY) tools/split_sprites.py
	$(PY) tools/build.py
	$(PY) tools/normalize.py
	$(PY) tools/clean_halo.py
	$(PY) tools/clean_background.py
	$(PY) tools/validate.py
	-$(PY) tools/audit.py
	$(PY) pixelart/build_sprites.py --out icons-pixelart
	$(PY) pixelart/build_sprites.py --endemic --out icons-pixelart/endemic

test: ## editor chain self-checks (synthesis, round trip, save refusals)
	$(PY) pixelart/test_editor.py

check: ## byte-verify icons-pixelart against the configs
	$(PY) pixelart/build_sprites.py --check icons-pixelart
	$(PY) pixelart/build_sprites.py --endemic --check icons-pixelart/endemic
