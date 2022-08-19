import aws_cdk as cdk

import constants
from deployment import FantasyFootballScraper

app = cdk.App()

# Development
FantasyFootballScraper(
    app,
    f"{constants.CDK_APP_NAME}-Dev",
    env=constants.DEV_ENV,
    database_dynamodb_billing_mode=constants.DEV_DATABASE_DYNAMODB_BILLING_MODE,
)

# TODO: define production pipeline

app.synth()
