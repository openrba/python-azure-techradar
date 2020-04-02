
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
|[addressSpace](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/addressSpace/README.md)|UNKNOWN|Microsoft.Network/vpnSites/addressSpace|TRIAL|
|[addressSpace.addressPrefixes](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/addressSpace.addressPrefixes/README.md)|UNKNOWN|Microsoft.Network/vpnSites/addressSpace.addressPrefixes|TRIAL|
|[addressSpace.addressPrefixes[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/addressSpace.addressPrefixes[*]/README.md)|UNKNOWN|Microsoft.Network/vpnSites/addressSpace.addressPrefixes[*]|TRIAL|
|[bgpProperties](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/bgpProperties/README.md)|UNKNOWN|Microsoft.Network/vpnSites/bgpProperties|TRIAL|
|[bgpProperties.asn](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/bgpProperties.asn/README.md)|UNKNOWN|Microsoft.Network/vpnSites/bgpProperties.asn|TRIAL|
|[bgpProperties.bgpPeeringAddress](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/bgpProperties.bgpPeeringAddress/README.md)|UNKNOWN|Microsoft.Network/vpnSites/bgpProperties.bgpPeeringAddress|TRIAL|
|[bgpProperties.peerWeight](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/bgpProperties.peerWeight/README.md)|UNKNOWN|Microsoft.Network/vpnSites/bgpProperties.peerWeight|TRIAL|
|[deviceProperties](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/deviceProperties/README.md)|UNKNOWN|Microsoft.Network/vpnSites/deviceProperties|TRIAL|
|[deviceProperties.deviceModel](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/deviceProperties.deviceModel/README.md)|UNKNOWN|Microsoft.Network/vpnSites/deviceProperties.deviceModel|TRIAL|
|[deviceProperties.deviceVendor](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/deviceProperties.deviceVendor/README.md)|UNKNOWN|Microsoft.Network/vpnSites/deviceProperties.deviceVendor|TRIAL|
|[deviceProperties.linkSpeedInMbps](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/deviceProperties.linkSpeedInMbps/README.md)|UNKNOWN|Microsoft.Network/vpnSites/deviceProperties.linkSpeedInMbps|TRIAL|
|[ipAddress](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/ipAddress/README.md)|UNKNOWN|Microsoft.Network/vpnSites/ipAddress|TRIAL|
|[isSecuritySite](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/isSecuritySite/README.md)|UNKNOWN|Microsoft.Network/vpnSites/isSecuritySite|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/provisioningState/README.md)|UNKNOWN|Microsoft.Network/vpnSites/provisioningState|TRIAL|
|[siteKey](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/siteKey/README.md)|UNKNOWN|Microsoft.Network/vpnSites/siteKey|TRIAL|
|[virtualWAN](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/virtualWAN/README.md)|UNKNOWN|Microsoft.Network/vpnSites/virtualWAN|TRIAL|
|[virtualWAN.id](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/virtualWAN.id/README.md)|UNKNOWN|Microsoft.Network/vpnSites/virtualWAN.id|TRIAL|
|[vpnSiteLinks](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks|TRIAL|
|[vpnSiteLinks[*]](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*]/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*]|TRIAL|
|[vpnSiteLinks[*].bgpProperties](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].bgpProperties/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].bgpProperties|TRIAL|
|[vpnSiteLinks[*].bgpProperties.asn](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].bgpProperties.asn/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].bgpProperties.asn|TRIAL|
|[vpnSiteLinks[*].bgpProperties.bgpPeeringAddress](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].bgpProperties.bgpPeeringAddress/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].bgpProperties.bgpPeeringAddress|TRIAL|
|[vpnSiteLinks[*].etag](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].etag/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].etag|TRIAL|
|[vpnSiteLinks[*].id](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].id/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].id|TRIAL|
|[vpnSiteLinks[*].ipAddress](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].ipAddress/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].ipAddress|TRIAL|
|[vpnSiteLinks[*].linkProperties](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].linkProperties/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].linkProperties|TRIAL|
|[vpnSiteLinks[*].linkProperties.linkProviderName](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].linkProperties.linkProviderName/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].linkProperties.linkProviderName|TRIAL|
|[vpnSiteLinks[*].linkProperties.linkSpeedInMbps](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].linkProperties.linkSpeedInMbps/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].linkProperties.linkSpeedInMbps|TRIAL|
|[vpnSiteLinks[*].name](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].name/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].name|TRIAL|
|[vpnSiteLinks[*].provisioningState](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].provisioningState/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].provisioningState|TRIAL|
|[vpnSiteLinks[*].type](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Network/vpnSites/vpnSiteLinks[*].type/README.md)|UNKNOWN|Microsoft.Network/vpnSites/vpnSiteLinks[*].type|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***