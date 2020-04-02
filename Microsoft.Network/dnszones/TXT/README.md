
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
|[AAAARecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/AAAARecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/AAAARecords|TRIAL|
|[AAAARecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/AAAARecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/AAAARecords[*]|TRIAL|
|[AAAARecords[*].ipv6Address](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/AAAARecords[*].ipv6Address/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/AAAARecords[*].ipv6Address|TRIAL|
|[ARecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/ARecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/ARecords|TRIAL|
|[ARecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/ARecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/ARecords[*]|TRIAL|
|[ARecords[*].ipv4Address](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/ARecords[*].ipv4Address/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/ARecords[*].ipv4Address|TRIAL|
|[CNAMERecord](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/CNAMERecord/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/CNAMERecord|TRIAL|
|[CNAMERecord.cname](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/CNAMERecord.cname/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/CNAMERecord.cname|TRIAL|
|[MXRecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/MXRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/MXRecords|TRIAL|
|[MXRecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/MXRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/MXRecords[*]|TRIAL|
|[MXRecords[*].exchange](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/MXRecords[*].exchange/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/MXRecords[*].exchange|TRIAL|
|[MXRecords[*].preference](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/MXRecords[*].preference/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/MXRecords[*].preference|TRIAL|
|[NSRecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/NSRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/NSRecords|TRIAL|
|[NSRecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/NSRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/NSRecords[*]|TRIAL|
|[NSRecords[*].nsdname](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/NSRecords[*].nsdname/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/NSRecords[*].nsdname|TRIAL|
|[PTRRecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/PTRRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/PTRRecords|TRIAL|
|[PTRRecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/PTRRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/PTRRecords[*]|TRIAL|
|[PTRRecords[*].ptrdname](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/PTRRecords[*].ptrdname/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/PTRRecords[*].ptrdname|TRIAL|
|[SOARecord](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord|TRIAL|
|[SOARecord.email](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.email/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.email|TRIAL|
|[SOARecord.expireTime](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.expireTime/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.expireTime|TRIAL|
|[SOARecord.host](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.host/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.host|TRIAL|
|[SOARecord.minimumTTL](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.minimumTTL/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.minimumTTL|TRIAL|
|[SOARecord.refreshTime](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.refreshTime/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.refreshTime|TRIAL|
|[SOARecord.retryTime](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.retryTime/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.retryTime|TRIAL|
|[SOARecord.serialNumber](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SOARecord.serialNumber/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SOARecord.serialNumber|TRIAL|
|[SRVRecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SRVRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SRVRecords|TRIAL|
|[SRVRecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SRVRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SRVRecords[*]|TRIAL|
|[SRVRecords[*].port](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SRVRecords[*].port/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SRVRecords[*].port|TRIAL|
|[SRVRecords[*].priority](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SRVRecords[*].priority/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SRVRecords[*].priority|TRIAL|
|[SRVRecords[*].target](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SRVRecords[*].target/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SRVRecords[*].target|TRIAL|
|[SRVRecords[*].weight](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/SRVRecords[*].weight/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/SRVRecords[*].weight|TRIAL|
|[TTL](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/TTL/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/TTL|TRIAL|
|[TXTRecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/TXTRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/TXTRecords|TRIAL|
|[TXTRecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/TXTRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/TXTRecords[*]|TRIAL|
|[caaRecords](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/caaRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/caaRecords|TRIAL|
|[caaRecords[*]](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/caaRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/caaRecords[*]|TRIAL|
|[caaRecords[*].flags](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/caaRecords[*].flags/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/caaRecords[*].flags|TRIAL|
|[caaRecords[*].tag](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/caaRecords[*].tag/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/caaRecords[*].tag|TRIAL|
|[caaRecords[*].value](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/caaRecords[*].value/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/caaRecords[*].value|TRIAL|
|[fqdn](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/fqdn/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/fqdn|TRIAL|
|[metadata](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/metadata/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/metadata|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/provisioningState/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/provisioningState|TRIAL|
|[targetResource](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/targetResource/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/targetResource|TRIAL|
|[targetResource.id](https://github.com/openrba/python-azure-techradar/Microsoft.Network/dnszones/TXT/targetResource.id/README.md)|UNKNOWN|Microsoft.Network/dnszones/TXT/targetResource.id|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***