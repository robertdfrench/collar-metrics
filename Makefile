SHELL=/bin/bash
.PHONY: test

test: .venv/.complete
	$(info # Make sure zappa is installed)
	source .venv/bin/activate && pytest --cov-fail-under 100

.venv/.complete: .venv/.updated_pip requirements.txt
	source .venv/bin/activate && pip install -r requirements.txt
	@touch $@

.venv/.updated_pip: .venv/.new
	source .venv/bin/activate && pip install --upgrade pip
	@touch $@

.venv/.new:
	python3.6 -m venv .venv
	@touch $@

uuid:
	@python3 -c "import uuid; print(uuid.uuid4())"
