# AWS Terraform Cloud Deployment Project

## Overview

This project provisions a complete AWS serverless architecture using Terraform. It deploys various AWS services including:

- **AWS Lambda Functions:** For processing DynamoDB records, handling S3 file uploads, and initiating AWS Glue jobs.
- **API Gateway:** To expose RESTful endpoints that trigger the Lambda functions.
- **DynamoDB:** As a NoSQL database for storing records.
- **S3 Buckets:** One for storing Glue scripts and other assets, and another dedicated for direct file uploads.
- **AWS Glue Job:** For ETL operations.
- **IAM Roles and Policies:** To ensure secure and controlled access between services.

## Project Structure

```
.
├── aws-terraform/
│   ├── main.tf             # Core Terraform configuration for AWS resources
│   ├── variables.tf        # Input variables for project configuration
│   ├── outputs.tf          # Outputs generated after provisioning
│   ├── readme.md           # Project documentation
│   └── modules/
│       └── functions/      # Module encapsulating Lambda functions and permissions
│           ├── main.tf
│           ├── variables.tf
│           └── outputs.tf
```

## Prerequisites

- **AWS Account:** Ensure you have an active AWS account with the necessary permissions.
- **Terraform:** Installed (version >= 0.12 recommended).
- **AWS CLI:** Configured with proper credentials.

## Setup and Deployment

1. **Navigate to the project root:**

   ```bash
   cd /Users/saeedrezasalari/Library/CloudStorage/OneDrive-Personal/Desktop/ccproject/terraform-project2/aws-terraform
   ```

2. **Initialize Terraform:**

   ```bash
   terraform init
   ```

3. **Preview the planned changes:**

   ```bash
   terraform plan
   ```

4. **Apply the configuration to provision resources:**

   ```bash
   terraform apply
   ```

## Modules Overview

The project uses a dedicated module for AWS Lambda functions located in the `modules/functions` directory. This module handles:

- Creation and deployment of Lambda functions for processing DynamoDB records, S3 interactions, and starting AWS Glue jobs.
- Configuration of Lambda permissions that allow API Gateway to invoke these Lambda functions.

## Configuration Variables

The project is highly configurable via the `variables.tf` file. Key variables include:

- **region:** AWS region for deployment (default: `ca-central-1`).
- **data_bucket_name:** Name of the S3 bucket for Glue scripts and shared storage.
- **upload_bucket_name:** Name of the S3 bucket dedicated for file uploads.
- **process_dynamodb_zip, process_s3_zip, start_glue_zip:** Filenames for Lambda function deployment packages.
- **lambda_runtime:** Runtime environment for the Lambda functions (default: `python3.8`).
- **glue_job_name:** Name for the AWS Glue job.
- **glue_script_location:** Bucket path for the Glue job script.
- **api_name:** API Gateway name.
- **api_stage:** Deployment stage for the API Gateway.

## Outputs

Post-deployment, Terraform outputs key information such as:

- The API Gateway URL (`api_url`).
- The AWS Glue job name.
- Bucket names for both general data and file uploads.
- Specific API endpoints for S3 integration.

## Troubleshooting

- **AWS Credentials:** Ensure that AWS CLI credentials are properly set up.
- **Terraform Plan:** Always run `terraform plan` to verify changes prior to applying them.
- **Logs and Monitoring:** Use AWS CloudWatch to monitor Lambda functions and diagnose any issues.

## Conclusion

This AWS Terraform project demonstrates a modular, secure, and scalable approach to cloud infrastructure provisioning. By leveraging best practices—such as centralized variable management, dedicated modules, and strict IAM policies—the project delivers an efficient, maintainable serverless architecture that supports dynamic scaling and simplified deployments.

Happy Deploying!
