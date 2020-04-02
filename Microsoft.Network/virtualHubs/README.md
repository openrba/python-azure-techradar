
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
|[addressPrefix](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/addressPrefix)|UNKNOWN|Microsoft.Network/virtualHubs/addressPrefix|TRIAL|
|[azureFirewall](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/azureFirewall)|UNKNOWN|Microsoft.Network/virtualHubs/azureFirewall|TRIAL|
|[azureFirewall.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/azureFirewall.id)|UNKNOWN|Microsoft.Network/virtualHubs/azureFirewall.id|TRIAL|
|[expressRouteGateway](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/expressRouteGateway)|UNKNOWN|Microsoft.Network/virtualHubs/expressRouteGateway|TRIAL|
|[expressRouteGateway.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/expressRouteGateway.id)|UNKNOWN|Microsoft.Network/virtualHubs/expressRouteGateway.id|TRIAL|
|[hubVirtualNetworkConnections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections|TRIAL|
|[hubVirtualNetworkConnections[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*])|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*]|TRIAL|
|[hubVirtualNetworkConnections[*].allowHubToRemoteVnetTransit](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].allowHubToRemoteVnetTransit)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].allowHubToRemoteVnetTransit|TRIAL|
|[hubVirtualNetworkConnections[*].allowRemoteVnetToUseHubVnetGateways](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].allowRemoteVnetToUseHubVnetGateways)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].allowRemoteVnetToUseHubVnetGateways|TRIAL|
|[hubVirtualNetworkConnections[*].etag](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].etag)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].etag|TRIAL|
|[hubVirtualNetworkConnections[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].id)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].id|TRIAL|
|[hubVirtualNetworkConnections[*].location](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].location)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].location|TRIAL|
|[hubVirtualNetworkConnections[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].name)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].name|TRIAL|
|[hubVirtualNetworkConnections[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].provisioningState)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].provisioningState|TRIAL|
|[hubVirtualNetworkConnections[*].remoteVirtualNetwork](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].remoteVirtualNetwork)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].remoteVirtualNetwork|TRIAL|
|[hubVirtualNetworkConnections[*].remoteVirtualNetwork.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].remoteVirtualNetwork.id)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].remoteVirtualNetwork.id|TRIAL|
|[hubVirtualNetworkConnections[*].tags](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].tags)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].tags|TRIAL|
|[hubVirtualNetworkConnections[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].type)|UNKNOWN|Microsoft.Network/virtualHubs/hubVirtualNetworkConnections[*].type|TRIAL|
|[p2SVpnGateway](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/p2SVpnGateway)|UNKNOWN|Microsoft.Network/virtualHubs/p2SVpnGateway|TRIAL|
|[p2SVpnGateway.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/p2SVpnGateway.id)|UNKNOWN|Microsoft.Network/virtualHubs/p2SVpnGateway.id|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/provisioningState)|UNKNOWN|Microsoft.Network/virtualHubs/provisioningState|TRIAL|
|[routeTable](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTable)|UNKNOWN|Microsoft.Network/virtualHubs/routeTable|TRIAL|
|[routeTable.routes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTable.routes)|UNKNOWN|Microsoft.Network/virtualHubs/routeTable.routes|TRIAL|
|[routeTable.routes[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTable.routes[*])|UNKNOWN|Microsoft.Network/virtualHubs/routeTable.routes[*]|TRIAL|
|[routeTable.routes[*].addressPrefixes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTable.routes[*].addressPrefixes)|UNKNOWN|Microsoft.Network/virtualHubs/routeTable.routes[*].addressPrefixes|TRIAL|
|[routeTable.routes[*].addressPrefixes[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTable.routes[*].addressPrefixes[*])|UNKNOWN|Microsoft.Network/virtualHubs/routeTable.routes[*].addressPrefixes[*]|TRIAL|
|[routeTable.routes[*].nextHopIpAddress](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTable.routes[*].nextHopIpAddress)|UNKNOWN|Microsoft.Network/virtualHubs/routeTable.routes[*].nextHopIpAddress|TRIAL|
|[routeTables](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/routeTables)|UNKNOWN|Microsoft.Network/virtualHubs/routeTables|TRIAL|
|[securityProviderName](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/securityProviderName)|UNKNOWN|Microsoft.Network/virtualHubs/securityProviderName|TRIAL|
|[sku](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/sku)|UNKNOWN|Microsoft.Network/virtualHubs/sku|TRIAL|
|[virtualHubRouteTableV2s](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s|TRIAL|
|[virtualHubRouteTableV2s[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*])|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*]|TRIAL|
|[virtualHubRouteTableV2s[*].attachedConnections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].attachedConnections)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].attachedConnections|TRIAL|
|[virtualHubRouteTableV2s[*].attachedConnections[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].attachedConnections[*])|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].attachedConnections[*]|TRIAL|
|[virtualHubRouteTableV2s[*].etag](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].etag)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].etag|TRIAL|
|[virtualHubRouteTableV2s[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].id)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].id|TRIAL|
|[virtualHubRouteTableV2s[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].name)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].name|TRIAL|
|[virtualHubRouteTableV2s[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].provisioningState)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].provisioningState|TRIAL|
|[virtualHubRouteTableV2s[*].routes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*])|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*]|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*].destinationType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].destinationType)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].destinationType|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*].destinations](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].destinations)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].destinations|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*].destinations[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].destinations[*])|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].destinations[*]|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*].nextHopType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].nextHopType)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].nextHopType|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*].nextHops](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].nextHops)|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].nextHops|TRIAL|
|[virtualHubRouteTableV2s[*].routes[*].nextHops[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].nextHops[*])|UNKNOWN|Microsoft.Network/virtualHubs/virtualHubRouteTableV2s[*].routes[*].nextHops[*]|TRIAL|
|[virtualNetworkConnections](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections|TRIAL|
|[virtualNetworkConnections[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*])|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*]|TRIAL|
|[virtualNetworkConnections[*].allowHubToRemoteVnetTransit](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].allowHubToRemoteVnetTransit)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].allowHubToRemoteVnetTransit|TRIAL|
|[virtualNetworkConnections[*].allowRemoteVnetToUseHubVnetGateways](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].allowRemoteVnetToUseHubVnetGateways)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].allowRemoteVnetToUseHubVnetGateways|TRIAL|
|[virtualNetworkConnections[*].enableInternetSecurity](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].enableInternetSecurity)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].enableInternetSecurity|TRIAL|
|[virtualNetworkConnections[*].etag](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].etag)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].etag|TRIAL|
|[virtualNetworkConnections[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].id)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].id|TRIAL|
|[virtualNetworkConnections[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].name)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].name|TRIAL|
|[virtualNetworkConnections[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].provisioningState)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].provisioningState|TRIAL|
|[virtualNetworkConnections[*].remoteVirtualNetwork](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].remoteVirtualNetwork)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].remoteVirtualNetwork|TRIAL|
|[virtualNetworkConnections[*].remoteVirtualNetwork.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualNetworkConnections[*].remoteVirtualNetwork.id)|UNKNOWN|Microsoft.Network/virtualHubs/virtualNetworkConnections[*].remoteVirtualNetwork.id|TRIAL|
|[virtualWan](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualWan)|UNKNOWN|Microsoft.Network/virtualHubs/virtualWan|TRIAL|
|[virtualWan.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/virtualWan.id)|UNKNOWN|Microsoft.Network/virtualHubs/virtualWan.id|TRIAL|
|[vpnGateway](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/vpnGateway)|UNKNOWN|Microsoft.Network/virtualHubs/vpnGateway|TRIAL|
|[vpnGateway.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/virtualHubs/vpnGateway.id)|UNKNOWN|Microsoft.Network/virtualHubs/vpnGateway.id|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***