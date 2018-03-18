
syntax:
	pycodestyle --ignore=E265,E501 callback_plugins/grafana_annotations.py

container:
	tools/start_grafana.sh

test-local-token: container
	GRAFANA_API_KEY='$(shell python tools/get_or_create_token.py)' ansible-playbook test.yml

test-local-basic-auth: container
	GRAFANA_USER='admin' GRAFANA_PASSWORD='admin' ansible-playbook test.yml

local-check: test-local-token test-local-basic-auth

# This test will be called multiple times by travis-ci with different env variables.
travis-check:
	ansible-playbook test.yml
