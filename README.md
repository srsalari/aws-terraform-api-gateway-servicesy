# AWS Terraform Project

This project provisions an AWS infrastructure using Terraform, which includes:

- **Lambda Functions**

  - `ProcessDynamoDB`: Processes DynamoDB records.
  - `ProcessS3`: Generates pre-signed URLs to allow file uploads to an S3 bucket.
  - `StartGlueJob`: Triggers an AWS Glue Job.

- **API Gateway Endpoints**

  - `/records`: A POST endpoint to work with DynamoDB (via a Lambda proxy).
  - `/glue`: A POST endpoint to trigger a Glue job (via a Lambda proxy).
  - `/s3`:
    - A GET endpoint that lists objects in a private S3 bucket using an AWS Service integration.
    - A POST endpoint that invokes the `ProcessS3` Lambda to generate pre-signed URLs for uploads.

- **Other Resources**
  - An S3 bucket for data storage.
  - A DynamoDB table for records.
  - An AWS Glue Job.
  - Necessary IAM Roles, Policies, and Bucket Policies for secure access.

## Pre-requisites

- AWS CLI configured with valid credentials.
- Terraform installed.
- An AWS account.
- (Optional) Postman or cURL installed for testing the API endpoints.

## Project Structure

- `main.tf`: Terraform configuration that provisions the entire stack.
- `process_s3.py`: Lambda code to generate pre-signed URLs for S3 file uploads.
- Other Lambda source code files (e.g., `process_dynamodb.zip`, `start_glue.zip`) must be built and available in the project directory.

## How to Deploy

1. **Initialize Terraform**

   In the root of your project directory, run:

   ```bash
   terraform init
   ```

2. **Plan the Deployment**

   To preview the changes:

   ```bash
   terraform plan
   ```

3. **Apply the Configuration**

   Deploy the resources by running:

   ```bash
   terraform apply
   ```

   Confirm when prompted. This will provision your AWS resources.

## API Endpoints

The deployment creates an API Gateway listed with the following endpoints (assuming the deployment outputs):

- **Base URL:**  
  The base URL is available via the output `api_url`. For example:

  ```
  https://<api-id>.execute-api.ca-central-1.amazonaws.com/prod
  ```

- **/records:**  
  POST method that integrates with the ProcessDynamoDB Lambda.

- **/glue:**  
  POST method that integrates with the StartGlueJob Lambda.

- **/s3:**  
  GET method (to list objects in the S3 bucket)  
  POST method (invokes `ProcessS3` to generate a pre-signed URL)

  A dedicated output `s3_api_url` is provided:

  ```
  ${api_url}/s3
  ```

## Testing the Endpoints

### List S3 Bucket Contents (GET `/s3`)

Use cURL:

```bash
curl -X GET "$(terraform output -raw s3_api_url)"
```

This returns the S3 bucket listing in XML format.

### Generate a Pre-signed URL for S3 Upload (POST `/s3`)

1. **Invoke the API to Get a Pre-signed URL:**

   Using Postman or cURL:

   ```bash
   curl -X POST "https://<api-id>.execute-api.ca-central-1.amazonaws.com/prod/s3" \
        -H "Content-Type: application/json" \
        -d '{}'
   ```

   The response body will contain a JSON string with a field `upload_url`.

2. **Upload a File Using the Pre-signed URL:**

   Copy the URL from the response and then use it to perform a file upload:

   ```bash
   curl -X PUT --upload-file "local_file.txt" "https://example-presigned-url.amazonaws.com/..."
   ```

   Replace the URL with the one obtained from the first call.

### Other Testing Notes

- **DynamoDB and Glue Endpoints:**  
  You may test the `/records` and `/glue` endpoints similarly using cURL or Postman.  
  For example:
  ```bash
  curl -X POST "https://<api-id>.execute-api.ca-central-1.amazonaws.com/prod/glue" \
       -H "Content-Type: application/json" \
       -d '{"job_name":"HelloWorldJob"}'
  ```

## Troubleshooting

- **Region Mismatch:** Ensure that your S3 client in `process_s3.py` is set to the region where your bucket is created.
- **Deployment Updates:** To force redeployments when resource configurations change, the Terraform deployment resource uses `triggers`.

## Cleanup

After testing, you can remove the stack by running:

```bash
terraform destroy
```

This README provides an overview of the resources and instructions to deploy, test, and manage your AWS-based solution using Terraform.
