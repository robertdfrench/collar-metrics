SHELL=/bin/bash

test: .venv/.complete
	$(info # Make sure zappa is installed)
	source .venv/bin/activate && which zappa

.venv/.complete: .venv/.updated_pip requirements.txt
	source .venv/bin/activate && pip install -r requirements.txt
	@touch $@

.venv/.updated_pip: .venv/.new
	source .venv/bin/activate && pip install --upgrade pip
	@touch $@

.venv/.new:
	python3.6 -m venv .venv
	@touch $@
