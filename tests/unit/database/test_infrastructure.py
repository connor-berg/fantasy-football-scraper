import math
import os

import aws_cdk as cdk
from aws_cdk import assertions
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda as lambda_

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

    app = cdk.App()
    test_stack = cdk.Stack(app, "TestStack")
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

    setup_statistics_fn = lambda_.Function(
        test_stack,
        "SetupStatistics",
        code=lambda_.Code.from_asset(os.path.join("setup_statistics", "src")),
        handler="app.lambda_handler",
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

    template = assertions.Template.from_stack(test_stack)

    template.resource_count_is("AWS::DynamoDB::Table", 3)
    template.resource_count_is("Custom::AWS", sdk_calls)

    template.has_resource_properties(
        "AWS::IAM::Policy",
        {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Action": [
                            "dynamodb:BatchGetItem",
                            "dynamodb:GetRecords",
                            "dynamodb:GetShardIterator",
                            "dynamodb:Query",
                            "dynamodb:GetItem",
                            "dynamodb:Scan",
                            "dynamodb:ConditionCheckItem",
                            "dynamodb:DescribeTable",
                        ],
                        "Effect": "Allow",
                        "Resource": [
                            {
                                "Fn::GetAtt": [
                                    assertions.Match.string_like_regexp(
                                        "DatabaseSeasonTable"
                                    ),
                                    "Arn",
                                ]
                            },
                            {"Ref": "AWS::NoValue"},
                        ],
                    },
                    {
                        "Action": [
                            "dynamodb:BatchGetItem",
                            "dynamodb:GetRecords",
                            "dynamodb:GetShardIterator",
                            "dynamodb:Query",
                            "dynamodb:GetItem",
                            "dynamodb:Scan",
                            "dynamodb:ConditionCheckItem",
                            "dynamodb:DescribeTable",
                        ],
                        "Effect": "Allow",
                        "Resource": [
                            {
                                "Fn::GetAtt": [
                                    assertions.Match.string_like_regexp(
                                        "DatabaseStatisticTable"
                                    ),
                                    "Arn",
                                ]
                            },
                            {"Ref": "AWS::NoValue"},
                        ],
                    },
                    {
                        "Action": [
                            "dynamodb:BatchGetItem",
                            "dynamodb:GetRecords",
                            "dynamodb:GetShardIterator",
                            "dynamodb:Query",
                            "dynamodb:GetItem",
                            "dynamodb:Scan",
                            "dynamodb:ConditionCheckItem",
                            "dynamodb:DescribeTable",
                        ],
                        "Effect": "Allow",
                        "Resource": [
                            {
                                "Fn::GetAtt": [
                                    assertions.Match.string_like_regexp(
                                        "DatabaseTeamTable"
                                    ),
                                    "Arn",
                                ]
                            },
                            {"Ref": "AWS::NoValue"},
                        ],
                    },
                ],
                "Version": "2012-10-17",
            }
        },
    )
