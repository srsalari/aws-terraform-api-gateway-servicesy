import json
import boto3

# Make sure to choose the correct region if your upload bucket is in a different region
s3 = boto3.client('s3', region_name='ca-central-1')

def lambda_handler(event, context):
    bucket_name = "saeed-app-data-storage-2025"  # This is the upload bucket
    file_key = "sample.txt"  # You may generate this dynamically

    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': file_key},
        ExpiresIn=3600
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"upload_url": presigned_url})
    }
