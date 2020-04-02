
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
|[enabled](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/enabled)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/enabled|TRIAL|
|[flowAnalyticsConfiguration](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration|TRIAL|
|[flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration|TRIAL|
|[flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.enabled](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.enabled)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.enabled|TRIAL|
|[flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.trafficAnalyticsInterval](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.trafficAnalyticsInterval)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.trafficAnalyticsInterval|TRIAL|
|[flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceId](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceId)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceId|TRIAL|
|[flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceRegion](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceRegion)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceRegion|TRIAL|
|[flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceResourceId](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceResourceId)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/flowAnalyticsConfiguration.networkWatcherFlowAnalyticsConfiguration.workspaceResourceId|TRIAL|
|[format](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/format)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/format|TRIAL|
|[format.type](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/format.type)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/format.type|TRIAL|
|[format.version](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/format.version)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/format.version|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/provisioningState)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/provisioningState|TRIAL|
|[retentionPolicy](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/retentionPolicy)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/retentionPolicy|TRIAL|
|[retentionPolicy.days](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/retentionPolicy.days)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/retentionPolicy.days|TRIAL|
|[retentionPolicy.enabled](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/retentionPolicy.enabled)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/retentionPolicy.enabled|TRIAL|
|[storageId](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/storageId)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/storageId|TRIAL|
|[targetResourceGuid](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/targetResourceGuid)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/targetResourceGuid|TRIAL|
|[targetResourceId](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/networkWatchers/flowLogs/targetResourceId)|UNKNOWN|Microsoft.Network/networkWatchers/flowLogs/targetResourceId|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***