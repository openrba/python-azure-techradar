
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
|[bgpSettings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/bgpSettings)|UNKNOWN|Microsoft.Network/vpnGateways/bgpSettings|TRIAL|
|[bgpSettings.asn](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/bgpSettings.asn)|UNKNOWN|Microsoft.Network/vpnGateways/bgpSettings.asn|TRIAL|
|[bgpSettings.bgpPeeringAddress](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/bgpSettings.bgpPeeringAddress)|UNKNOWN|Microsoft.Network/vpnGateways/bgpSettings.bgpPeeringAddress|TRIAL|
|[bgpSettings.peerWeight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/bgpSettings.peerWeight)|UNKNOWN|Microsoft.Network/vpnGateways/bgpSettings.peerWeight|TRIAL|
|[connections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections)|UNKNOWN|Microsoft.Network/vpnGateways/connections|TRIAL|
|[connections[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*])|UNKNOWN|Microsoft.Network/vpnGateways/connections[*]|TRIAL|
|[connections[*].connectionBandwidth](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].connectionBandwidth)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].connectionBandwidth|TRIAL|
|[connections[*].connectionBandwidthInMbps](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].connectionBandwidthInMbps)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].connectionBandwidthInMbps|TRIAL|
|[connections[*].connectionStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].connectionStatus)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].connectionStatus|TRIAL|
|[connections[*].egressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].egressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].egressBytesTransferred|TRIAL|
|[connections[*].enableBgp](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].enableBgp)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].enableBgp|TRIAL|
|[connections[*].enableInternetSecurity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].enableInternetSecurity)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].enableInternetSecurity|TRIAL|
|[connections[*].enableRateLimiting](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].enableRateLimiting)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].enableRateLimiting|TRIAL|
|[connections[*].etag](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].etag)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].etag|TRIAL|
|[connections[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].id)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].id|TRIAL|
|[connections[*].ingressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ingressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ingressBytesTransferred|TRIAL|
|[connections[*].ipsecPolicies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies|TRIAL|
|[connections[*].ipsecPolicies[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*])|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*]|TRIAL|
|[connections[*].ipsecPolicies[*].dhGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].dhGroup)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].dhGroup|TRIAL|
|[connections[*].ipsecPolicies[*].ikeEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ikeEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ikeEncryption|TRIAL|
|[connections[*].ipsecPolicies[*].ikeIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ikeIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ikeIntegrity|TRIAL|
|[connections[*].ipsecPolicies[*].ipsecEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ipsecEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ipsecEncryption|TRIAL|
|[connections[*].ipsecPolicies[*].ipsecIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ipsecIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].ipsecIntegrity|TRIAL|
|[connections[*].ipsecPolicies[*].pfsGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].pfsGroup)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].pfsGroup|TRIAL|
|[connections[*].ipsecPolicies[*].saDataSizeKilobytes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].saDataSizeKilobytes)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].saDataSizeKilobytes|TRIAL|
|[connections[*].ipsecPolicies[*].saLifeTimeSeconds](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].saLifeTimeSeconds)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].ipsecPolicies[*].saLifeTimeSeconds|TRIAL|
|[connections[*].location](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].location)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].location|TRIAL|
|[connections[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].name)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].name|TRIAL|
|[connections[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].provisioningState)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].provisioningState|TRIAL|
|[connections[*].remoteVpnSite](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].remoteVpnSite)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].remoteVpnSite|TRIAL|
|[connections[*].remoteVpnSite.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].remoteVpnSite.id)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].remoteVpnSite.id|TRIAL|
|[connections[*].routingWeight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].routingWeight)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].routingWeight|TRIAL|
|[connections[*].sharedKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].sharedKey)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].sharedKey|TRIAL|
|[connections[*].tags](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].tags)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].tags|TRIAL|
|[connections[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].type)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].type|TRIAL|
|[connections[*].useLocalAzureIpAddress](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].useLocalAzureIpAddress)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].useLocalAzureIpAddress|TRIAL|
|[connections[*].usePolicyBasedTrafficSelectors](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].usePolicyBasedTrafficSelectors)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].usePolicyBasedTrafficSelectors|TRIAL|
|[connections[*].vpnConnectionProtocolType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnConnectionProtocolType)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnConnectionProtocolType|TRIAL|
|[connections[*].vpnLinkConnections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections|TRIAL|
|[connections[*].vpnLinkConnections[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*])|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*]|TRIAL|
|[connections[*].vpnLinkConnections[*].connectionBandwidth](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].connectionBandwidth)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].connectionBandwidth|TRIAL|
|[connections[*].vpnLinkConnections[*].connectionStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].connectionStatus)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].connectionStatus|TRIAL|
|[connections[*].vpnLinkConnections[*].egressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].egressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].egressBytesTransferred|TRIAL|
|[connections[*].vpnLinkConnections[*].enableBgp](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].enableBgp)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].enableBgp|TRIAL|
|[connections[*].vpnLinkConnections[*].enableRateLimiting](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].enableRateLimiting)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].enableRateLimiting|TRIAL|
|[connections[*].vpnLinkConnections[*].etag](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].etag)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].etag|TRIAL|
|[connections[*].vpnLinkConnections[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].id)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].id|TRIAL|
|[connections[*].vpnLinkConnections[*].ingressBytesTransferred](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ingressBytesTransferred)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ingressBytesTransferred|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*])|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*]|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].dhGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].dhGroup)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].dhGroup|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].ikeEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ikeEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ikeEncryption|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].ikeIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ikeIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ikeIntegrity|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].ipsecEncryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ipsecEncryption)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ipsecEncryption|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].ipsecIntegrity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ipsecIntegrity)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].ipsecIntegrity|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].pfsGroup](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].pfsGroup)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].pfsGroup|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].saDataSizeKilobytes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].saDataSizeKilobytes)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].saDataSizeKilobytes|TRIAL|
|[connections[*].vpnLinkConnections[*].ipsecPolicies[*].saLifeTimeSeconds](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].saLifeTimeSeconds)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].ipsecPolicies[*].saLifeTimeSeconds|TRIAL|
|[connections[*].vpnLinkConnections[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].name)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].name|TRIAL|
|[connections[*].vpnLinkConnections[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].provisioningState)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].provisioningState|TRIAL|
|[connections[*].vpnLinkConnections[*].routingWeight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].routingWeight)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].routingWeight|TRIAL|
|[connections[*].vpnLinkConnections[*].sharedKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].sharedKey)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].sharedKey|TRIAL|
|[connections[*].vpnLinkConnections[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].type)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].type|TRIAL|
|[connections[*].vpnLinkConnections[*].useLocalAzureIpAddress](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].useLocalAzureIpAddress)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].useLocalAzureIpAddress|TRIAL|
|[connections[*].vpnLinkConnections[*].usePolicyBasedTrafficSelectors](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].usePolicyBasedTrafficSelectors)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].usePolicyBasedTrafficSelectors|TRIAL|
|[connections[*].vpnLinkConnections[*].vpnConnectionProtocolType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].vpnConnectionProtocolType)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].vpnConnectionProtocolType|TRIAL|
|[connections[*].vpnLinkConnections[*].vpnSiteLink](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].vpnSiteLink)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].vpnSiteLink|TRIAL|
|[connections[*].vpnLinkConnections[*].vpnSiteLink.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].vpnSiteLink.id)|UNKNOWN|Microsoft.Network/vpnGateways/connections[*].vpnLinkConnections[*].vpnSiteLink.id|TRIAL|
|[policies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/policies)|UNKNOWN|Microsoft.Network/vpnGateways/policies|TRIAL|
|[policies.allowBranchToBranchTraffic](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/policies.allowBranchToBranchTraffic)|UNKNOWN|Microsoft.Network/vpnGateways/policies.allowBranchToBranchTraffic|TRIAL|
|[policies.allowVnetToVnetTraffic](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/policies.allowVnetToVnetTraffic)|UNKNOWN|Microsoft.Network/vpnGateways/policies.allowVnetToVnetTraffic|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/provisioningState)|UNKNOWN|Microsoft.Network/vpnGateways/provisioningState|TRIAL|
|[virtualHub](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/virtualHub)|UNKNOWN|Microsoft.Network/vpnGateways/virtualHub|TRIAL|
|[virtualHub.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/virtualHub.id)|UNKNOWN|Microsoft.Network/vpnGateways/virtualHub.id|TRIAL|
|[vpnConnections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnConnections)|UNKNOWN|Microsoft.Network/vpnGateways/vpnConnections|TRIAL|
|[vpnGatewayScaleUnit](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/vpnGateways/vpnGatewayScaleUnit)|UNKNOWN|Microsoft.Network/vpnGateways/vpnGatewayScaleUnit|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***