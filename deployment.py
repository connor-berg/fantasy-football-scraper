from typing import Any

import aws_cdk as cdk
from aws_cdk import (
    aws_dynamodb as dynamodb
)
from constructs import Construct

from database.infrastructure import Database


class FantasyFootballScraper(cdk.Stage):
    def __init__(
            self,
            scope: Construct,
            id_: str,
            *,
            database_dynamodb_billing_mode: dynamodb.BillingMode,
            **kwargs: Any,
    ) -> None:
        super().__init__(scope, id_, **kwargs)

        serverless = cdk.Stack(self, "Serverless")

        database = Database(
            serverless, "Database",
            dynamodb_billing_mode=database_dynamodb_billing_mode
        )
