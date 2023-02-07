# cloud-resume

This is a static resume site hosted via an Amazon S3 bucket. Route 53 points a custom domain name to a CloudFront distribution which points to the S3 bucket. The site is secured with an HTTPS certificate.

To explore how a serverless application works, a visitor counter was implemented using JavaScript, which retrieves and updates its count in a DynamoDB table. When a user visits the site, an endpoint to a lambda function is contacted through the API Gateway, which updates the current value in the DynamoDB table; the updated value is what's displayed to the user. The lambda functions were created using the AWS SDK for Python (boto3).

The DynamoDB table, API Gateway, and Lambda functions are defined in an AWS Serverless Application Model (SAM) template. This is called infrastructure as code (IaC).

Throughout most of development, the AWS SAM CLI was used to deploy changes to the site contents and infrastructure. AWS Vault was useful here in managing the credentials for the IAM user I created to make any and all changes. However, I eventually created a continuous deployment pipeline with GitHub Actions. So now when an update is pushed to this repo, the SAM application gets packaged and deployed to AWS, the S3 bucket automatically gets updated, and the CloudFront distribution is invalidated (to force a retrieval of the new files in S3).
