# ansible callback grafana_annotations

Automatically publish annotations in grafana when you execute your playbooks !
This callback was accepted in Ansible and should be available in version 2.6

# Configuration

The configuration can be set through ansible cfg by declaring te callback section.
The following configuration represent the default values:

```
[callback_grafana_annotations]

grafana_url = "http://127.0.0.1:3000/api/annotations"
validate_grafana_certs = 1
http_agent = 'Ansible (grafana_annotations callback)'
grafana_user = ansible
grafana_password = ansible
```

The configuration can be overridden using environment variables.
Check the DOCUMENTATION string to have the full list of parameters.

# Quickstart

* Copy the callback_plugins directory in you playbook directory
* Export the required environement variables:

```
$ export GRAFANA_URL=<your_grafana_url>
```

The URL must be the Grafana annotations api URL, example: http://<some_address>/api/annotations
The protocal can be either http or https.

For token based authentication:

```
$ export GRAFANA_API_KEY=<your_grafana_api_key>
```

For basic http authentication:

```
$ export GRAFANA_USER=<your_grafana_user>
$ export GRAFANA_PASSWORD=<your_grafana_user_password>
```

* Run your playbook:
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
