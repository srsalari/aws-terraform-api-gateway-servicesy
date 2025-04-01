import json
import boto3

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
glue = boto3.client('glue')

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Lambda function executed successfully")
    }

# Lambda Function for Processing DynamoDB
def process_dynamodb(event, context):
    table = dynamodb.Table('RecordsTable')
    
    for record in event['Records']:
        table.put_item(Item={
            'id': record['eventID'],
            'data': record['body']
        })
    
    return {"statusCode": 200, "body": json.dumps("Data inserted into DynamoDB")}

# Lambda Function for Processing S3
def process_s3(event, context):
    bucket_name = "my-app-data-storage"
    file_key = "sample.txt"
    
    response = s3.put_object(Bucket=bucket_name, Key=file_key, Body="Sample Data")
    
    return {"statusCode": 200, "body": json.dumps("File uploaded to S3")}

# Lambda Function to Start AWS Glue Job
def start_glue(event, context):
    response = glue.start_job_run(JobName='HelloWorldJob')
    return {"statusCode": 200, "body": json.dumps(f"Glue job started: {response['JobRunId']}")}
