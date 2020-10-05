
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

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Type</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>[Microsoft.ADHybridHealthService](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.ADHybridHealthService)</sub>|<sub>Azure Active Directory (Azure AD) is a multi-tenant, cloud-based identity and access management service.</sub>|<sub>SAAS</sub>|<sub>ADOPT</sub>|

### Trial


Technologies that we have seen work with success in projects to solve real problems;  first serious usage experience that confirm benefits and uncover limitations.  TRIAL technologies are slightly more risky; some engineers in our organization walked this path and will share knowledge and experiences.  This area can contain services that have been architecture and security reviewed but do not contain automated policy managmeent.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Type</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>[Microsoft.Compute](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Compute)</sub>|<sub>Azure compute provides the infrastructure you need to run your apps.</sub>|<sub>IAAS</sub>|<sub>TRIAL</sub>|
|<sub>[Microsoft.DBforPostgreSQL](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DBforPostgreSQL)</sub>|<sub>Azure Database for PostgreSQL is a relational database service based on the open-source Postgres database engine.</sub>|<sub>PAAS</sub>|<sub>TRIAL</sub>|
|<sub>[Microsoft.Network](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Network)</sub>|<sub>Azure Virtual Network (VNet) is the fundamental building block for your private network in Azure.</sub>|<sub>IAAS</sub>|<sub>TRIAL</sub>|

### Assess


Technologies that are promising and have clear potential value-add for us; technologies worth investing some research and prototyping efforts to see if it has impact.  ASSESS technologies have higher risks;  they are often new to our organization and highly unproven within RBA.  You will find some engineers that have knowledge in the technology and promote it, you may even find teams that have started a prototyping effort.  These technologies can also include services that are currently in architecture or security review.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Type</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>[Microsoft.Advisor](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Advisor)</sub>|<sub>Azure Advisor scans your Azure configuration and recommends changes to optimize deployments, increase security, and save you money.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.AlertsManagement](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AlertsManagement)</sub>|<sub>Monitoring Azure and on-premises services. Aggregate and analyze metrics, logs, and traces. Fire alerts and send notifications or call automated solutions.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.ApiManagement](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.ApiManagement)</sub>|<sub>Learn how to use API Management to publish APIs to external, partner, and employee developers securely and at scale. Shows you how to create and manage modern API gateways for existing back-end services hosted anywhere.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.AppConfiguration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AppConfiguration)</sub>|<sub>Azure App Configuration provides a service to centrally manage application settings and feature flags.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.AppPlatform](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.AppPlatform)</sub>|<sub>Azure Spring Cloud makes it easy to deploy Spring Boot-based microservice applications to Azure with zero code changes.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Batch](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Batch)</sub>|<sub>Azure Batch runs large-scale applications efficiently in the cloud. Schedule compute-intensive tasks and dynamically adjust resources for your solution without managing infrastructure.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Billing](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Billing)</sub>|<sub>Azure Cost Management and Billing help you understand Azure billing, manage your account and subscriptions, monitor and control Azure spending and optimize resource use.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.BingMaps](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.BingMaps)</sub>|<sub>The Bing Maps Platform offers a suite of controls and service APIs that you can use to add Bing Maps or geospatial services to your application.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Blueprint](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Blueprint)</sub>|<sub>Blueprints are a declarative way to orchestrate the deployment of various resource templates and other artifacts.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Cache](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Cache)</sub>|<sub>Azure Cache for Redis provides an in-memory data store based on the open-source software Redis.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Cdn](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Cdn)</sub>|<sub>Secure and reliable global content delivery and acceleration</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.CertificateRegistration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.CertificateRegistration)</sub>|<sub>Azure App Service customers can now purchase, configure, and manage SSL certificates right from the Azure portal</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Consumption](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Consumption)</sub>|<sub>Azure Cost Management and Billing help you understand Azure billing, manage your account and subscriptions, monitor and control Azure spending and optimize resource use. Learn how to analyze costs, create and manage budgets, export data, and review and act on recommendations.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.ContainerInstance](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.ContainerInstance)</sub>|<sub>Run Docker containers on-demand in a managed, serverless Azure environment. Azure Container Instances is a solution for any scenario that can operate in isolated containers, without orchestration.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.ContainerRegistry](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.ContainerRegistry)</sub>|<sub>Azure Container Registry allows you to build, store, and manage container images and artifacts in a private registry for all types of container deployments.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.ContainerService](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.ContainerService)</sub>|<sub>Azure Kubernetes Service (AKS) makes it simple to deploy a managed Kubernetes cluster in Azure. AKS reduces the complexity and operational overhead of managing Kubernetes by offloading much of that responsibility to Azure.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.CostManagement](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.CostManagement)</sub>|<sub>Azure Cost Management and Billing help you understand Azure billing, manage your account and subscriptions, monitor and control Azure spending and optimize resource use. Learn how to analyze costs, create and manage budgets, export data, and review and act on recommendations.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.CostManagementExports](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.CostManagementExports)</sub>|<sub>Azure Cost Management and Billing help you understand Azure billing, manage your account and subscriptions, monitor and control Azure spending and optimize resource use. Learn how to analyze costs, create and manage budgets, export data, and review and act on recommendations.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DBforMariaDB](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DBforMariaDB)</sub>|<sub>Azure Database for MariaDB provides fully managed, enterprise-ready community MariaDB database as a service.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DBforMySQL](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DBforMySQL)</sub>|<sub>Azure Database for MySQL provides fully managed, enterprise-ready community MySQL database as a service.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataBox](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataBox)</sub>|<sub>The Azure Data Box family offers products of differing storage capacities to help send terabytes (TB) of data to Azure in a quick, inexpensive, reliable way. Microsoft accelerates secure data transfer by shipping you proprietary storage devices that enable offline or over the network data transfer.</sub>|<sub>IAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataBricks](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataBricks)</sub>|<sub>an Apache Spark-based analytics platform with one-click setup, streamlined workflows, and an interactive workspace for collaboration between data scientists, engineers, and business analysts.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataCatalog](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataCatalog)</sub>|<sub>Azure Data Catalog is a fully managed cloud service. It lets users discover the data sources they need and understand the data sources they find.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataFactory](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataFactory)</sub>|<sub>Azure Data Factory is Azure's cloud ETL service for scale-out serverless data integration and data transformation. It offers a code-free UI for intuitive authoring and single-pane-of-glass monitoring and management.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataLakeAnalytics](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataLakeAnalytics)</sub>|<sub>Azure Data Lake Analytics allows you to run big data analysis jobs that scale to massive data sets.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataLakeStore](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataLakeStore)</sub>|<sub>Azure Data Lake Storage Gen2 is a set of capabilities dedicated to big data analytics, built on Azure Blob storage.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DataMigration](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DataMigration)</sub>|<sub>Azure Database Migration Service enables seamless migrations from multiple database sources to Azure Data platforms with minimal downtime.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Databricks](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Databricks)</sub>|<sub>Apache Spark-based analytics platform with one-click setup, streamlined workflows, and an interactive workspace for collaboration between data scientists, engineers, and business analysts.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DesktopVirtualization](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DesktopVirtualization)</sub>|<sub>Deliver a virtual desktop experience and remote apps to any device. Bring together Microsoft 365 and Azure to provide users with the only multi-session Windows 10 experience</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DevSpaces](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DevSpaces)</sub>|<sub>Azure Dev Spaces is an extension to AKS that allows you to easily run and debug your code in the context of a larger application.</sub>|<sub>SAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Devices](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Devices)</sub>|<sub>IoT Hub is a managed service, hosted in the cloud, that acts as a central message hub for bi-directional communication between your IoT application and the devices it manages.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.DocumentDB](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.DocumentDB)</sub>|<sub>Azure Cosmos DB is Microsoftâ€™s globally distributed, multi-model database service for operational and analytics workloads.</sub>|<sub>PAAS</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.Insights](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.Insights)</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>ASSESS</sub>|
|<sub>[Microsoft.ServiceBus](https://github.com/openrba/python-azure-techradar/tree/master/Microsoft.ServiceBus)</sub>|<sub>Reliable cloud messaging as a service (MaaS) and simple hybrid integration</sub>|<sub>MAAS</sub>|<sub>ASSESS</sub>|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Type</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>Microsoft.AAD</sub>|<sub>Azure Active Directory Domain Services (Azure AD DS) provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos / NTLM authentication that is fully compatible with Windows Server Active Directory.</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Addons</sub>|<sub>Add additonal support plans from other providers to your Azure resources.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AnalysisServices</sub>|<sub>Learn how to set up data modeling with Analysis Services in the cloud. Documentation shows you how to create an enterprise BI solution by using tabular data models.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Attestation</sub>|<sub>Azure Attestation Service</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AzureActiveDirectory</sub>|<sub>Azure Active Directory B2C (Azure AD B2C) is an identity management service that enables custom control of how your customers sign up, sign in, and manage their profiles when using your iOS, Android, .NET, single-page (SPA), and other applications.</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AzureData</sub>|<sub>We don't use the Azure Portal often so we need notification function when available for ESU patches.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.AzureStack</sub>|<sub>Azure Stack is a hybrid cloud computing software solution developed by Microsoft based on the company's Azure cloud platform.</sub>|<sub>IAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Blockchain</sub>|<sub>Azure Blockchain Workbench Preview is a collection of Azure services and capabilities designed to help you create and deploy blockchain applications to share business processes and data with other organizations.</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.BlockchainTokens</sub>|<sub>Azure Blockchain Tokens makes deploying and managing standard tokens easier than ever.</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.BotService</sub>|<sub>Develop intelligent, enterprise-grade bots that let you maintain control of your data. Build any type of bot</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Capacity</sub>|<sub>Reserve capacity on Azure regions.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CognitiveServices</sub>|<sub>Learn how to build intelligent and supported algorithms into apps, websites, and bots to see, hear, speak, understand, and interpret your user needs.</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Commerce</sub>|<sub>Elevate your brand with Dynamics 365 Commerce. Deliver personalized, seamless shopping experiences across physical and digital channels</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CustomProviders</sub>|<sub>Azure Custom Resource Providers is an extensibility platform to Azure. It allows you to define custom APIs that can be used to enrich the default Azure experience.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.CustomerLockbox</sub>|<sub>Customer Lockbox for Microsoft Azure provides an interface for customers to review and approve or reject customer data access requests.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataBoxEdge</sub>|<sub>Azure Stack Edge is an AI-enabled edge computing device with network data transfer capabilities.</sub>|<sub>IAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DataShare</sub>|<sub>Azure Data Share is a safe and secure service for sharing data with third-party organizations.</sub>|<sub>PAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DigitalTwins</sub>|<sub>Azure Digital Twins Preview is an Azure IoT service that creates comprehensive models of the physical environment.</sub>|<sub>IAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.DomainRegistration</sub>|<sub>Register domain names through Microsoft Azure.</sub>|<sub>SAAS</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.EnterpriseKnowledgeGraph</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.EventGrid</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.EventHub</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Experimentation</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Falcon</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Features</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.GuestConfiguration</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HDInsight</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HanaOnAzure</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HardwareSecurityModules</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HealthcareApis</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HybridCompute</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.HybridData</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Hydra</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ImportExport</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.IoTCentral</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.IoTSpaces</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.KeyVault</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Keyvault</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Kubernetes</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Kusto</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.LabServices</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Logic</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MachineLearning</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MachineLearningServices</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Maintenance</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ManagedIdentity</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ManagedServices</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Management</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Maps</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Marketplace</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MarketplaceApps</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MarketplaceOrdering</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Media</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Migrate</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.MixedReality</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.NetApp</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.NotificationHubs</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ObjectStore</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.OffAzure</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.OperationalInsights</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.OperationsManagement</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Peering</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.PolicyInsights</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Portal</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.PowerBI</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.PowerBIDedicated</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ProjectBabylon</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ProviderHub</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Quantum</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.RecoveryServices</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.RedHatOpenShift</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Relay</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ResourceGraph</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ResourceHealth</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Resources</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SaaS</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Scheduler</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Search</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Security</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SecurityInsights</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SerialConsole</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ServiceFabric</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.ServiceFabricMesh</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Services</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SignalRService</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SignalRservice</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SoftwarePlan</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Solutions</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Sql</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.SqlVirtualMachine</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StorSimple</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Storage</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StorageCache</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StorageSync</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.StreamAnalytics</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Subscription</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Synapse</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.TimeSeriesInsights</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Token</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VMwareCloudSimple</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VSOnline</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VirtualMachineImages</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VisualStudio</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.VnfManager</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.Web</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.WindowsESU</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.WindowsIoT</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|
|<sub>Microsoft.WorkloadMonitor</sub>|<sub>UNKNOWN</sub>|<sub>UNKNOWN</sub>|<sub>HOLD</sub>|

### Reject


Technologies not recommended to be used for any projects. Technologies that have undergone architecture and security review but do not meet company standards for use.  REJECT technologies should never be used on any project and should be considered deprecated for existing projects.  

|<sub>Resource</sub>|<sub>Description</sub>|<sub>Type</sub>|<sub>Status</sub>|
| :---: | :---: | :---: | :---: |
|<sub>Microsoft.Authorization</sub>|<sub>Azure Resource Manager is the deployment and management service for Azure.</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.Automation</sub>|<sub>Azure Automation delivers a cloud-based automation and configuration service that provides consistent management across your Azure and non-Azure environments.</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.BatchAI</sub>|<sub>Azure Batch AI is designed to help you run large AI training and testing workloads in the cloud. Batch AI supports multiple training toolkits such as Tensorflow, CNTK, Chainer, among others, as well as the ability to deploy your own software stacks at scale.</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.CDN</sub>|<sub>Secure and reliable global content delivery and acceleration</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicCompute</sub>|<sub>Deprecated version of Azure compute</sub>|<sub>IAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicInfrastructureMigrate</sub>|<sub>Deprecated version of Azure migrate</sub>|<sub>IAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicNetwork</sub>|<sub>Deprecated version of Azure network</sub>|<sub>IAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicStorage</sub>|<sub>Deprecated version of Azure storage</sub>|<sub>IAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.ClassicSubscription</sub>|<sub>Deprecated version of Azure subscription</sub>|<sub>IAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.DeploymentManager</sub>|<sub>Deployment Manager is a feature of Resource Manager. It expands your capabilities during deployment.</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.DevOps</sub>|<sub>Collaborate on software development through source control, work tracking, and continuous integration and delivery, both on-premises and in the cloud!</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
|<sub>Microsoft.DevTestLab</sub>|<sub>Azure DevTest Labs enables developers on teams to efficiently self-manage virtual machines (VMs) and PaaS resources without waiting for approvals.</sub>|<sub>PAAS</sub>|<sub>REJECT</sub>|
