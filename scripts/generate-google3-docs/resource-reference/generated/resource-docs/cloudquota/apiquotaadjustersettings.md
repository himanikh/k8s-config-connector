{# AUTOGENERATED. DO NOT EDIT. #}

{% extends "config-connector/_base.html" %}

{% block page_title %}APIQuotaAdjusterSettings{% endblock %}
{% block body %}


<table>
<thead>
<tr>
<th><strong>Property</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>{{gcp_name_short}} Service Name</td>
<td>Cloud Quotas</td>
</tr>
<tr>
<td>{{gcp_name_short}} Service Documentation</td>
<td><a href="/quotas/docs/">/quotas/docs/</a></td>
</tr>
<tr>
<td>{{gcp_name_short}} REST Resource Documentation</td>
<td><a href="/quotas/docs/reference/rest/v1beta/projects.locations.quotaAdjusterSettings">/quotas/docs/reference/rest/v1beta/projects.locations.quotaAdjusterSettings</a></td>
</tr>
<tr>
<td>{{product_name_short}} Resource Short Names</td>
<td>APIQuotaAdjusterSettings<br>gcpapiquotaadjustersettings<br>apiquotaadjustersettings</td>
</tr>
<tr>
<td>{{product_name_short}} Service Name</td>
<td>cloudquotas.googleapis.com</td>
</tr>
<tr>
<td>{{product_name_short}} Resource Fully Qualified Name</td>
<td>apiquotaadjustersettings.cloudquota.cnrm.cloud.google.com</td>
</tr>

<tr>
    <td>Can Be Referenced by IAMPolicy/IAMPolicyMember</td>
    <td>No</td>
</tr>


<tr>
<td>{{product_name_short}} Default Average Reconcile Interval In Seconds</td>
<td>600</td>
</tr>
</tbody>
</table>

## Custom Resource Definition Properties



### Spec
#### Schema
```yaml
enablement: string
projectRef:
  external: string
  kind: string
  name: string
  namespace: string
resourceID: string
```

<table class="properties responsive">
<thead>
    <tr>
        <th colspan="2">Fields</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>
            <p><code>enablement</code></p>
            <p><i>Required</i></p>
        </td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Required. The configured value of the enablement at the given resource.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>projectRef</code></p>
            <p><i>Required</i></p>
        </td>
        <td>
            <p><code class="apitype">object</code></p>
            <p>{% verbatim %}The Project that this resource belongs to.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>projectRef.external</code></p>
            <p><i>Optional</i></p>
        </td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}The `projectID` field of a project, when not managed by Config Connector.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>projectRef.kind</code></p>
            <p><i>Optional</i></p>
        </td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}The kind of the Project resource; optional but must be `Project` if provided.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>projectRef.name</code></p>
            <p><i>Optional</i></p>
        </td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}The `name` field of a `Project` resource.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>projectRef.namespace</code></p>
            <p><i>Optional</i></p>
        </td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}The `namespace` field of a `Project` resource.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>resourceID</code></p>
            <p><i>Optional</i></p>
        </td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}The APIQuotaAdjusterSettings name. If not given, the metadata.name will be used.{% endverbatim %}</p>
        </td>
    </tr>
</tbody>
</table>



### Status
#### Schema
```yaml
conditions:
- lastTransitionTime: string
  message: string
  reason: string
  status: string
  type: string
externalRef: string
observedGeneration: integer
observedState:
  etag: string
  updateTime: string
```

<table class="properties responsive">
<thead>
    <tr>
        <th colspan="2">Fields</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>conditions</code></td>
        <td>
            <p><code class="apitype">list (object)</code></p>
            <p>{% verbatim %}Conditions represent the latest available observations of the object's current state.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>conditions[]</code></td>
        <td>
            <p><code class="apitype">object</code></p>
            <p>{% verbatim %}{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>conditions[].lastTransitionTime</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Last time the condition transitioned from one status to another.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>conditions[].message</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Human-readable message indicating details about last transition.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>conditions[].reason</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Unique, one-word, CamelCase reason for the condition's last transition.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>conditions[].status</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Status is the status of the condition. Can be True, False, Unknown.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>conditions[].type</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Type is the type of the condition.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>externalRef</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}A unique specifier for the APIQuotaAdjusterSettings resource in GCP.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>observedGeneration</code></td>
        <td>
            <p><code class="apitype">integer</code></p>
            <p>{% verbatim %}ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>observedState</code></td>
        <td>
            <p><code class="apitype">object</code></p>
            <p>{% verbatim %}ObservedState is the state of the resource as most recently observed in GCP.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>observedState.etag</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Optional. The current etag of the QuotaAdjusterSettings. If an etag is provided on update and does not match the current server's etag of the QuotaAdjusterSettings, the request will be blocked and an ABORTED error will be returned. See https://google.aip.dev/134#etags for more details on etags.{% endverbatim %}</p>
        </td>
    </tr>
    <tr>
        <td><code>observedState.updateTime</code></td>
        <td>
            <p><code class="apitype">string</code></p>
            <p>{% verbatim %}Output only. The timestamp when the QuotaAdjusterSettings was last updated.{% endverbatim %}</p>
        </td>
    </tr>
</tbody>
</table>

## Sample YAML(s)

### Typical Use Case
```yaml
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: cloudquota.cnrm.cloud.google.com/v1beta1
kind: APIQuotaAdjusterSettings
metadata:
  name: apiquotaadjustersettings-sample
spec:
  resourceID: quotaAdjusterSettings
  projectRef:
    external: projects/${PROJECT_ID?}
  enablement: ENABLED
```


Note: If you have any trouble with instantiating the resource, refer to <a href="/config-connector/docs/troubleshooting">Troubleshoot Config Connector</a>.

{% endblock %}
