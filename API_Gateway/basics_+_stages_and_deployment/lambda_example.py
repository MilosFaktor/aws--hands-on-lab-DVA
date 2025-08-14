import json

def lambda_handler(event, context):
    body = "Hello from converter lambda LATEST and DEV Alias!"
    statusCode = 200
    return {
        'statusCode': statusCode,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
