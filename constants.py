import os

from aws_cdk import aws_dynamodb as dynamodb
import aws_cdk as cdk

CDK_APP_NAME = "FantasyFootballScraper"
CDK_APP_PYTHON_VERSION = "3.9"

DEV_ENV = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)
DEV_DATABASE_DYNAMODB_BILLING_MODE = dynamodb.BillingMode.PAY_PER_REQUEST