PYTHON = python
PIP = pip

all: test

test: deps
	@$(PYTHON) src/manage.py test --nocapture

deps: django django-nose should_dsl 

django:
	@$(PYTHON) -c 'import django' 2>/dev/null || $(PIP) install django

django-nose:
	@$(PYTHON) -c 'import nose' 2>/dev/null || $(PIP) install django-nose

should_dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/null || $(PIP) install should_dsl