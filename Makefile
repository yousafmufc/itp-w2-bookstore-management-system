.PHONY: test test-cov

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PROJECT_PACKAGE=bookstore


test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test -s test_bookstore.py

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=$(PROJECT_PACKAGE) test_bookstore.py

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=$(PROJECT_PACKAGE) $(shell which py.test) ./test_bookstore.py -q --tb=no >/dev/null; true
	@coverage report
