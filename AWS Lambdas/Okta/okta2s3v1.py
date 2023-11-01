#!/usr/local/bin/python3
"""okta-prod-logging.py: This script is to collect Okta logs for compliance"""
__author__      = "Christopher Watkins"
__copyright__   = "Copyright 2023, Postman"
__license__ = "Apache License, Version 2.0"
__version__ = "1.0.0"
__maintainer__ = "Christopher Watkins"
__email__ = "christopher.watkins@postman.com"
__status__ = "Production"
##############################################
import json
import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Define the S3 bucket name
    bucket_name = 'postman-s3-okta-audit-logs'
    
    # Convert the event object to a string
    event_str = json.dumps(event)
    
    # Define the object key
    object_key = f"okta_logs/{context.aws_request_id}.json"
    
    # Upload the event to the S3 bucket
    s3.put_object(Body=event_str, Bucket=bucket_name, Key=object_key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully forwarded Okta logs to S3.')
    }
