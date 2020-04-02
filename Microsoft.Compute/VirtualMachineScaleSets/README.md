
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
|<sub>[computerNamePrefix](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/computerNamePrefix)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/computerNamePrefix</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*])</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*]</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].autoUpgradeMinorVersion](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].autoUpgradeMinorVersion)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].autoUpgradeMinorVersion</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].enableAutomaticUpgrade](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].enableAutomaticUpgrade)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].enableAutomaticUpgrade</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].name</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].provisioningState)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].provisioningState</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].publisher](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].publisher)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].publisher</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].settings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].settings.workspaceId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings.workspaceId)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].settings.workspaceId</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].type)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].type</sub>|<sub>TRIAL</sub>|
|<sub>[extensionProfile.extensions[*].typeHandlerVersion](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].typeHandlerVersion)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/extensionProfile.extensions[*].typeHandlerVersion</sub>|<sub>TRIAL</sub>|
|<sub>[networkInterfaceConfigurations[*].enableIPForwarding](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].enableIPForwarding)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].enableIPForwarding</sub>|<sub>TRIAL</sub>|
|<sub>[networkInterfaceConfigurations[*].ipConfigurations[*].subnet.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].ipConfigurations[*].subnet.id)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].ipConfigurations[*].subnet.id</sub>|<sub>TRIAL</sub>|
|<sub>[networkInterfaceConfigurations[*].networkSecurityGroup.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].networkSecurityGroup.id)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/networkInterfaceConfigurations[*].networkSecurityGroup.id</sub>|<sub>TRIAL</sub>|
|<sub>[networkProfile.healthProbe.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/networkProfile.healthProbe.id)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/networkProfile.healthProbe.id</sub>|<sub>TRIAL</sub>|
|<sub>[osDisk.caching](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.caching)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osDisk.caching</sub>|<sub>TRIAL</sub>|
|<sub>[osDisk.createOption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.createOption)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osDisk.createOption</sub>|<sub>TRIAL</sub>|
|<sub>[osDisk.managedDisk.storageAccountType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.managedDisk.storageAccountType)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osDisk.managedDisk.storageAccountType</sub>|<sub>TRIAL</sub>|
|<sub>[osDisk.name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osDisk.name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osDisk.name</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.adminPassword](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminPassword)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminPassword</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.adminUsername](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminUsername)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.adminUsername</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.linuxConfiguration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.linuxConfiguration.disablePasswordAuthentication](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration.disablePasswordAuthentication)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.linuxConfiguration.disablePasswordAuthentication</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.windowsConfiguration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.windowsConfiguration.enableAutomaticUpdates](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.enableAutomaticUpdates)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.enableAutomaticUpdates</sub>|<sub>TRIAL</sub>|
|<sub>[osProfile.windowsConfiguration.provisionVMAgent](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.provisionVMAgent)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osProfile.windowsConfiguration.provisionVMAgent</sub>|<sub>TRIAL</sub>|
|<sub>[osdisk.imageUrl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osdisk.imageUrl)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osdisk.imageUrl</sub>|<sub>TRIAL</sub>|
|<sub>[osdisk.vhdContainers](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/osdisk.vhdContainers)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/osdisk.vhdContainers</sub>|<sub>TRIAL</sub>|
|<sub>[sku.name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/sku.name)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/sku.name</sub>|<sub>TRIAL</sub>|
|<sub>[sku.tier](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/sku.tier)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/sku.tier</sub>|<sub>TRIAL</sub>|
|<sub>[upgradePolicy.automaticOSUpgrade](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/upgradePolicy.automaticOSUpgrade)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/upgradePolicy.automaticOSUpgrade</sub>|<sub>TRIAL</sub>|
|<sub>[virtualMachineProfile](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/VirtualMachineScaleSets/virtualMachineProfile)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute/VirtualMachineScaleSets/virtualMachineProfile</sub>|<sub>TRIAL</sub>|

### Assess


Technologies that are promising and have clear potential value-add for us; technologies worth investing some research and prototyping efforts to see if it has impact.  ASSESS technologies have higher risks;  they are often new to our organization and highly unproven within RBA.  You will find some engineers that have knowledge in the technology and promote it, you may even find teams that have started a prototyping effort.  These technologies can also include services that are currently in architecture or security review.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***