
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
|<sub>[Microsoft.AzureActiveDirectory](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AzureActiveDirectory)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureActiveDirectory</sub>|<sub>ADOPT</sub>|

### Trial


Technologies that we have seen work with success in projects to solve real problems;  first serious usage experience that confirm benefits and uncover limitations.  TRIAL technologies are slightly more risky; some engineers in our organization walked this path and will share knowledge and experiences.  This area can contain services that have been architecture and security reviewed but do not contain automated policy managmeent.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Path</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>[Microsoft.Compute](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Compute</sub>|<sub>TRIAL</sub>|
|<sub>[Microsoft.DBforPostgreSQL](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DBforPostgreSQL)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DBforPostgreSQL</sub>|<sub>TRIAL</sub>|
|<sub>[Microsoft.Network](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network)</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Network</sub>|<sub>TRIAL</sub>|

### Assess


Technologies that are promising and have clear potential value-add for us; technologies worth investing some research and prototyping efforts to see if it has impact.  ASSESS technologies have higher risks;  they are often new to our organization and highly unproven within RBA.  You will find some engineers that have knowledge in the technology and promote it, you may even find teams that have started a prototyping effort.  These technologies can also include services that are currently in architecture or security review.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***
### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Path</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>Microsoft.AAD</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AAD</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ADHybridHealthService</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ADHybridHealthService</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Addons</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Addons</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Advisor</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Advisor</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AlertsManagement</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AlertsManagement</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AnalysisServices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AnalysisServices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ApiManagement</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ApiManagement</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AppConfiguration</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AppConfiguration</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AppPlatform</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AppPlatform</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Attestation</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Attestation</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Authorization</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Authorization</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Automation</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Automation</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AzureData</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureData</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AzureStack</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.AzureStack</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Batch</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Batch</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.BatchAI</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.BatchAI</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Billing</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Billing</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.BingMaps</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.BingMaps</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Blockchain</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Blockchain</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.BlockchainTokens</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.BlockchainTokens</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Blueprint</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Blueprint</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.BotService</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.BotService</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CDN</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CDN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Cache</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Cache</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Capacity</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Capacity</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Cdn</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Cdn</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CertificateRegistration</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CertificateRegistration</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ChangeAnalysis</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ChangeAnalysis</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CognitiveServices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CognitiveServices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Commerce</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Commerce</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Consumption</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Consumption</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ContainerInstance</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ContainerInstance</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ContainerRegistry</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ContainerRegistry</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ContainerService</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ContainerService</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CostManagement</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CostManagement</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CostManagementExports</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CostManagementExports</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CustomProviders</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CustomProviders</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CustomerLockbox</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.CustomerLockbox</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DBforMariaDB</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DBforMariaDB</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DBforMySQL</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DBforMySQL</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataBox</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataBox</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataBoxEdge</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataBoxEdge</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataBricks</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataBricks</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataCatalog</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataCatalog</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataFactory</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataFactory</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataLakeAnalytics</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataLakeAnalytics</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataLakeStore</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataLakeStore</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataMigration</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataMigration</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataShare</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DataShare</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Databricks</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Databricks</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DeploymentManager</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DeploymentManager</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DesktopVirtualization</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DesktopVirtualization</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DevOps</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DevOps</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DevSpaces</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DevSpaces</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DevTestLab</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DevTestLab</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Devices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Devices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DigitalTwins</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DigitalTwins</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DocumentDB</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DocumentDB</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DomainRegistration</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.DomainRegistration</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.EnterpriseKnowledgeGraph</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.EnterpriseKnowledgeGraph</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.EventGrid</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.EventGrid</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.EventHub</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.EventHub</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Experimentation</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Experimentation</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Falcon</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Falcon</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Features</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Features</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.GuestConfiguration</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.GuestConfiguration</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HDInsight</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.HDInsight</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HanaOnAzure</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.HanaOnAzure</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HardwareSecurityModules</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.HardwareSecurityModules</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HealthcareApis</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.HealthcareApis</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HybridCompute</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.HybridCompute</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HybridData</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.HybridData</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Hydra</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Hydra</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ImportExport</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ImportExport</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Insights</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Insights</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.IoTCentral</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.IoTCentral</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.IoTSpaces</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.IoTSpaces</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.KeyVault</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.KeyVault</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Keyvault</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Keyvault</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Kubernetes</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Kubernetes</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Kusto</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Kusto</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.LabServices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.LabServices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Logic</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Logic</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MachineLearning</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.MachineLearning</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MachineLearningServices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.MachineLearningServices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Maintenance</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Maintenance</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ManagedIdentity</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ManagedIdentity</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ManagedServices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ManagedServices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Management</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Management</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Maps</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Maps</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Marketplace</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Marketplace</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MarketplaceApps</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.MarketplaceApps</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MarketplaceOrdering</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.MarketplaceOrdering</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Media</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Media</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Migrate</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Migrate</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MixedReality</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.MixedReality</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.NetApp</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.NetApp</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.NotificationHubs</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.NotificationHubs</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ObjectStore</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ObjectStore</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.OffAzure</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.OffAzure</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.OperationalInsights</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.OperationalInsights</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.OperationsManagement</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.OperationsManagement</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Peering</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Peering</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.PolicyInsights</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.PolicyInsights</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Portal</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Portal</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.PowerBI</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.PowerBI</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.PowerBIDedicated</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.PowerBIDedicated</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ProjectBabylon</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ProjectBabylon</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ProviderHub</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ProviderHub</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Quantum</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Quantum</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.RecoveryServices</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.RecoveryServices</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.RedHatOpenShift</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.RedHatOpenShift</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Relay</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Relay</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ResourceGraph</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ResourceGraph</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ResourceHealth</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ResourceHealth</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Resources</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Resources</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SaaS</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SaaS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Scheduler</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Scheduler</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Search</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Search</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Security</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Security</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SecurityInsights</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SecurityInsights</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SerialConsole</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SerialConsole</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ServiceBus</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ServiceBus</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ServiceFabric</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ServiceFabric</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ServiceFabricMesh</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ServiceFabricMesh</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Services</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Services</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SignalRService</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SignalRService</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SignalRservice</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SignalRservice</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SoftwarePlan</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SoftwarePlan</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Solutions</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Solutions</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Sql</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Sql</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SqlVirtualMachine</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.SqlVirtualMachine</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StorSimple</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.StorSimple</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Storage</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Storage</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StorageCache</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.StorageCache</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StorageSync</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.StorageSync</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StreamAnalytics</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.StreamAnalytics</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Subscription</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Subscription</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Synapse</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Synapse</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.TimeSeriesInsights</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.TimeSeriesInsights</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Token</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Token</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VMwareCloudSimple</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.VMwareCloudSimple</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VSOnline</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.VSOnline</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VirtualMachineImages</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.VirtualMachineImages</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VisualStudio</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.VisualStudio</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VnfManager</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.VnfManager</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Web</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.Web</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.WindowsESU</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.WindowsESU</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.WindowsIoT</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.WindowsIoT</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.WorkloadMonitor</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.WorkloadMonitor</sub>|<sub>HOLD</sub>|

### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Path</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>Microsoft.ClassicCompute</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ClassicCompute</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicInfrastructureMigrate</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ClassicInfrastructureMigrate</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicNetwork</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ClassicNetwork</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicStorage</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ClassicStorage</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicSubscription</sub>|<sub>UNKNOWN</sub>|<sub>Microsoft.ClassicSubscription</sub>|<sub>REJECT</sub>|
