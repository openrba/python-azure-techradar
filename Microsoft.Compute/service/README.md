
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
|[apiVersionSets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/apiVersionSets)|UNKNOWN|Microsoft.Compute/service/apiVersionSets|TRIAL|
|[apis](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/apis)|UNKNOWN|Microsoft.Compute/service/apis|TRIAL|
|[authorizationServers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/authorizationServers)|UNKNOWN|Microsoft.Compute/service/authorizationServers|TRIAL|
|[backends](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/backends)|UNKNOWN|Microsoft.Compute/service/backends|TRIAL|
|[caches](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/caches)|UNKNOWN|Microsoft.Compute/service/caches|TRIAL|
|[diagnostics](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/diagnostics)|UNKNOWN|Microsoft.Compute/service/diagnostics|TRIAL|
|[groups](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/groups)|UNKNOWN|Microsoft.Compute/service/groups|TRIAL|
|[identityProviders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/identityProviders)|UNKNOWN|Microsoft.Compute/service/identityProviders|TRIAL|
|[loggers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/loggers)|UNKNOWN|Microsoft.Compute/service/loggers|TRIAL|
|[notifications](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/notifications)|UNKNOWN|Microsoft.Compute/service/notifications|TRIAL|
|[openidConnectProviders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/openidConnectProviders)|UNKNOWN|Microsoft.Compute/service/openidConnectProviders|TRIAL|
|[policies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/policies)|UNKNOWN|Microsoft.Compute/service/policies|TRIAL|
|[portalsettings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/portalsettings)|UNKNOWN|Microsoft.Compute/service/portalsettings|TRIAL|
|[products](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/products)|UNKNOWN|Microsoft.Compute/service/products|TRIAL|
|[properties](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/properties)|UNKNOWN|Microsoft.Compute/service/properties|TRIAL|
|[subscriptions](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/subscriptions)|UNKNOWN|Microsoft.Compute/service/subscriptions|TRIAL|
|[tags](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/tags)|UNKNOWN|Microsoft.Compute/service/tags|TRIAL|
|[templates](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/templates)|UNKNOWN|Microsoft.Compute/service/templates|TRIAL|
|[users](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/service/users)|UNKNOWN|Microsoft.Compute/service/users|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***