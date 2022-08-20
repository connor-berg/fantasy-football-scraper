import aws_cdk as cdk

from constants import (
    CDK_APP_NAME,
    DEV_DATABASE_DYNAMODB_BILLING_MODE,
    DEV_ENV,
    PIPELINE_ENV,
)
from deployment import FantasyFootballScraper
from pipeline import Pipeline

app = cdk.App()

# Development
FantasyFootballScraper(
    app,
    f"{CDK_APP_NAME}-Dev",
    env=DEV_ENV,
    database_dynamodb_billing_mode=DEV_DATABASE_DYNAMODB_BILLING_MODE,
)

# Production pipeline
Pipeline(app, f"{CDK_APP_NAME}-Pipeline", env=PIPELINE_ENV)

app.synth()
