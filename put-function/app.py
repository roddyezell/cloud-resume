import json
import boto3

def lambda_handler(event, context):

    client = boto3.resource('dynamodb')
    table = client.Table('cloud-resume-table')

    response = table.get_item(Key = {"ID" : "1"})
    if "Item" in response:
            visit_count = response["Item"]["count"]
    
    count = int(visit_count) + 1
    visit_count = str(count)
    
    table.put_item(Item={"ID" : "1", "count" : visit_count})

    return {
        
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
         },
        'body': json.dumps({"count" : visit_count}),
        'statusCode': 200
    }