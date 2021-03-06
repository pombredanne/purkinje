doc:
	(cd docs/ && make html)

test-tox:
	tox

test-py: test-tox

test-js-karma:
	./node_modules/karma/bin/karma start --single-run

test-js-karma-continuous:
	./node_modules/karma/bin/karma --browsers=Chrome start

test-js-karma-only-firefox:
	./node_modules/karma/bin/karma start --single-run --browsers=Firefox

test-js-protractor:
	npm test

test-js-esvalidate:
	find purkinje/static/js/ -iname "*.js" |xargs esvalidate

test-js-jshint:
	jshint *.js purkinje/static/js

test-js: test-js-jshint test-js-karma test-js-protractor test-js-esvalidate

test: test-py test-js

doc-clean:
	(cd docs/ && make clean)

dist:
	python setup.py sdist
	python setup.py bdist_wheel

build-docker:
	sudo docker build .

# Build Flask assets
assets:
	python manage.py assets build

install_selenium:
	./node_modules/protractor/bin/webdriver-manager update

update: install_selenium
	pip install -r dev-requirements.txt
	bower install
	npm install
	pip install -e .

upload-pypi:
	python setup.py sdist upload -r pypi

