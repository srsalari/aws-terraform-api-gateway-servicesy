import json
import boto3

# Specify the correct region for your bucket
s3 = boto3.client('s3', region_name='ca-central-1')

def lambda_handler(event, context):
    bucket_name = "my-app-data-storage"  # Ensure this bucket is in ap-east-1
    file_key = "sample.txt"              # You may generate this dynamically

    # Generate a pre-signed URL valid for 1 hour to PUT (upload) an object
    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': file_key},
        ExpiresIn=3600
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"upload_url": presigned_url})
    }
