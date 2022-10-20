from os import path
from typing import Any

import aws_cdk as cdk
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks
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

        setup_statistics = tasks.LambdaInvoke(
            serverless,
            "Setup Statistics",
            lambda_function=setup_statistics_fn,
            invocation_type=tasks.LambdaInvocationType.REQUEST_RESPONSE,
        )

        collect_statistics_fn = lambda_.Function(
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
            timeout=cdk.Duration.seconds(5),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="app.handler",
        )

        collect_statistics_map = sfn.Map(
            serverless,
            "Map State",
            input_path="$.Payload",
            items_path="$.statistics",
            parameters={
                "teams.$": "$.teams",
                "season.$": "$.season",
                "week.$": "$.week",
                "statistic.$": "$$.Map.Item.Value",
            },
        )
        collect_statistics_map.iterator(
            tasks.LambdaInvoke(
                serverless,
                "Collect Statistics",
                lambda_function=collect_statistics_fn,
                invocation_type=tasks.LambdaInvocationType.REQUEST_RESPONSE,
            )
        )

        format_statistics_fn = lambda_.Function(
            serverless,
            "FormatStatisticsFunction",
            code=lambda_.Code.from_asset(
                path.join("format_statistics", "src"),
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
            timeout=cdk.Duration.seconds(5),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="app.handler",
            environment={
                "STATISTIC_TABLE_NAME": database.statistic_table.table_name,
            },
        )
        database.statistic_table.grant_read_data(format_statistics_fn)

        format_statistics = tasks.LambdaInvoke(
            serverless,
            "Format Statistics",
            lambda_function=format_statistics_fn,
            invocation_type=tasks.LambdaInvocationType.REQUEST_RESPONSE,
        )

        definition = setup_statistics.next(collect_statistics_map).next(
            format_statistics
        )
        state_machine = sfn.StateMachine(
            serverless,
            "FantasyFootballScraperStateMachine",
            definition=definition,
            timeout=cdk.Duration.minutes(5),
        )

        rule = events.Rule(
            serverless,
            "Run Weekly at 11:00 hrs UTC SEP-JAN",
            # UTC - 6 time. ~6 AM CST
            # UTC - 5 time. ~5 AM CDT
            schedule=events.Schedule.cron(
                minute="0", hour="11", week_day="MON", month="SEP-JAN", year="*"
            ),
        )
        rule.add_target(targets.SfnStateMachine(state_machine))
