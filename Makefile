venv:
	python3 -m venv venv

freeze:
	rm -rf requirements-lock.txt; \
	python3 -m pipdeptree --warn silence > requirements-lock.txt; \
	rm -rf requirements.txt; \
	python3 -m pip freeze > requirements.txt

install:
ifeq ($(origin name), undefined)
	python3 -m pip install -r requirements.txt
else
	python3 -m pip install $(name); \
	make freeze
endif

smell:
ifeq ($(origin file), undefined)
	python3 -m pylint ./src/datastructpy
else
	python3 -m pylint ./src/datastructpy/$(file)
endif

test:
ifeq ($(origin file), undefined)
	python3 -m unittest ./tests/test_*.py
else
	python3 -m unittest ./tests/$(file)
endif

format:
ifeq ($(origin file), undefined)
	python3 -m black .
else
	python3 -m black ./$(file)
endif

check-format:
ifeq ($(origin file), undefined)
	python3 -m black . --check --diff --color
else
	python3 -m black ./$(file) --check --diff --color
endif

typecheck:
ifeq ($(origin file), undefined)
	python3 -m mypy --config-file mypy.ini . --explicit-package-bases
else
	python3 -m mypy --config-file mypy.int $(file) --explicit-package-bases
endif

hooks:
	pre-commit install --hook-type pre-commit; \
	pre-commit install --hook-type pre-push

test-hook:
ifeq ($(origin hook), undefined)
	pre-commit run --all-files
else
	pre-commit run $(hook) --all-files
endif
