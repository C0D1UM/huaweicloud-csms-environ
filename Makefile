default: yapf lint test

lint:
	poetry run pylint csms tests

test:
	cd tests && poetry run python -m unittest

coverage:
	poetry run coverage erase
	poetry run coverage run --source='csms' -m unittest discover -s tests
	poetry run coverage report -m

yapf:
	poetry run yapf -ipr csms tests
