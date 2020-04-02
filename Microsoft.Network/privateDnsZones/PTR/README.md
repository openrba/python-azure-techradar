
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
|[aRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/aRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/aRecords|TRIAL|
|[aRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/aRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/aRecords[*]|TRIAL|
|[aRecords[*].ipv4Address](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/aRecords[*].ipv4Address)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/aRecords[*].ipv4Address|TRIAL|
|[aaaaRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/aaaaRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/aaaaRecords|TRIAL|
|[aaaaRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/aaaaRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/aaaaRecords[*]|TRIAL|
|[aaaaRecords[*].ipv6Address](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/aaaaRecords[*].ipv6Address)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/aaaaRecords[*].ipv6Address|TRIAL|
|[cnameRecord](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/cnameRecord)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/cnameRecord|TRIAL|
|[cnameRecord.cname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/cnameRecord.cname)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/cnameRecord.cname|TRIAL|
|[fqdn](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/fqdn)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/fqdn|TRIAL|
|[isAutoRegistered](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/isAutoRegistered)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/isAutoRegistered|TRIAL|
|[metadata](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/metadata)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/metadata|TRIAL|
|[mxRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/mxRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/mxRecords|TRIAL|
|[mxRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/mxRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/mxRecords[*]|TRIAL|
|[mxRecords[*].exchange](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/mxRecords[*].exchange)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/mxRecords[*].exchange|TRIAL|
|[mxRecords[*].preference](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/mxRecords[*].preference)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/mxRecords[*].preference|TRIAL|
|[ptrRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/ptrRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/ptrRecords|TRIAL|
|[ptrRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/ptrRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/ptrRecords[*]|TRIAL|
|[ptrRecords[*].ptrdname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/ptrRecords[*].ptrdname)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/ptrRecords[*].ptrdname|TRIAL|
|[soaRecord](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord|TRIAL|
|[soaRecord.email](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.email)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.email|TRIAL|
|[soaRecord.expireTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.expireTime)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.expireTime|TRIAL|
|[soaRecord.host](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.host)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.host|TRIAL|
|[soaRecord.minimumTtl](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.minimumTtl)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.minimumTtl|TRIAL|
|[soaRecord.refreshTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.refreshTime)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.refreshTime|TRIAL|
|[soaRecord.retryTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.retryTime)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.retryTime|TRIAL|
|[soaRecord.serialNumber](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/soaRecord.serialNumber)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/soaRecord.serialNumber|TRIAL|
|[srvRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/srvRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/srvRecords|TRIAL|
|[srvRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/srvRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/srvRecords[*]|TRIAL|
|[srvRecords[*].port](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/srvRecords[*].port)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/srvRecords[*].port|TRIAL|
|[srvRecords[*].priority](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/srvRecords[*].priority)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/srvRecords[*].priority|TRIAL|
|[srvRecords[*].target](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/srvRecords[*].target)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/srvRecords[*].target|TRIAL|
|[srvRecords[*].weight](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/srvRecords[*].weight)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/srvRecords[*].weight|TRIAL|
|[ttl](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/ttl)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/ttl|TRIAL|
|[txtRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/txtRecords)|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/txtRecords|TRIAL|
|[txtRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/privateDnsZones/PTR/txtRecords[*])|UNKNOWN|Microsoft.Network/privateDnsZones/PTR/txtRecords[*]|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***