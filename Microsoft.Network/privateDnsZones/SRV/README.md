
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
|[aRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/aRecords/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/aRecords|TRIAL|
|[aRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/aRecords[*]/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/aRecords[*]|TRIAL|
|[aRecords[*].ipv4Address](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/aRecords[*].ipv4Address/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/aRecords[*].ipv4Address|TRIAL|
|[aaaaRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/aaaaRecords/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/aaaaRecords|TRIAL|
|[aaaaRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/aaaaRecords[*]/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/aaaaRecords[*]|TRIAL|
|[aaaaRecords[*].ipv6Address](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/aaaaRecords[*].ipv6Address/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/aaaaRecords[*].ipv6Address|TRIAL|
|[cnameRecord](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/cnameRecord/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/cnameRecord|TRIAL|
|[cnameRecord.cname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/cnameRecord.cname/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/cnameRecord.cname|TRIAL|
|[fqdn](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/fqdn/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/fqdn|TRIAL|
|[isAutoRegistered](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/isAutoRegistered/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/isAutoRegistered|TRIAL|
|[metadata](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/metadata/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/metadata|TRIAL|
|[mxRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/mxRecords/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/mxRecords|TRIAL|
|[mxRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/mxRecords[*]/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/mxRecords[*]|TRIAL|
|[mxRecords[*].exchange](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/mxRecords[*].exchange/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/mxRecords[*].exchange|TRIAL|
|[mxRecords[*].preference](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/mxRecords[*].preference/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/mxRecords[*].preference|TRIAL|
|[ptrRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/ptrRecords/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/ptrRecords|TRIAL|
|[ptrRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/ptrRecords[*]/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/ptrRecords[*]|TRIAL|
|[ptrRecords[*].ptrdname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/ptrRecords[*].ptrdname/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/ptrRecords[*].ptrdname|TRIAL|
|[soaRecord](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord|TRIAL|
|[soaRecord.email](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.email/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.email|TRIAL|
|[soaRecord.expireTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.expireTime/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.expireTime|TRIAL|
|[soaRecord.host](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.host/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.host|TRIAL|
|[soaRecord.minimumTtl](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.minimumTtl/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.minimumTtl|TRIAL|
|[soaRecord.refreshTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.refreshTime/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.refreshTime|TRIAL|
|[soaRecord.retryTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.retryTime/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.retryTime|TRIAL|
|[soaRecord.serialNumber](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/soaRecord.serialNumber/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/soaRecord.serialNumber|TRIAL|
|[srvRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/srvRecords/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/srvRecords|TRIAL|
|[srvRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/srvRecords[*]/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/srvRecords[*]|TRIAL|
|[srvRecords[*].port](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/srvRecords[*].port/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/srvRecords[*].port|TRIAL|
|[srvRecords[*].priority](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/srvRecords[*].priority/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/srvRecords[*].priority|TRIAL|
|[srvRecords[*].target](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/srvRecords[*].target/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/srvRecords[*].target|TRIAL|
|[srvRecords[*].weight](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/srvRecords[*].weight/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/srvRecords[*].weight|TRIAL|
|[ttl](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/ttl/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/ttl|TRIAL|
|[txtRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/txtRecords/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/txtRecords|TRIAL|
|[txtRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/SRV/txtRecords[*]/README.md)|UNKNOWN|Microsoft.Network/privateDnsZones/SRV/txtRecords[*]|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***