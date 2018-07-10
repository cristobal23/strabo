.PHONY: docs test

help:
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  test        run all your tests using py.test"

deps:
	pip install -r requirements.txt

clean:
	python manage.py clean

test: lint pytest

lint:
	flake8 . --exclude=venv

pytest:
	py.test tests
