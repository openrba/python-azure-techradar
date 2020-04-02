
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
|[managed](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/managed/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/managed|TRIAL|
|[platformFaultDomainCount](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/platformFaultDomainCount/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/platformFaultDomainCount|TRIAL|
|[platformUpdateDomainCount](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/platformUpdateDomainCount/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/platformUpdateDomainCount|TRIAL|
|[proximityPlacementGroup](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/proximityPlacementGroup/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/proximityPlacementGroup|TRIAL|
|[proximityPlacementGroup.id](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/proximityPlacementGroup.id/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/proximityPlacementGroup.id|TRIAL|
|[sku](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/sku/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/sku|TRIAL|
|[sku.capacity](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/sku.capacity/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/sku.capacity|TRIAL|
|[sku.name](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/sku.name/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/sku.name|TRIAL|
|[sku.tier](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/sku.tier/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/sku.tier|TRIAL|
|[statuses](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses|TRIAL|
|[statuses[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses[*]/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses[*]|TRIAL|
|[statuses[*].code](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses[*].code/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses[*].code|TRIAL|
|[statuses[*].displayStatus](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses[*].displayStatus/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses[*].displayStatus|TRIAL|
|[statuses[*].level](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses[*].level/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses[*].level|TRIAL|
|[statuses[*].message](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses[*].message/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses[*].message|TRIAL|
|[statuses[*].time](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/statuses[*].time/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/statuses[*].time|TRIAL|
|[virtualMachines](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/virtualMachines/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/virtualMachines|TRIAL|
|[virtualMachines[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/virtualMachines[*]/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/virtualMachines[*]|TRIAL|
|[virtualMachines[*].id](https://github.com/openrba/python-azure-techradar/Microsoft.Compute/availabilitySets/virtualMachines[*].id/README.md)|UNKNOWN|Microsoft.Compute/availabilitySets/virtualMachines[*].id|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***