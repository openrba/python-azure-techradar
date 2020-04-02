
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
|[connectionBandwidth](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/connectionBandwidth)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/connectionBandwidth|TRIAL|
|[connectionBandwidthInMbps](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/connectionBandwidthInMbps)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/connectionBandwidthInMbps|TRIAL|
|[connectionStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/connectionStatus)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/connectionStatus|TRIAL|
|[egressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/egressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/egressBytesTransferred|TRIAL|
|[enableBgp](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/enableBgp)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/enableBgp|TRIAL|
|[enableInternetSecurity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/enableInternetSecurity)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/enableInternetSecurity|TRIAL|
|[enableRateLimiting](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/enableRateLimiting)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/enableRateLimiting|TRIAL|
|[ingressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ingressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ingressBytesTransferred|TRIAL|
|[ipsecPolicies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies|TRIAL|
|[ipsecPolicies[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*])|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*]|TRIAL|
|[ipsecPolicies[*].dhGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].dhGroup)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].dhGroup|TRIAL|
|[ipsecPolicies[*].ikeEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ikeEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ikeEncryption|TRIAL|
|[ipsecPolicies[*].ikeIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ikeIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ikeIntegrity|TRIAL|
|[ipsecPolicies[*].ipsecEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ipsecEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ipsecEncryption|TRIAL|
|[ipsecPolicies[*].ipsecIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ipsecIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].ipsecIntegrity|TRIAL|
|[ipsecPolicies[*].pfsGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].pfsGroup)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].pfsGroup|TRIAL|
|[ipsecPolicies[*].saDataSizeKilobytes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].saDataSizeKilobytes)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].saDataSizeKilobytes|TRIAL|
|[ipsecPolicies[*].saLifeTimeSeconds](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].saLifeTimeSeconds)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/ipsecPolicies[*].saLifeTimeSeconds|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/provisioningState)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/provisioningState|TRIAL|
|[remoteVpnSite](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/remoteVpnSite)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/remoteVpnSite|TRIAL|
|[remoteVpnSite.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/remoteVpnSite.id)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/remoteVpnSite.id|TRIAL|
|[routingWeight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/routingWeight)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/routingWeight|TRIAL|
|[sharedKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/sharedKey)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/sharedKey|TRIAL|
|[useLocalAzureIpAddress](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/useLocalAzureIpAddress)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/useLocalAzureIpAddress|TRIAL|
|[usePolicyBasedTrafficSelectors](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/usePolicyBasedTrafficSelectors)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/usePolicyBasedTrafficSelectors|TRIAL|
|[vpnConnectionProtocolType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnConnectionProtocolType)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnConnectionProtocolType|TRIAL|
|[vpnLinkConnections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections|TRIAL|
|[vpnLinkConnections[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*])|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*]|TRIAL|
|[vpnLinkConnections[*].connectionBandwidth](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].connectionBandwidth)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].connectionBandwidth|TRIAL|
|[vpnLinkConnections[*].connectionStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].connectionStatus)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].connectionStatus|TRIAL|
|[vpnLinkConnections[*].egressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].egressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].egressBytesTransferred|TRIAL|
|[vpnLinkConnections[*].enableBgp](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].enableBgp)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].enableBgp|TRIAL|
|[vpnLinkConnections[*].enableRateLimiting](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].enableRateLimiting)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].enableRateLimiting|TRIAL|
|[vpnLinkConnections[*].etag](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].etag)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].etag|TRIAL|
|[vpnLinkConnections[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].id)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].id|TRIAL|
|[vpnLinkConnections[*].ingressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ingressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ingressBytesTransferred|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*])|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*]|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].dhGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].dhGroup)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].dhGroup|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].ikeEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ikeEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ikeEncryption|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].ikeIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ikeIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ikeIntegrity|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].ipsecEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ipsecEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ipsecEncryption|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].ipsecIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ipsecIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].ipsecIntegrity|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].pfsGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].pfsGroup)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].pfsGroup|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].saDataSizeKilobytes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].saDataSizeKilobytes)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].saDataSizeKilobytes|TRIAL|
|[vpnLinkConnections[*].ipsecPolicies[*].saLifeTimeSeconds](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].saLifeTimeSeconds)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].ipsecPolicies[*].saLifeTimeSeconds|TRIAL|
|[vpnLinkConnections[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].name)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].name|TRIAL|
|[vpnLinkConnections[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].provisioningState)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].provisioningState|TRIAL|
|[vpnLinkConnections[*].routingWeight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].routingWeight)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].routingWeight|TRIAL|
|[vpnLinkConnections[*].sharedKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].sharedKey)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].sharedKey|TRIAL|
|[vpnLinkConnections[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].type)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].type|TRIAL|
|[vpnLinkConnections[*].useLocalAzureIpAddress](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].useLocalAzureIpAddress)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].useLocalAzureIpAddress|TRIAL|
|[vpnLinkConnections[*].usePolicyBasedTrafficSelectors](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].usePolicyBasedTrafficSelectors)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].usePolicyBasedTrafficSelectors|TRIAL|
|[vpnLinkConnections[*].vpnConnectionProtocolType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].vpnConnectionProtocolType)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].vpnConnectionProtocolType|TRIAL|
|[vpnLinkConnections[*].vpnSiteLink](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].vpnSiteLink)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].vpnSiteLink|TRIAL|
|[vpnLinkConnections[*].vpnSiteLink.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].vpnSiteLink.id)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections[*].vpnSiteLink.id|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***