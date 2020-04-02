
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

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Path</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>[apiVersionSets](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/apiVersionSets)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/apiVersionSets</sub>|<sub>ADOPT</sub>|
|<sub>[apis](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/apis)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/apis</sub>|<sub>ADOPT</sub>|
|<sub>[authorizationServers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/authorizationServers)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/authorizationServers</sub>|<sub>ADOPT</sub>|
|<sub>[backends](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/backends)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/backends</sub>|<sub>ADOPT</sub>|
|<sub>[caches](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/caches)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/caches</sub>|<sub>ADOPT</sub>|
|<sub>[diagnostics](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/diagnostics)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/diagnostics</sub>|<sub>ADOPT</sub>|
|<sub>[groups](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/groups)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/groups</sub>|<sub>ADOPT</sub>|
|<sub>[identityProviders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/identityProviders)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/identityProviders</sub>|<sub>ADOPT</sub>|
|<sub>[loggers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/loggers)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/loggers</sub>|<sub>ADOPT</sub>|
|<sub>[notifications](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/notifications)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/notifications</sub>|<sub>ADOPT</sub>|
|<sub>[openidConnectProviders](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/openidConnectProviders)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/openidConnectProviders</sub>|<sub>ADOPT</sub>|
|<sub>[policies](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/policies)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/policies</sub>|<sub>ADOPT</sub>|
|<sub>[portalsettings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/portalsettings)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/portalsettings</sub>|<sub>ADOPT</sub>|
|<sub>[products](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/products)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/products</sub>|<sub>ADOPT</sub>|
|<sub>[properties](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/properties)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/properties</sub>|<sub>ADOPT</sub>|
|<sub>[subscriptions](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/subscriptions)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/subscriptions</sub>|<sub>ADOPT</sub>|
|<sub>[tags](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/tags)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/tags</sub>|<sub>ADOPT</sub>|
|<sub>[templates](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/templates)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/templates</sub>|<sub>ADOPT</sub>|
|<sub>[users](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory/service/users)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory/service/users</sub>|<sub>ADOPT</sub>|

### Trial


Technologies that we have seen work with success in projects to solve real problems;  first serious usage experience that confirm benefits and uncover limitations.  TRIAL technologies are slightly more risky; some engineers in our organization walked this path and will share knowledge and experiences.  This area can contain services that have been architecture and security reviewed but do not contain automated policy managmeent.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Assess


Technologies that are promising and have clear potential value-add for us; technologies worth investing some research and prototyping efforts to see if it has impact.  ASSESS technologies have higher risks;  they are often new to our organization and highly unproven within RBA.  You will find some engineers that have knowledge in the technology and promote it, you may even find teams that have started a prototyping effort.  These technologies can also include services that are currently in architecture or security review.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***