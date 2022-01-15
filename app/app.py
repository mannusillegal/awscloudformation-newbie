import json


def lambda_handler(event, context):
    print("i am going to invoke")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
