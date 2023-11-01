---
description: >-
  For organizations aiming to be threat-informed defenders, SLAM offers a
  robust, real-time, and fully managed platform for security detection and
  response within AWS.
---

# Project SLAM

***

## SLAM WebApp Platform

### Overview

SLAM (Security.Logging.Alert.Monitoring) is an enterprise-ready, API-first, event-driven SaaS platform designed for cloud-native security detection and incident response in AWS environments. It offers a comprehensive suite of features, including Log Runner for real-time log ingestion and transformation, and integrates with AWS OpenSearch Security Analytics and Jupyter Notebooks via SageMaker for advanced threat detection and automated response.

***

### Core Features

#### Log Runner

* **Real-time Log Ingestion**: Ingest logs from AWS and SaaS applications into AWS Security Lake.
* **Schema Mapping**: Uses Vector Remap running in AWS Step Functions to transform raw logs into ECS (Elastic Common Schema) format.
* **Serverless & Event-Driven**: Built on AWS Lambda and Step Functions for scalability and real-time processing.

#### AWS OpenSearch Security Analytics

* **Advanced Threat Detection**: Utilizes Sigma as the detection engine.
* **Integrated with Security Lake**: Seamless data flow from Security Lake to OpenSearch for real-time analytics.

#### Jupyter Notebooks via SageMaker

* **Automated Response**: Run custom analytics and automated response algorithms.
* **Event-Triggered**: Notebooks can be triggered by security events for real-time response.
* **Collaboration and Version Control**: Built-in capabilities for team collaboration and versioning.

***

### Benefits

* **Fully Managed**: All components are AWS-native, offering a fully managed, scalable solution.
* **API-First**: Easy integration with existing systems and enables automation.
* **Real-Time**: Event-driven architecture allows for real-time threat detection and response.
* **Extensible**: Easily add new data sources, analytics algorithms, or response actions.

***

### Use Cases

* **Threat Detection**: Real-time monitoring and alerting of security threats.
* **Incident Response**: Automated workflows for responding to security incidents.
* **Compliance Monitoring**: Ensure real-time compliance with security policies.
* **Advanced Analytics**: Use Jupyter Notebooks for deep dives into security data.

***

### Future Enhancements

* **AWS Security Lake & OpenSearch Deployment**: Configure and deploy directly from the SLAM UI.
* **Detection as Code**: CI/CD pipelines for detection algorithms via GitHub and GitHub Actions.

***

### Log Sources

#### Tier 1: AWS Environment

* **AWS CloudTrail logs**: Auditing and reviewing API calls.
* **AWS GuardDuty findings**: Threat intelligence.
* **AWS S3 access logs**: S3 bucket access monitoring.
* **AWS WAF logs**: Web request inspection.
* **AWS CloudWatch logs**: Operational and performance data.

#### Tier 1: SaaS Applications

* **Okta logs**: Identity-related events.
* **GitHub audit logs**: Repository changes and access.
* **Postman App Logs**: Postman usage and behavior.
* **Postman Cloudflare Logs**: Web traffic and security threats.

***

### Getting Started

#### AWS Security Lake Setup

* Instructions on setting up AWS Security Lake, including data ingestion from AWS Guard Duty, Security Hub, and other log sources.

#### AWS Glue and Brex Substation Setup

* Instructions on setting up AWS Glue for AWS and third-party logs, and Brex Substation for Postman logs.

***

### Deployment

* Instructions on deploying the project on a live system using AWS CloudFormation for IaC and AWS CodePipeline for CI/CD.

***

### Contributing

* Guidelines for submitting pull requests and issues.

***

### License

* License details.

***

### Contact

* Your Contact Information

***

