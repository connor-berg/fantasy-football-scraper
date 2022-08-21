from aws_cdk import App, Stack, assertions
from aws_cdk import aws_dynamodb as dynamodb

import constants
from database.infrastructure import Database, LoadTableResource


def test_infrastructure() -> None:
    app = App()
    test_stack = Stack(app, "TestStack")
    database = Database(
        test_stack,
        "Database",
        dynamodb_billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
    )
    LoadTableResource(
        test_stack,
        "LoadSeasonTable",
        database.season_table,
        constants.SEASON_PUT_REQUESTS,
    )
    LoadTableResource(
        test_stack,
        "LoadStatisticTable",
        database.statistic_table,
        constants.STATISTIC_PUT_REQUESTS,
    )
    LoadTableResource(
        test_stack,
        "LoadTeamTable",
        database.team_table,
        constants.TEAM_PUT_REQUESTS,
    )

    template = assertions.Template.from_stack(test_stack)

    template.resource_count_is("AWS::DynamoDB::Table", 3)
    template.resource_count_is("Custom::AWS", 4)
