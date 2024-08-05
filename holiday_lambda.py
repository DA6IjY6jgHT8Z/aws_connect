import json
import logging
import boto3

import datetime
import dateutil.tz
     
logger = logging.getLogger()
logger.setLevel("INFO")

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('holidays')

    
def read_table_column(date, column):
    response_col = "None"
    try:
        response = table.get_item(
            Key={
                'date':date
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
    
    eastern = dateutil.tz.gettz('US/Eastern')
    dt_us_eastern = datetime.datetime.now(tz=eastern)
    logger.info (dt_us_eastern)
    str_date = dt_us_eastern.strftime("%Y-%m-%d")

    logger.info("The attributes of now() are : ")

    logger.info(str_date)

    str_date = "2024-12-25"
    response = read_table_column(str_date, "description")

    return {
        "holiday": response
    }

