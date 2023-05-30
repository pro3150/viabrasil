.PHONY: setup
setup:
	@python3.8 -m venv .venv && . .venv/bin/activate

.PHONY: requirements
requirements:
	@pip install -r requirements.txt

.PHONY: run-debug
run-debug:
	@flask --app app/app run --debug