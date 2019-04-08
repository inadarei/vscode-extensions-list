.PHONY: build-dist
build-dist:
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish:
	twine upload dist/*