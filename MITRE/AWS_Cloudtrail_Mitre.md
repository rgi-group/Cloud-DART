---
description: >-
  An overview of CloudTrail events that are interesting from an Incident
  Response perspective
cover: >-
  https://images.unsplash.com/photo-1579567761406-4684ee0c75b6?crop=entropy&cs=srgb&fm=jpg&ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwxfHxjeWJlcnxlbnwwfHx8fDE2OTg2NzU4Njh8MA&ixlib=rb-4.0.3&q=85
coverY: 0
---

# AWS Cloudtrail Event Field to MITRE Mappings

| Initial Access                    | Execution                | Persistence       | Privilege Escalation | Defense Evasion           |
| --------------------------------- | ------------------------ | ----------------- | -------------------- | ------------------------- |
| ConsoleLogin                      | StartInstance            | CreateAccessKey   | CreateGroup          | StopLogging               |
| PasswordRecoveryRequested         | StartInstances           | CreateUser        | CreateRole           | DeleteTrail               |
| Invoke                            | CreateNetworkAclEntry    | UpdateAccessKey   | UpdateTrail          | RequestCertificate        |
| SendCommand                       | CreateRoute              | PutGroupPolicy    | PutEventSelectors    | UpdateAssumeRolePolicy    |
| CreateLoginProfile                | PutRolePolicy            | DeleteFlowLogs    | ListServiceQuotas    | DeleteDetector            |
| AuthorizeSecurityGroupEgress      | PutUserPolicy            | DeleteMembers     | ListInstanceProfiles | ModifyDBSnapshotAttribute |
| AuthorizeSecurityGroupIngress     | AddRoleToInstanceProfile | DeleteSnapshot    | ListGroups           | PutBucketPolicy           |
| CreateVirtualMFADevice            | AddUserToGroup           | LeaveOrganization | ListBuckets          | PutBucketAcl              |
| CreateConnection                  | DeactivateMFADevice      |                   |                      |                           |
| ApplySecurityGroupsToLoadBalancer |                          |                   |                      |                           |
| SetSecurityGroups                 |                          |                   |                      |                           |
| AuthorizeDBSecurityGroupIngress   |                          |                   |                      |                           |
| CreateDBSecurityGroup             |                          |                   |                      |                           |
| ChangePassword                    |                          |                   |                      |                           |
| DisassociateFromMasterAccount     |                          |                   |                      |                           |
| DisassociateMembers               |                          |                   |                      |                           |
| StopMonitoringMembers             |                          |                   |                      |                           |
