import math

from aws_cdk import App, Stack, assertions
from aws_cdk import aws_dynamodb as dynamodb

from database.infrastructure import Database, LoadTableResource
from tests import constants


def _calculate_sdk_calls(put_requests: list) -> int:
    """
    Determine the number of SDK calls needed to write all items in `put_requests`.
    There is a 25-item limit on calls to dynamodb:BatchWriteItem.
    :param put_requests:
    :return: The number of SDK calls needed
    """
    return math.ceil(len(put_requests) / LoadTableResource.MAX_PUT_REQUESTS)


def test_infrastructure() -> None:
    sdk_calls = 0

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
    sdk_calls += _calculate_sdk_calls(constants.SEASON_PUT_REQUESTS)
    LoadTableResource(
        test_stack,
        "LoadStatisticTable",
        database.statistic_table,
        constants.STATISTIC_PUT_REQUESTS,
    )
    sdk_calls += _calculate_sdk_calls(constants.STATISTIC_PUT_REQUESTS)
    LoadTableResource(
        test_stack,
        "LoadTeamTable",
        database.team_table,
        constants.TEAM_PUT_REQUESTS,
    )
    sdk_calls += _calculate_sdk_calls(constants.TEAM_PUT_REQUESTS)

    template = assertions.Template.from_stack(test_stack)

    template.resource_count_is("AWS::DynamoDB::Table", 3)
    template.resource_count_is("Custom::AWS", sdk_calls)
