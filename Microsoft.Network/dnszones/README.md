
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
|[A](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/A)|UNKNOWN|Microsoft.Network/dnszones/A|TRIAL|
|[AAAA](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/AAAA)|UNKNOWN|Microsoft.Network/dnszones/AAAA|TRIAL|
|[CAA](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/CAA)|UNKNOWN|Microsoft.Network/dnszones/CAA|TRIAL|
|[CNAME](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/CNAME)|UNKNOWN|Microsoft.Network/dnszones/CNAME|TRIAL|
|[MX](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/MX)|UNKNOWN|Microsoft.Network/dnszones/MX|TRIAL|
|[NS](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/NS)|UNKNOWN|Microsoft.Network/dnszones/NS|TRIAL|
|[PTR](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/PTR)|UNKNOWN|Microsoft.Network/dnszones/PTR|TRIAL|
|[SOA](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/SOA)|UNKNOWN|Microsoft.Network/dnszones/SOA|TRIAL|
|[SRV](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/SRV)|UNKNOWN|Microsoft.Network/dnszones/SRV|TRIAL|
|[TXT](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/TXT)|UNKNOWN|Microsoft.Network/dnszones/TXT|TRIAL|
|[all](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/all)|UNKNOWN|Microsoft.Network/dnszones/all|TRIAL|
|[maxNumberOfRecordSets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/maxNumberOfRecordSets)|UNKNOWN|Microsoft.Network/dnszones/maxNumberOfRecordSets|TRIAL|
|[nameServers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/nameServers)|UNKNOWN|Microsoft.Network/dnszones/nameServers|TRIAL|
|[nameServers[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/nameServers[*])|UNKNOWN|Microsoft.Network/dnszones/nameServers[*]|TRIAL|
|[numberOfRecordSets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/numberOfRecordSets)|UNKNOWN|Microsoft.Network/dnszones/numberOfRecordSets|TRIAL|
|[recordsets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/recordsets)|UNKNOWN|Microsoft.Network/dnszones/recordsets|TRIAL|
|[registrationVirtualNetworks](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/registrationVirtualNetworks)|UNKNOWN|Microsoft.Network/dnszones/registrationVirtualNetworks|TRIAL|
|[registrationVirtualNetworks[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/registrationVirtualNetworks[*])|UNKNOWN|Microsoft.Network/dnszones/registrationVirtualNetworks[*]|TRIAL|
|[registrationVirtualNetworks[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/registrationVirtualNetworks[*].id)|UNKNOWN|Microsoft.Network/dnszones/registrationVirtualNetworks[*].id|TRIAL|
|[resolutionVirtualNetworks](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/resolutionVirtualNetworks)|UNKNOWN|Microsoft.Network/dnszones/resolutionVirtualNetworks|TRIAL|
|[resolutionVirtualNetworks[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/resolutionVirtualNetworks[*])|UNKNOWN|Microsoft.Network/dnszones/resolutionVirtualNetworks[*]|TRIAL|
|[resolutionVirtualNetworks[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/resolutionVirtualNetworks[*].id)|UNKNOWN|Microsoft.Network/dnszones/resolutionVirtualNetworks[*].id|TRIAL|
|[zoneType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/dnszones/zoneType)|UNKNOWN|Microsoft.Network/dnszones/zoneType|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***