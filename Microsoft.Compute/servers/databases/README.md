
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
|[VulnerabilityAssessment](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/VulnerabilityAssessment/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/VulnerabilityAssessment|TRIAL|
|[VulnerabilityAssessmentScans](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/VulnerabilityAssessmentScans/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/VulnerabilityAssessmentScans|TRIAL|
|[VulnerabilityAssessmentSettings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/VulnerabilityAssessmentSettings/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/VulnerabilityAssessmentSettings|TRIAL|
|[advisors](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/advisors/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/advisors|TRIAL|
|[auditRecords](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/auditRecords/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/auditRecords|TRIAL|
|[auditingPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/auditingPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/auditingPolicies|TRIAL|
|[auditingSettings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/auditingSettings/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/auditingSettings|TRIAL|
|[automaticTuning](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/automaticTuning/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/automaticTuning|TRIAL|
|[backupLongTermRetentionPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/backupLongTermRetentionPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/backupLongTermRetentionPolicies|TRIAL|
|[backupShortTermRetentionPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/backupShortTermRetentionPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/backupShortTermRetentionPolicies|TRIAL|
|[connectionPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/connectionPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/connectionPolicies|TRIAL|
|[dataMaskingPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/dataMaskingPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/dataMaskingPolicies|TRIAL|
|[extendedAuditingSettings](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/extendedAuditingSettings/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/extendedAuditingSettings|TRIAL|
|[extensions](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/extensions/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/extensions|TRIAL|
|[geoBackupPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/geoBackupPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/geoBackupPolicies|TRIAL|
|[metricDefinitions](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/metricDefinitions/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/metricDefinitions|TRIAL|
|[metrics](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/metrics/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/metrics|TRIAL|
|[recommendedSensitivityLabels](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/recommendedSensitivityLabels/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/recommendedSensitivityLabels|TRIAL|
|[schemas](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/schemas/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/schemas|TRIAL|
|[securityAlertPolicies](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/securityAlertPolicies/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/securityAlertPolicies|TRIAL|
|[syncGroups](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/syncGroups/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/syncGroups|TRIAL|
|[topQueries](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/topQueries/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/topQueries|TRIAL|
|[transparentDataEncryption](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/transparentDataEncryption/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/transparentDataEncryption|TRIAL|
|[vulnerabilityAssessments](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/vulnerabilityAssessments/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/vulnerabilityAssessments|TRIAL|
|[workloadGroups](https://github.com/openrba/python-azure-techradar/blob/master/Microsoft.Compute/servers/databases/workloadGroups/README.md)|UNKNOWN|Microsoft.Compute/servers/databases/workloadGroups|TRIAL|

### Hold


Technologies not recommended to be used for new projects. Technologies that we think are not (yet) worth to (further) invest in.  HOLD technologies should not be used for new projects, but usually can be continued for existing projects.  These technologies may include services that have yet to be evaluated by architecture and security due to a lack of interest, time, or need.  
  
***<font color="red"> There are currently no resources at this ring level. </font>***