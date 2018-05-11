SHELL=/bin/bash
.PHONY: test

test: .venv/.complete dynamodb_restart
	$(info # Make sure zappa is installed)
	source .venv/bin/activate && \
		DYNAMODB_ENDPOINT="http://localhost:8000" pytest --cov=collar_metrics --cov-fail-under 100 --cov-report term-missing

.venv/.complete: .venv/.updated_pip requirements.txt
	source .venv/bin/activate && pip install -r requirements.txt
	@touch $@

.venv/.updated_pip: .venv/.new
	source .venv/bin/activate && pip install --upgrade pip==9.0.3
	@touch $@

.venv/.new:
	python3.6 -m venv .venv
	@touch $@

dynamodb_restart: dynamodb_stop dynamodb_start;
	
dynamodb_stop:
	killall java || true
	rm -rf shared-local-instance.db

dynamodb_start:	vendor/dynamodb/DynamoDBLocal.jar
	(java -Djava.library.path=./vendor/dynamodb/DynamoDBLocal_lib -jar vendor/dynamodb/DynamoDBLocal.jar -sharedDb &)

vendor/dynamodb/DynamoDBLocal.jar: vendor/dynamodb.tar.gz
	mkdir -p $(dir $@)
	tar xzf $^ -C $(dir $@)

vendor/dynamodb.tar.gz:
	mkdir -p $(dir $@)
	curl https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz -o $@

clean:
	rm -rf vendor/ .venv/
	rm -f collar-metrics-*-template-*.json

deploy: .venv/.complete zappa_settings.json migrate
	source .venv/bin/activate && zappa update production

tail: .venv/.complete zappa_settings.json
	source .venv/bin/activate && zappa tail production

migrate: .venv/.complete zappa_settings.json
	source .venv/bin/activate && python migrate.py

zappa_settings.json: .venv/.complete
	zappa init
	$(error you will now need to run 'make setup' by hand and hammer out your IAM permissions until they are loose enough)

setup: .venv/.complete zappa_settings.json
	source .venv/bin/activate && zappa deploy production
