import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('support-ticket-system')
sqs = boto3.client('sqs')
sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
        name = body.get('name', 'Unknown')
        email = body.get('email', 'Unknown')
        issue = body.get('issue', 'No issue')
        
        ticketId = 'TICKET-' + str(uuid.uuid4())[:8].upper()
        
        # Save to DynamoDB
        table.put_item(Item={
            'ticketId': ticketId,
            'name': name,
            'email': email,
            'issue': issue,
            'status': 'OPEN',
            'createdAt': datetime.now().isoformat()
        })
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS,GET'
            },
            'body': json.dumps({'ticketId': ticketId, 'message': 'Ticket created successfully', 'status': 'OPEN'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS,GET'
            },
            'body': json.dumps({'error': str(e)})
        }
