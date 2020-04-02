
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
|[accountType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/accountType)|UNKNOWN|Microsoft.Compute/disks/accountType|TRIAL|
|[creationData](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData)|UNKNOWN|Microsoft.Compute/disks/creationData|TRIAL|
|[creationData.createOption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.createOption)|UNKNOWN|Microsoft.Compute/disks/creationData.createOption|TRIAL|
|[creationData.imageReference](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.imageReference)|UNKNOWN|Microsoft.Compute/disks/creationData.imageReference|TRIAL|
|[creationData.imageReference.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.imageReference.id)|UNKNOWN|Microsoft.Compute/disks/creationData.imageReference.id|TRIAL|
|[creationData.imageReference.lun](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.imageReference.lun)|UNKNOWN|Microsoft.Compute/disks/creationData.imageReference.lun|TRIAL|
|[creationData.sourceResourceId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.sourceResourceId)|UNKNOWN|Microsoft.Compute/disks/creationData.sourceResourceId|TRIAL|
|[creationData.sourceUniqueId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.sourceUniqueId)|UNKNOWN|Microsoft.Compute/disks/creationData.sourceUniqueId|TRIAL|
|[creationData.sourceUri](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.sourceUri)|UNKNOWN|Microsoft.Compute/disks/creationData.sourceUri|TRIAL|
|[creationData.storageAccountId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.storageAccountId)|UNKNOWN|Microsoft.Compute/disks/creationData.storageAccountId|TRIAL|
|[creationData.uploadSizeBytes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/creationData.uploadSizeBytes)|UNKNOWN|Microsoft.Compute/disks/creationData.uploadSizeBytes|TRIAL|
|[diskIOPSReadWrite](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/diskIOPSReadWrite)|UNKNOWN|Microsoft.Compute/disks/diskIOPSReadWrite|TRIAL|
|[diskMBpsReadWrite](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/diskMBpsReadWrite)|UNKNOWN|Microsoft.Compute/disks/diskMBpsReadWrite|TRIAL|
|[diskSizeBytes](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/diskSizeBytes)|UNKNOWN|Microsoft.Compute/disks/diskSizeBytes|TRIAL|
|[diskSizeGB](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/diskSizeGB)|UNKNOWN|Microsoft.Compute/disks/diskSizeGB|TRIAL|
|[diskState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/diskState)|UNKNOWN|Microsoft.Compute/disks/diskState|TRIAL|
|[encryption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryption)|UNKNOWN|Microsoft.Compute/disks/encryption|TRIAL|
|[encryption.diskEncryptionSetId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryption.diskEncryptionSetId)|UNKNOWN|Microsoft.Compute/disks/encryption.diskEncryptionSetId|TRIAL|
|[encryption.type](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryption.type)|UNKNOWN|Microsoft.Compute/disks/encryption.type|TRIAL|
|[encryptionSettings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings|TRIAL|
|[encryptionSettings.diskEncryptionKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey|TRIAL|
|[encryptionSettings.diskEncryptionKey.secretUrl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey.secretUrl)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey.secretUrl|TRIAL|
|[encryptionSettings.diskEncryptionKey.sourceVault](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey.sourceVault)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey.sourceVault|TRIAL|
|[encryptionSettings.diskEncryptionKey.sourceVault.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey.sourceVault.id)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.diskEncryptionKey.sourceVault.id|TRIAL|
|[encryptionSettings.enabled](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.enabled)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.enabled|TRIAL|
|[encryptionSettings.keyEncryptionKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey|TRIAL|
|[encryptionSettings.keyEncryptionKey.keyUrl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey.keyUrl)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey.keyUrl|TRIAL|
|[encryptionSettings.keyEncryptionKey.sourceVault](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey.sourceVault)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey.sourceVault|TRIAL|
|[encryptionSettings.keyEncryptionKey.sourceVault.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey.sourceVault.id)|UNKNOWN|Microsoft.Compute/disks/encryptionSettings.keyEncryptionKey.sourceVault.id|TRIAL|
|[encryptionSettingsCollection](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection|TRIAL|
|[encryptionSettingsCollection.enabled](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.enabled)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.enabled|TRIAL|
|[encryptionSettingsCollection.encryptionSettings](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings|TRIAL|
|[encryptionSettingsCollection.encryptionSettingsVersion](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettingsVersion)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettingsVersion|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*])|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*]|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.secretUrl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.secretUrl)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.secretUrl|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.sourceVault](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.sourceVault)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.sourceVault|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.sourceVault.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.sourceVault.id)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].diskEncryptionKey.sourceVault.id|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.keyUrl](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.keyUrl)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.keyUrl|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.sourceVault](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.sourceVault)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.sourceVault|TRIAL|
|[encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.sourceVault.id](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.sourceVault.id)|UNKNOWN|Microsoft.Compute/disks/encryptionSettingsCollection.encryptionSettings[*].keyEncryptionKey.sourceVault.id|TRIAL|
|[hyperVGeneration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/hyperVGeneration)|UNKNOWN|Microsoft.Compute/disks/hyperVGeneration|TRIAL|
|[managedBy](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/managedBy)|UNKNOWN|Microsoft.Compute/disks/managedBy|TRIAL|
|[osType](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/osType)|UNKNOWN|Microsoft.Compute/disks/osType|TRIAL|
|[ownerId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/ownerId)|UNKNOWN|Microsoft.Compute/disks/ownerId|TRIAL|
|[provisioningState](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/provisioningState)|UNKNOWN|Microsoft.Compute/disks/provisioningState|TRIAL|
|[sku](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/sku)|UNKNOWN|Microsoft.Compute/disks/sku|TRIAL|
|[sku.name](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/sku.name)|UNKNOWN|Microsoft.Compute/disks/sku.name|TRIAL|
|[sku.tier](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/sku.tier)|UNKNOWN|Microsoft.Compute/disks/sku.tier|TRIAL|
|[timeCreated](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/timeCreated)|UNKNOWN|Microsoft.Compute/disks/timeCreated|TRIAL|
|[uniqueId](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/uniqueId)|UNKNOWN|Microsoft.Compute/disks/uniqueId|TRIAL|
|[zones](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/zones)|UNKNOWN|Microsoft.Compute/disks/zones|TRIAL|
|[zones[*]](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute/disks/zones[*])|UNKNOWN|Microsoft.Compute/disks/zones[*]|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***