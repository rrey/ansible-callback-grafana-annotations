# ansible callback grafana_annotations

Automatically publish annotations in grafana when you execute your playbooks !

# Quickstart

* Copy the callback_plugins directory in you playbook directory
* Export the required environement variables:

```
$ export GRAFANA_HOST=<your_grafana_server_address>:<your_grafana_server_port>
$ export GRAFANA_SECURE=0                           # 0 for HTTP, 1 for HTTPS
$ export GRAFANA_API_KEY=<your_grafana_api_token>
```

For token based authentication:

```
$ export GRAFANA_API_KEY=<your_grafana_api_key>
```

For basic http authentication:

```
$ export GRAFANA_USER=<your_grafana_user>
$ export GRAFANA_PASSWORD=<your_grafana_user_password>
```

* Run you playbook:
```
$ ansible-playbook test.yml
```
* See the deployment in grafana:
![Grafana annotations](/screenshot/result.png)

# Restrict the annotations to a specific dashboard

If the annotations should be restricted to a particular dashboard, you can
specify its dashboard id through the dedicated environment variable:

```
$ export GRAFANA_DASHBOARD_ID=<the_grafana_dashboard_id>
```

# Restrict the annotations to a specific panel in a dashboard

If the annotations should be restricted to a particular panel in a dashboard, you can
specify both dashboard id and panel id through the dedicated environment variables:

```
$ export GRAFANA_DASHBOARD_ID=<the_grafana_dashboard_id>
$ export GRAFANA_PANEL_ID=<the_grafana_panel_id>
```
