
RBA TechRadar for Azure
=======================

# Overview

## What is the purpose?


The RBA TechRadar for Azure is a tool to inspire and support engineering teams at Risk & Business Analytics to pick the best technologies for new projects; it provides a platform to share knowledge and experience in technologies, to reflect on technology decisions and continuously evolve our technology landscape.  Based on the pioneering work at Thought Works, our radar sets out the changes in technologies that are interesting in cloud development - changes that we think our engineering teams should pay attention to and consider using in their projects.
## How do we maintain it?


The RBA TechRadar for Azure is maintained by the Cloud Center of Excellence - an open group of senior RBA technologists committed to devote time to this purpose.  The CCoE self organizes to maintain these documents, including this version.  Assignment of technologies to rings is the outcome of status change proposals, which are discussed and voted on in CCoE meetings.  The radar depends on active participation and input from all engineering teams at RBA.
## What are the current ring assignments?


The RBA TechRadar for Azure is a list of technologies, complemented by an assesment result, called ring assignment.  We use five rings with the following semantics:
### Adopt


Technologies we have high confidence in to serve our purpose, also at large scale.  Technologies with a usage culture in the RBA production environment, low risk, automated policy enforcement and are recommended to be widely used.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Trial


Technologies that we have seen work with success in projects to solve real problems;  first serious usage experience that confirm benefits and uncover limitations.  TRIAL technologies are slightly more risky; some engineers in our organization walked this path and will share knowledge and experiences.  This area can contain services that have been architecture and security reviewed but do not contain automated policy managmeent.  

|Resource|Description|Path|Status|
| :---: | :---: | :---: | :---: |
|[GetCredentials](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/GetCredentials/README.md)|UNKNOWN|Microsoft.Network/registries/GetCredentials|TRIAL|
|[buildTasks](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/buildTasks/README.md)|UNKNOWN|Microsoft.Network/registries/buildTasks|TRIAL|
|[builds](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/builds/README.md)|UNKNOWN|Microsoft.Network/registries/builds|TRIAL|
|[eventGridFilters](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/eventGridFilters/README.md)|UNKNOWN|Microsoft.Network/registries/eventGridFilters|TRIAL|
|[generateCredentials](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/generateCredentials/README.md)|UNKNOWN|Microsoft.Network/registries/generateCredentials|TRIAL|
|[getBuildSourceUploadUrl](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/getBuildSourceUploadUrl/README.md)|UNKNOWN|Microsoft.Network/registries/getBuildSourceUploadUrl|TRIAL|
|[importImage](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/importImage/README.md)|UNKNOWN|Microsoft.Network/registries/importImage|TRIAL|
|[listBuildSourceUploadUrl](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/listBuildSourceUploadUrl/README.md)|UNKNOWN|Microsoft.Network/registries/listBuildSourceUploadUrl|TRIAL|
|[listCredentials](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/listCredentials/README.md)|UNKNOWN|Microsoft.Network/registries/listCredentials|TRIAL|
|[listPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/listPolicies/README.md)|UNKNOWN|Microsoft.Network/registries/listPolicies|TRIAL|
|[listUsages](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/listUsages/README.md)|UNKNOWN|Microsoft.Network/registries/listUsages|TRIAL|
|[privateEndpointConnectionProxies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/privateEndpointConnectionProxies/README.md)|UNKNOWN|Microsoft.Network/registries/privateEndpointConnectionProxies|TRIAL|
|[privateEndpointConnections](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/privateEndpointConnections/README.md)|UNKNOWN|Microsoft.Network/registries/privateEndpointConnections|TRIAL|
|[privateLinkResources](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/privateLinkResources/README.md)|UNKNOWN|Microsoft.Network/registries/privateLinkResources|TRIAL|
|[queueBuild](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/queueBuild/README.md)|UNKNOWN|Microsoft.Network/registries/queueBuild|TRIAL|
|[regenerateCredential](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/regenerateCredential/README.md)|UNKNOWN|Microsoft.Network/registries/regenerateCredential|TRIAL|
|[regenerateCredentials](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/regenerateCredentials/README.md)|UNKNOWN|Microsoft.Network/registries/regenerateCredentials|TRIAL|
|[replications](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/replications/README.md)|UNKNOWN|Microsoft.Network/registries/replications|TRIAL|
|[runs](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/runs/README.md)|UNKNOWN|Microsoft.Network/registries/runs|TRIAL|
|[scheduleRun](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/scheduleRun/README.md)|UNKNOWN|Microsoft.Network/registries/scheduleRun|TRIAL|
|[scopeMaps](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/scopeMaps/README.md)|UNKNOWN|Microsoft.Network/registries/scopeMaps|TRIAL|
|[taskRuns](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/taskRuns/README.md)|UNKNOWN|Microsoft.Network/registries/taskRuns|TRIAL|
|[tasks](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/tasks/README.md)|UNKNOWN|Microsoft.Network/registries/tasks|TRIAL|
|[tokens](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/tokens/README.md)|UNKNOWN|Microsoft.Network/registries/tokens|TRIAL|
|[updatePolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/updatePolicies/README.md)|UNKNOWN|Microsoft.Network/registries/updatePolicies|TRIAL|
|[webhooks](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/registries/webhooks/README.md)|UNKNOWN|Microsoft.Network/registries/webhooks|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***