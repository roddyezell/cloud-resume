import json
import boto3

def lambda_handler(event, context):

    client = boto3.resource('dynamodb')
    table = client.Table('cloud-resume-table')

    data = table.get_item(Key = {"ID" : "1"})
    
    visit_count = data["Item"]["count"]
    
    response = {
        
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
         },
        'body': json.dumps({"count" : visit_count}),
        'statusCode': 200
    }
    
    return response