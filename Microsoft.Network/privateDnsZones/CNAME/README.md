
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

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Path</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>[aRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/aRecords)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/aRecords</sub>|<sub>TRIAL</sub>|
|<sub>[aRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/aRecords[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/aRecords[*]</sub>|<sub>TRIAL</sub>|
|<sub>[aRecords[*].ipv4Address](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/aRecords[*].ipv4Address)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/aRecords[*].ipv4Address</sub>|<sub>TRIAL</sub>|
|<sub>[aaaaRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/aaaaRecords)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/aaaaRecords</sub>|<sub>TRIAL</sub>|
|<sub>[aaaaRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/aaaaRecords[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/aaaaRecords[*]</sub>|<sub>TRIAL</sub>|
|<sub>[aaaaRecords[*].ipv6Address](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/aaaaRecords[*].ipv6Address)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/aaaaRecords[*].ipv6Address</sub>|<sub>TRIAL</sub>|
|<sub>[cnameRecord](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/cnameRecord)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/cnameRecord</sub>|<sub>TRIAL</sub>|
|<sub>[cnameRecord.cname](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/cnameRecord.cname)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/cnameRecord.cname</sub>|<sub>TRIAL</sub>|
|<sub>[fqdn](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/fqdn)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/fqdn</sub>|<sub>TRIAL</sub>|
|<sub>[isAutoRegistered](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/isAutoRegistered)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/isAutoRegistered</sub>|<sub>TRIAL</sub>|
|<sub>[metadata](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/metadata)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/metadata</sub>|<sub>TRIAL</sub>|
|<sub>[mxRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/mxRecords)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/mxRecords</sub>|<sub>TRIAL</sub>|
|<sub>[mxRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/mxRecords[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/mxRecords[*]</sub>|<sub>TRIAL</sub>|
|<sub>[mxRecords[*].exchange](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/mxRecords[*].exchange)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/mxRecords[*].exchange</sub>|<sub>TRIAL</sub>|
|<sub>[mxRecords[*].preference](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/mxRecords[*].preference)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/mxRecords[*].preference</sub>|<sub>TRIAL</sub>|
|<sub>[ptrRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/ptrRecords)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/ptrRecords</sub>|<sub>TRIAL</sub>|
|<sub>[ptrRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/ptrRecords[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/ptrRecords[*]</sub>|<sub>TRIAL</sub>|
|<sub>[ptrRecords[*].ptrdname](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/ptrRecords[*].ptrdname)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/ptrRecords[*].ptrdname</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.email](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.email)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.email</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.expireTime](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.expireTime)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.expireTime</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.host](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.host)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.host</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.minimumTtl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.minimumTtl)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.minimumTtl</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.refreshTime](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.refreshTime)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.refreshTime</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.retryTime](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.retryTime)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.retryTime</sub>|<sub>TRIAL</sub>|
|<sub>[soaRecord.serialNumber](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/soaRecord.serialNumber)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/soaRecord.serialNumber</sub>|<sub>TRIAL</sub>|
|<sub>[srvRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/srvRecords)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/srvRecords</sub>|<sub>TRIAL</sub>|
|<sub>[srvRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/srvRecords[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/srvRecords[*]</sub>|<sub>TRIAL</sub>|
|<sub>[srvRecords[*].port](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].port)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].port</sub>|<sub>TRIAL</sub>|
|<sub>[srvRecords[*].priority](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].priority)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].priority</sub>|<sub>TRIAL</sub>|
|<sub>[srvRecords[*].target](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].target)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].target</sub>|<sub>TRIAL</sub>|
|<sub>[srvRecords[*].weight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].weight)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/srvRecords[*].weight</sub>|<sub>TRIAL</sub>|
|<sub>[ttl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/ttl)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/ttl</sub>|<sub>TRIAL</sub>|
|<sub>[txtRecords](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/txtRecords)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/txtRecords</sub>|<sub>TRIAL</sub>|
|<sub>[txtRecords[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/privateDnsZones/CNAME/txtRecords[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/privateDnsZones/CNAME/txtRecords[*]</sub>|<sub>TRIAL</sub>|

### Assess


Technologies that are promising and have clear potential value-add for us; technologies worth investing some research and prototyping efforts to see if it has impact.  ASSESS technologies have higher risks;  they are often new to our organization and highly unproven within RBA.  You will find some engineers that have knowledge in the technology and promote it, you may even find teams that have started a prototyping effort.  These technologies can also include services that are currently in architecture or security review.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***