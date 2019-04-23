VERSION = 0.1.1

.PHONY: doc test tgz

clean:
	rm -rf htmlcov .coverage *.tgz __pycache__ .pytest_cache
tgz: doc
	git archive --format=tar.gz -o palindrome-$(VERSION).tgz --prefix=palindrome-$(VERSION)/ master
doc:
	README.md -o
test:
	python3 -m pytest -v test.py
