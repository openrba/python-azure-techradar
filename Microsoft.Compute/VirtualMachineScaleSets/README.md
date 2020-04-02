
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
|[computerNamePrefix](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/computerNamePrefix)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/computerNamePrefix|TRIAL|
|[extensionProfile](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile|TRIAL|
|[extensionProfile.extensions[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*])|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*]|TRIAL|
|[extensionProfile.extensions[*].autoUpgradeMinorVersion](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].autoUpgradeMinorVersion)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].autoUpgradeMinorVersion|TRIAL|
|[extensionProfile.extensions[*].enableAutomaticUpgrade](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].enableAutomaticUpgrade)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].enableAutomaticUpgrade|TRIAL|
|[extensionProfile.extensions[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].name)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].name|TRIAL|
|[extensionProfile.extensions[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].provisioningState)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].provisioningState|TRIAL|
|[extensionProfile.extensions[*].publisher](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].publisher)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].publisher|TRIAL|
|[extensionProfile.extensions[*].settings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings|TRIAL|
|[extensionProfile.extensions[*].settings.workspaceId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings.workspaceId)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings.workspaceId|TRIAL|
|[extensionProfile.extensions[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].type)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].type|TRIAL|
|[extensionProfile.extensions[*].typeHandlerVersion](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].typeHandlerVersion)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].typeHandlerVersion|TRIAL|
|[networkInterfaceConfigurations[*].enableIPForwarding](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].enableIPForwarding)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].enableIPForwarding|TRIAL|
|[networkInterfaceConfigurations[*].ipConfigurations[*].subnet.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].ipConfigurations[*].subnet.id)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].ipConfigurations[*].subnet.id|TRIAL|
|[networkInterfaceConfigurations[*].networkSecurityGroup.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].networkSecurityGroup.id)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].networkSecurityGroup.id|TRIAL|
|[networkProfile.healthProbe.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkProfile.healthProbe.id)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/networkProfile.healthProbe.id|TRIAL|
|[osDisk.caching](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.caching)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osDisk.caching|TRIAL|
|[osDisk.createOption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.createOption)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osDisk.createOption|TRIAL|
|[osDisk.managedDisk.storageAccountType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.managedDisk.storageAccountType)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osDisk.managedDisk.storageAccountType|TRIAL|
|[osDisk.name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.name)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osDisk.name|TRIAL|
|[osProfile.adminPassword](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminPassword)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminPassword|TRIAL|
|[osProfile.adminUsername](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminUsername)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminUsername|TRIAL|
|[osProfile.linuxConfiguration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration|TRIAL|
|[osProfile.linuxConfiguration.disablePasswordAuthentication](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration.disablePasswordAuthentication)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration.disablePasswordAuthentication|TRIAL|
|[osProfile.windowsConfiguration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration|TRIAL|
|[osProfile.windowsConfiguration.enableAutomaticUpdates](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.enableAutomaticUpdates)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.enableAutomaticUpdates|TRIAL|
|[osProfile.windowsConfiguration.provisionVMAgent](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.provisionVMAgent)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.provisionVMAgent|TRIAL|
|[osdisk.imageUrl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osdisk.imageUrl)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osdisk.imageUrl|TRIAL|
|[osdisk.vhdContainers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osdisk.vhdContainers)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/osdisk.vhdContainers|TRIAL|
|[sku.name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/sku.name)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/sku.name|TRIAL|
|[sku.tier](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/sku.tier)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/sku.tier|TRIAL|
|[upgradePolicy.automaticOSUpgrade](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/upgradePolicy.automaticOSUpgrade)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/upgradePolicy.automaticOSUpgrade|TRIAL|
|[virtualMachineProfile](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/virtualMachineProfile)|UNKNOWN|Microsoft.Compute/VirtualMachineScaleSets/virtualMachineProfile|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***