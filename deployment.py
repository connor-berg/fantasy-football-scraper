from typing import Any

import aws_cdk as cdk
from aws_cdk import (
    aws_dynamodb as dynamodb
)
from constructs import Construct

import constants
from database.infrastructure import (
    Database,
    LoadTableResource
)


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
        LoadTableResource(serverless, "LoadSeasonTable", database.season_table, constants.SEASON_PUT_REQUESTS)
        LoadTableResource(serverless, "LoadStatisticTable", database.statistic_table, constants.STATISTIC_PUT_REQUESTS)
        LoadTableResource(serverless, "LoadTeamTable", database.team_table, constants.TEAM_PUT_REQUESTS)
