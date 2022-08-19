import aws_cdk as cdk

import constants
from deployment import FantasyFootballScraper
from pipeline import Pipeline

app = cdk.App()

# Development
FantasyFootballScraper(
    app,
    f"{constants.CDK_APP_NAME}-Dev",
    env=constants.DEV_ENV,
    database_dynamodb_billing_mode=constants.DEV_DATABASE_DYNAMODB_BILLING_MODE,
)

# Production pipeline
Pipeline(app, f"{constants.CDK_APP_NAME}-Pipeline", env=constants.PIPELINE_ENV)

app.synth()
