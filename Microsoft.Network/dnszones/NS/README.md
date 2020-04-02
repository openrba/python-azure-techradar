
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
|[AAAARecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/AAAARecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/AAAARecords|TRIAL|
|[AAAARecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/AAAARecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/AAAARecords[*]|TRIAL|
|[AAAARecords[*].ipv6Address](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/AAAARecords[*].ipv6Address/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/AAAARecords[*].ipv6Address|TRIAL|
|[ARecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/ARecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/ARecords|TRIAL|
|[ARecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/ARecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/ARecords[*]|TRIAL|
|[ARecords[*].ipv4Address](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/ARecords[*].ipv4Address/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/ARecords[*].ipv4Address|TRIAL|
|[CNAMERecord](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/CNAMERecord/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/CNAMERecord|TRIAL|
|[CNAMERecord.cname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/CNAMERecord.cname/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/CNAMERecord.cname|TRIAL|
|[MXRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/MXRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/MXRecords|TRIAL|
|[MXRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/MXRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/MXRecords[*]|TRIAL|
|[MXRecords[*].exchange](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/MXRecords[*].exchange/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/MXRecords[*].exchange|TRIAL|
|[MXRecords[*].preference](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/MXRecords[*].preference/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/MXRecords[*].preference|TRIAL|
|[NSRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/NSRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/NSRecords|TRIAL|
|[NSRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/NSRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/NSRecords[*]|TRIAL|
|[NSRecords[*].nsdname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/NSRecords[*].nsdname/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/NSRecords[*].nsdname|TRIAL|
|[PTRRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/PTRRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/PTRRecords|TRIAL|
|[PTRRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/PTRRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/PTRRecords[*]|TRIAL|
|[PTRRecords[*].ptrdname](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/PTRRecords[*].ptrdname/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/PTRRecords[*].ptrdname|TRIAL|
|[SOARecord](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord|TRIAL|
|[SOARecord.email](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.email/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.email|TRIAL|
|[SOARecord.expireTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.expireTime/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.expireTime|TRIAL|
|[SOARecord.host](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.host/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.host|TRIAL|
|[SOARecord.minimumTTL](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.minimumTTL/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.minimumTTL|TRIAL|
|[SOARecord.refreshTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.refreshTime/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.refreshTime|TRIAL|
|[SOARecord.retryTime](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.retryTime/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.retryTime|TRIAL|
|[SOARecord.serialNumber](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SOARecord.serialNumber/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SOARecord.serialNumber|TRIAL|
|[SRVRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SRVRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SRVRecords|TRIAL|
|[SRVRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SRVRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SRVRecords[*]|TRIAL|
|[SRVRecords[*].port](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SRVRecords[*].port/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SRVRecords[*].port|TRIAL|
|[SRVRecords[*].priority](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SRVRecords[*].priority/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SRVRecords[*].priority|TRIAL|
|[SRVRecords[*].target](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SRVRecords[*].target/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SRVRecords[*].target|TRIAL|
|[SRVRecords[*].weight](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/SRVRecords[*].weight/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/SRVRecords[*].weight|TRIAL|
|[TTL](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/TTL/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/TTL|TRIAL|
|[TXTRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/TXTRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/TXTRecords|TRIAL|
|[TXTRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/TXTRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/TXTRecords[*]|TRIAL|
|[caaRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/caaRecords/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/caaRecords|TRIAL|
|[caaRecords[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/caaRecords[*]/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/caaRecords[*]|TRIAL|
|[caaRecords[*].flags](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/caaRecords[*].flags/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/caaRecords[*].flags|TRIAL|
|[caaRecords[*].tag](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/caaRecords[*].tag/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/caaRecords[*].tag|TRIAL|
|[caaRecords[*].value](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/caaRecords[*].value/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/caaRecords[*].value|TRIAL|
|[fqdn](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/fqdn/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/fqdn|TRIAL|
|[metadata](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/metadata/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/metadata|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/provisioningState/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/provisioningState|TRIAL|
|[targetResource](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/targetResource/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/targetResource|TRIAL|
|[targetResource.id](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/dnszones/NS/targetResource.id/README.md)|UNKNOWN|Microsoft.Network/dnszones/NS/targetResource.id|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***