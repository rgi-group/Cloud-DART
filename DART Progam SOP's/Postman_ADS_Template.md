# Alerting and Detection Strategy (ADS) Template
## Goal
The goal is the intended purpose of the alert. It is a simple, plaintext description of the type of behavior you're attempting to detect in your ADS.
## Categorization
The categorization is a mapping of the ADS to the relevant entry in the MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) Framework. ATT&CK provides a language for various post-exploitation techniques and strategies that adversaries might use.
## Strategy Abstract
The strategy abstract is a high-level walkthrough of how the ADS functions. This describes what the alert is looking for, what technical data sources are used, any enrichment that occurs, and any false positive minimization steps.
## Technical Context
Technical Context provides detailed information and background needed for a responder to understand all components of the alert.
## Blind Spots and Assumptions
Blind Spots and Assumptions are the recognized issues, assumptions, and areas where an ADS may not fire.
## False Positives
False Positives are the known instances of an ADS misfiring due to a misconfiguration, idiosyncrasy in the environment, or other non-malicious scenario.
## Validation
Validation are the steps required to generate a representative true positive event which triggers this alert.
## Priority
Priority describes the various alerting levels that an ADS may be tagged with.
## Response
These are the general response steps in the event that this alert fired.
## Additional Resources
Additional Resources are any other internal, external, or technical references that may be useful for understanding the ADS.