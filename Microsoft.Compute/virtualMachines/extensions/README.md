
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
|[autoUpgradeMinorVersion](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/autoUpgradeMinorVersion)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/autoUpgradeMinorVersion|TRIAL|
|[enableAutomaticUpgrade](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/enableAutomaticUpgrade)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/enableAutomaticUpgrade|TRIAL|
|[forceUpdateTag](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/forceUpdateTag)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/forceUpdateTag|TRIAL|
|[protectedSettings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/protectedSettings)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/protectedSettings|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/provisioningState)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/provisioningState|TRIAL|
|[publisher](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/publisher)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/publisher|TRIAL|
|[resources](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources|TRIAL|
|[resources[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*])|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*]|TRIAL|
|[resources[*].autoUpgradeMinorVersion](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].autoUpgradeMinorVersion)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].autoUpgradeMinorVersion|TRIAL|
|[resources[*].forceUpdateTag](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].forceUpdateTag)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].forceUpdateTag|TRIAL|
|[resources[*].id](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].id)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].id|TRIAL|
|[resources[*].location](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].location)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].location|TRIAL|
|[resources[*].name](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].name)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].name|TRIAL|
|[resources[*].protectedSettings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].protectedSettings)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].protectedSettings|TRIAL|
|[resources[*].provisioningState](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].provisioningState)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].provisioningState|TRIAL|
|[resources[*].publisher](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].publisher)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].publisher|TRIAL|
|[resources[*].settings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].settings)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].settings|TRIAL|
|[resources[*].tags](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].tags)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].tags|TRIAL|
|[resources[*].type](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].type)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].type|TRIAL|
|[resources[*].typeHandlerVersion](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/resources[*].typeHandlerVersion)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/resources[*].typeHandlerVersion|TRIAL|
|[settings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/settings)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/settings|TRIAL|
|[settings.workspaceId](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/settings.workspaceId)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/settings.workspaceId|TRIAL|
|[type](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/type)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/type|TRIAL|
|[typeHandlerVersion](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/virtualMachines/extensions/typeHandlerVersion)|UNKNOWN|Microsoft.Compute/virtualMachines/extensions/typeHandlerVersion|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***