
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
|[certificates](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/certificates)|UNKNOWN|Microsoft.Network/automationAccounts/certificates|TRIAL|
|[compilationjobs](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/compilationjobs)|UNKNOWN|Microsoft.Network/automationAccounts/compilationjobs|TRIAL|
|[configurations](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/configurations)|UNKNOWN|Microsoft.Network/automationAccounts/configurations|TRIAL|
|[connectionTypes](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/connectionTypes)|UNKNOWN|Microsoft.Network/automationAccounts/connectionTypes|TRIAL|
|[connections](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/connections)|UNKNOWN|Microsoft.Network/automationAccounts/connections|TRIAL|
|[credentials](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/credentials)|UNKNOWN|Microsoft.Network/automationAccounts/credentials|TRIAL|
|[jobSchedules](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/jobSchedules)|UNKNOWN|Microsoft.Network/automationAccounts/jobSchedules|TRIAL|
|[jobs](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/jobs)|UNKNOWN|Microsoft.Network/automationAccounts/jobs|TRIAL|
|[modules](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/modules)|UNKNOWN|Microsoft.Network/automationAccounts/modules|TRIAL|
|[nodeConfigurations](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/nodeConfigurations)|UNKNOWN|Microsoft.Network/automationAccounts/nodeConfigurations|TRIAL|
|[privateEndpointConnectionProxies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/privateEndpointConnectionProxies)|UNKNOWN|Microsoft.Network/automationAccounts/privateEndpointConnectionProxies|TRIAL|
|[privateEndpointConnections](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/privateEndpointConnections)|UNKNOWN|Microsoft.Network/automationAccounts/privateEndpointConnections|TRIAL|
|[privateLinkResources](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/privateLinkResources)|UNKNOWN|Microsoft.Network/automationAccounts/privateLinkResources|TRIAL|
|[python2Packages](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/python2Packages)|UNKNOWN|Microsoft.Network/automationAccounts/python2Packages|TRIAL|
|[runbooks](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/runbooks)|UNKNOWN|Microsoft.Network/automationAccounts/runbooks|TRIAL|
|[schedules](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/schedules)|UNKNOWN|Microsoft.Network/automationAccounts/schedules|TRIAL|
|[softwareUpdateConfigurations](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/softwareUpdateConfigurations)|UNKNOWN|Microsoft.Network/automationAccounts/softwareUpdateConfigurations|TRIAL|
|[variables](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/variables)|UNKNOWN|Microsoft.Network/automationAccounts/variables|TRIAL|
|[watchers](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/watchers)|UNKNOWN|Microsoft.Network/automationAccounts/watchers|TRIAL|
|[webhooks](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/automationAccounts/webhooks)|UNKNOWN|Microsoft.Network/automationAccounts/webhooks|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***