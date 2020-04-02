
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
|<sub>[customHeaders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/customHeaders)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/customHeaders</sub>|<sub>TRIAL</sub>|
|<sub>[customHeaders[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/customHeaders[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/customHeaders[*]</sub>|<sub>TRIAL</sub>|
|<sub>[customHeaders[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/customHeaders[*].name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/customHeaders[*].name</sub>|<sub>TRIAL</sub>|
|<sub>[dnsConfig](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/dnsConfig)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/dnsConfig</sub>|<sub>TRIAL</sub>|
|<sub>[dnsConfig.fqdn](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/dnsConfig.fqdn)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/dnsConfig.fqdn</sub>|<sub>TRIAL</sub>|
|<sub>[dnsConfig.relativeName](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/dnsConfig.relativeName)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/dnsConfig.relativeName</sub>|<sub>TRIAL</sub>|
|<sub>[dnsConfig.ttl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/dnsConfig.ttl)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/dnsConfig.ttl</sub>|<sub>TRIAL</sub>|
|<sub>[endpointLocation](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpointLocation)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpointLocation</sub>|<sub>TRIAL</sub>|
|<sub>[endpointMonitorStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpointMonitorStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpointMonitorStatus</sub>|<sub>TRIAL</sub>|
|<sub>[endpointStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpointStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpointStatus</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*]</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].customHeaders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].customHeaders[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders[*]</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].customHeaders[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders[*].name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders[*].name</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].customHeaders[*].value](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders[*].value)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].customHeaders[*].value</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].endpointLocation](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].endpointLocation)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].endpointLocation</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].endpointMonitorStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].endpointMonitorStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].endpointMonitorStatus</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].endpointStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].endpointStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].endpointStatus</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].geoMapping](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].geoMapping)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].geoMapping</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].geoMapping[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].geoMapping[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].geoMapping[*]</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].id)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].id</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].minChildEndpoints](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].minChildEndpoints)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].minChildEndpoints</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].name</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].priority](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].priority)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].priority</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].subnets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].subnets[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*]</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].subnets[*].first](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*].first)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*].first</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].subnets[*].last](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*].last)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*].last</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].subnets[*].scope](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*].scope)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].subnets[*].scope</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].target](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].target)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].target</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].targetResourceId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].targetResourceId)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].targetResourceId</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].type)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].type</sub>|<sub>TRIAL</sub>|
|<sub>[endpoints[*].weight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/endpoints[*].weight)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/endpoints[*].weight</sub>|<sub>TRIAL</sub>|
|<sub>[geoMapping](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/geoMapping)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/geoMapping</sub>|<sub>TRIAL</sub>|
|<sub>[geoMapping[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/geoMapping[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/geoMapping[*]</sub>|<sub>TRIAL</sub>|
|<sub>[heatMaps](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/heatMaps)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/heatMaps</sub>|<sub>TRIAL</sub>|
|<sub>[maxReturn](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/maxReturn)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/maxReturn</sub>|<sub>TRIAL</sub>|
|<sub>[minChildEndpoints](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/minChildEndpoints)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/minChildEndpoints</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.customHeaders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.customHeaders[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders[*]</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.customHeaders[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders[*].name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders[*].name</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.customHeaders[*].value](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders[*].value)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.customHeaders[*].value</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.expectedStatusCodeRanges](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.expectedStatusCodeRanges[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges[*]</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.expectedStatusCodeRanges[*].max](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges[*].max)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges[*].max</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.expectedStatusCodeRanges[*].min](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges[*].min)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.expectedStatusCodeRanges[*].min</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.intervalInSeconds](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.intervalInSeconds)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.intervalInSeconds</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.path](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.path)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.path</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.port](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.port)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.port</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.profileMonitorStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.profileMonitorStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.profileMonitorStatus</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.protocol](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.protocol)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.protocol</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.timeoutInSeconds](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.timeoutInSeconds)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.timeoutInSeconds</sub>|<sub>TRIAL</sub>|
|<sub>[monitorConfig.toleratedNumberOfFailures](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/monitorConfig.toleratedNumberOfFailures)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/monitorConfig.toleratedNumberOfFailures</sub>|<sub>TRIAL</sub>|
|<sub>[priority](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/priority)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/priority</sub>|<sub>TRIAL</sub>|
|<sub>[profileStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/profileStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/profileStatus</sub>|<sub>TRIAL</sub>|
|<sub>[subnets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/subnets)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/subnets</sub>|<sub>TRIAL</sub>|
|<sub>[subnets[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/subnets[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/subnets[*]</sub>|<sub>TRIAL</sub>|
|<sub>[subnets[*].first](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/subnets[*].first)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/subnets[*].first</sub>|<sub>TRIAL</sub>|
|<sub>[subnets[*].last](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/subnets[*].last)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/subnets[*].last</sub>|<sub>TRIAL</sub>|
|<sub>[subnets[*].scope](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/subnets[*].scope)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/subnets[*].scope</sub>|<sub>TRIAL</sub>|
|<sub>[target](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/target)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/target</sub>|<sub>TRIAL</sub>|
|<sub>[targetResourceId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/targetResourceId)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/targetResourceId</sub>|<sub>TRIAL</sub>|
|<sub>[trafficRoutingMethod](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/trafficRoutingMethod)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/trafficRoutingMethod</sub>|<sub>TRIAL</sub>|
|<sub>[trafficViewEnrollmentStatus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/trafficViewEnrollmentStatus)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/trafficViewEnrollmentStatus</sub>|<sub>TRIAL</sub>|
|<sub>[weight](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network/trafficmanagerprofiles/weight)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network/trafficmanagerprofiles/weight</sub>|<sub>TRIAL</sub>|

### Assess


Technologies that are promising and have clear potential value-add for us; technologies worth investing some research and prototyping efforts to see if it has impact.  ASSESS technologies have higher risks;  they are often new to our organization and highly unproven within RBA.  You will find some engineers that have knowledge in the technology and promote it, you may even find teams that have started a prototyping effort.  These technologies can also include services that are currently in architecture or security review.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***