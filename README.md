# ansible callback grafana_annotations

Automatically publish annotations in grafana when you execute your playbooks !

# Quickstart

* Copy the callback_plugins directory in you playbook directory
* Export the required environement variables:

```
$ export GRAFANA_SERVER=<your_grafana_server_address>
$ export GRAFANA_PORT=<your_grafana_server_port>
$ export GRAFANA_SECURE=0                           # 0 for HTTP, 1 for HTTPS
$ export GRAFANA_API_TOKEN=<your_grafana_api_token>
```

* Run you playbook:
```
$ ansible-playbook test.yml
```
* See the deployment in grafana:
![Grafana annotations](/screenshot/result.png)
