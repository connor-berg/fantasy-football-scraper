import aws_cdk as cdk
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_iam as iam
from aws_cdk import aws_logs as logs
from aws_cdk import custom_resources as cr
from constructs import Construct


class Database(Construct):
    def __init__(
        self, scope: Construct, id_: str, *, dynamodb_billing_mode: dynamodb.BillingMode
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


class LoadTableResource(Construct):

    MAX_PUT_REQUESTS = 25

    def chunk_requests(self):
        f"""
        Yield successive {self.MAX_PUT_REQUESTS}-sizedchunks from the
        resource's requests.
        """
        for i in range(0, len(self.requests), self.MAX_PUT_REQUESTS):
            yield self.requests[i : i + self.MAX_PUT_REQUESTS]  # noqa E203

    def __init__(
        self, scope: Construct, id_: str, table: dynamodb.Table, requests: list
    ) -> None:
        super().__init__(scope, id_)

        self.requests = requests
        chunked_requests = self.chunk_requests()

        for i, chunked_request in enumerate(chunked_requests):
            physical_resource_id = f"{table.table_name}_loadData_{i}"
            sdk_call = cr.AwsSdkCall(
                service="DynamoDB",
                action="batchWriteItem",
                parameters={"RequestItems": {table.table_name: chunked_request}},
                physical_resource_id=cr.PhysicalResourceId.of(physical_resource_id),
            )

            policy = cr.AwsCustomResourcePolicy.from_statements(
                [
                    iam.PolicyStatement(
                        actions=["dynamodb:BatchWriteItem"], resources=[table.table_arn]
                    )
                ]
            )
            resource = cr.AwsCustomResource(
                self,
                f"LoadTableResource_{i}",
                on_create=sdk_call,
                policy=policy,
                log_retention=logs.RetentionDays.ONE_DAY,
            )
            resource.node.add_dependency(table)
