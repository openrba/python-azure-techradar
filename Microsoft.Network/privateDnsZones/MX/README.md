
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
|[aRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/aRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/aRecords|TRIAL|
|[aRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/aRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/MX/aRecords[*]|TRIAL|
|[aRecords[*].ipv4Address](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/aRecords[*].ipv4Address)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/aRecords[*].ipv4Address|TRIAL|
|[aaaaRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/aaaaRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/aaaaRecords|TRIAL|
|[aaaaRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/aaaaRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/MX/aaaaRecords[*]|TRIAL|
|[aaaaRecords[*].ipv6Address](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/aaaaRecords[*].ipv6Address)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/aaaaRecords[*].ipv6Address|TRIAL|
|[cnameRecord](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/cnameRecord)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/cnameRecord|TRIAL|
|[cnameRecord.cname](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/cnameRecord.cname)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/cnameRecord.cname|TRIAL|
|[fqdn](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/fqdn)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/fqdn|TRIAL|
|[isAutoRegistered](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/isAutoRegistered)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/isAutoRegistered|TRIAL|
|[metadata](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/metadata)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/metadata|TRIAL|
|[mxRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/mxRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/mxRecords|TRIAL|
|[mxRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/mxRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/MX/mxRecords[*]|TRIAL|
|[mxRecords[*].exchange](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/mxRecords[*].exchange)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/mxRecords[*].exchange|TRIAL|
|[mxRecords[*].preference](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/mxRecords[*].preference)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/mxRecords[*].preference|TRIAL|
|[ptrRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/ptrRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/ptrRecords|TRIAL|
|[ptrRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/ptrRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/MX/ptrRecords[*]|TRIAL|
|[ptrRecords[*].ptrdname](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/ptrRecords[*].ptrdname)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/ptrRecords[*].ptrdname|TRIAL|
|[soaRecord](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord|TRIAL|
|[soaRecord.email](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.email)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.email|TRIAL|
|[soaRecord.expireTime](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.expireTime)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.expireTime|TRIAL|
|[soaRecord.host](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.host)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.host|TRIAL|
|[soaRecord.minimumTtl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.minimumTtl)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.minimumTtl|TRIAL|
|[soaRecord.refreshTime](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.refreshTime)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.refreshTime|TRIAL|
|[soaRecord.retryTime](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.retryTime)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.retryTime|TRIAL|
|[soaRecord.serialNumber](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/soaRecord.serialNumber)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/soaRecord.serialNumber|TRIAL|
|[srvRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/srvRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/srvRecords|TRIAL|
|[srvRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/srvRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/MX/srvRecords[*]|TRIAL|
|[srvRecords[*].port](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/srvRecords[*].port)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/srvRecords[*].port|TRIAL|
|[srvRecords[*].priority](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/srvRecords[*].priority)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/srvRecords[*].priority|TRIAL|
|[srvRecords[*].target](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/srvRecords[*].target)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/srvRecords[*].target|TRIAL|
|[srvRecords[*].weight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/srvRecords[*].weight)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/srvRecords[*].weight|TRIAL|
|[ttl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/ttl)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/ttl|TRIAL|
|[txtRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/txtRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/MX/txtRecords|TRIAL|
|[txtRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/MX/txtRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/MX/txtRecords[*]|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***