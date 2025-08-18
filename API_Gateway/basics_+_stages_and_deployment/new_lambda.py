import json
import os

def lambda_handler(event, context):
    # Extract metadata from Lambda context
    function_name = context.function_name
    function_version = context.function_version
    
    # Extract API Gateway information from event
    domain_name = event.get('requestContext', {}).get('domainName', 'api.example.com')
    stage = event.get('requestContext', {}).get('stage', 'v1')
    resource_path = event.get('requestContext', {}).get('resourcePath', '/basic-calc')
    
    # Get alias from environment variable (you can set this in Lambda configuration)
    alias = stage.upper()
    
    # Dynamically construct the body message
    api_endpoint = f"{domain_name}/{stage}{resource_path}"
    body = f"This is {function_name} lambda called from API {api_endpoint} ... version: {function_version} with {alias} Alias!"
    
    statusCode = 200
    return {
        'statusCode': statusCode,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json'
        }
    }