MODULE_LINT=/usr/share/moduleframework/tools/modulelint.py
CMD=python -m avocado run --sysinfo=off --show-job-log --filter-by-tags=-WIP $(MODULE_LINT) pythonTests.py

test:
	$(CMD)

check: test
all: check
