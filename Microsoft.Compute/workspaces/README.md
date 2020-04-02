
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
|[clusters](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/clusters)|UNKNOWN|Microsoft.Compute/workspaces/clusters|TRIAL|
|[computes](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/computes)|UNKNOWN|Microsoft.Compute/workspaces/computes|TRIAL|
|[dataSources](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/dataSources)|UNKNOWN|Microsoft.Compute/workspaces/dataSources|TRIAL|
|[dbWorkspaces](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/dbWorkspaces)|UNKNOWN|Microsoft.Compute/workspaces/dbWorkspaces|TRIAL|
|[eventGridFilters](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/eventGridFilters)|UNKNOWN|Microsoft.Compute/workspaces/eventGridFilters|TRIAL|
|[experiments](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/experiments)|UNKNOWN|Microsoft.Compute/workspaces/experiments|TRIAL|
|[fileservers](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/fileservers)|UNKNOWN|Microsoft.Compute/workspaces/fileservers|TRIAL|
|[linkedServices](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/linkedServices)|UNKNOWN|Microsoft.Compute/workspaces/linkedServices|TRIAL|
|[query](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/query)|UNKNOWN|Microsoft.Compute/workspaces/query|TRIAL|
|[savedSearches](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/savedSearches)|UNKNOWN|Microsoft.Compute/workspaces/savedSearches|TRIAL|
|[scopedPrivateLinkProxies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/scopedPrivateLinkProxies)|UNKNOWN|Microsoft.Compute/workspaces/scopedPrivateLinkProxies|TRIAL|
|[storageinsightconfigs](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/storageinsightconfigs)|UNKNOWN|Microsoft.Compute/workspaces/storageinsightconfigs|TRIAL|
|[virtualNetworkPeerings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/workspaces/virtualNetworkPeerings)|UNKNOWN|Microsoft.Compute/workspaces/virtualNetworkPeerings|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***