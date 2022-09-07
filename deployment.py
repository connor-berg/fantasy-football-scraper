from os import path
from typing import Any

import aws_cdk as cdk
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda as lambda_
from constructs import Construct

import constants
from database.infrastructure import Database, LoadTableResource


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
            serverless, "Database", dynamodb_billing_mode=database_dynamodb_billing_mode
        )
        LoadTableResource(
            serverless,
            "LoadSeasonTable",
            database.season_table,
            constants.SEASON_PUT_REQUESTS,
        )
        LoadTableResource(
            serverless,
            "LoadStatisticTable",
            database.statistic_table,
            constants.STATISTIC_PUT_REQUESTS,
        )
        LoadTableResource(
            serverless,
            "LoadTeamTable",
            database.team_table,
            constants.TEAM_PUT_REQUESTS,
        )

        setup_statistics_fn = lambda_.Function(
            serverless,
            "SetupStatisticsFunction",
            code=lambda_.Code.from_asset(path.join("setup_statistics", "src")),
            handler="app.handler",
            environment={
                "SEASON_TABLE_NAME": database.season_table.table_name,
                "STATISTIC_TABLE_NAME": database.statistic_table.table_name,
                "TEAM_TABLE_NAME": database.team_table.table_name,
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
        )
        database.season_table.grant_read_data(setup_statistics_fn)
        database.statistic_table.grant_read_data(setup_statistics_fn)
        database.team_table.grant_read_data(setup_statistics_fn)

        lambda_.Function(
            serverless,
            "CollectStatisticsFunction",
            code=lambda_.Code.from_asset(
                path.join("collect_statistics", "src"),
                bundling=cdk.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_9.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        "pip install -r requirements.txt -t /asset-output && \
                            cp -au . /asset-output",
                    ],
                ),
            ),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="app.handler",
        )
