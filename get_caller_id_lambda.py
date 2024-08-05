import json
import logging
import boto3
     
logger = logging.getLogger()
logger.setLevel("INFO")

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('caller_id')

    
def read_table_column(key, column):
    response_col = "None"
    try:
        response = table.get_item(
            Key={
                'caller_phone':key
            }
        )
        logger.info(response)
        response_col = response["Item"][column]
    except Exception as e:
        logger.error("DDB Read Error")
        logger.error(e)
    return response_col

def lambda_handler(event, context):
    logger.info(json.dumps(event, indent=2))
    caller_phone = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
    response = read_table_column(caller_phone, "sales_rep")

    return {
        "sales_rep": response
    }

