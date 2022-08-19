from aws_cdk import (
    assertions,
    aws_dynamodb as dynamodb,
    App,
    Stack
)

from database.infrastructure import Database


def test_infrastructure() -> None:
    app = App()
    stack = Stack(app, "Stack")
    database = Database(
        stack, "Database", dynamodb_billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
    )

    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::DynamoDB::Table", 3)
    template.resource_count_is("Custom::AWS", 3)
