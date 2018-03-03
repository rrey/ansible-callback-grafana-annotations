
syntax:
	pycodestyle --ignore=E265,E501 callback_plugins/grafana_annotations.py

container:
	tools/start_grafana.sh

check: container
	GRAFANA_API_KEY='$(shell python tools/get_or_create_token.py)' ansible-playbook test.yml
	#TODO: Check annotations are available in grafana
	#TODO: use a test framework like unittest
