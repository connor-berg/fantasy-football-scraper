import aws_cdk as cdk
from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct


class Database(Construct):
    def __init__(
            self,
            scope: Construct,
            id_: str,
            *,
            dynamodb_billing_mode: dynamodb.BillingMode
    ) -> None:
        super().__init__(scope, id_)

        self.season_table = dynamodb.Table(
            self,
            "SeasonTable",
            billing_mode=dynamodb_billing_mode,
            partition_key=dynamodb.Attribute(
                name="Id", type=dynamodb.AttributeType.STRING
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        self.statistic_table = dynamodb.Table(
            self,
            "StatisticTable",
            billing_mode=dynamodb_billing_mode,
            partition_key=dynamodb.Attribute(
                name="Id", type=dynamodb.AttributeType.STRING
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        self.team_table = dynamodb.Table(
            self,
            "TeamTable",
            billing_mode=dynamodb_billing_mode,
            partition_key=dynamodb.Attribute(
                name="Id", type=dynamodb.AttributeType.STRING
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
