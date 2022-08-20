import json
import pathlib

import aws_cdk as cdk
from aws_cdk import aws_codebuild as codebuild
from aws_cdk import pipelines
from constructs import Construct

from constants import (
    CDK_APP_NAME,
    CDK_APP_PYTHON_VERSION,
    GITHUB_CONNECTION_ARN,
    GITHUB_OWNER,
    GITHUB_REPO,
    GITHUB_TRUNK_BRANCH,
    PROD_DATABASE_DYNAMODB_BILLING_MODE,
    PROD_ENV,
)
from deployment import FantasyFootballScraper


class Pipeline(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        build_spec = {
            "phases": {
                "install": {"runtime-versions": {"python": CDK_APP_PYTHON_VERSION}}
            }
        }
        pipeline_source = pipelines.CodePipelineSource.connection(
            f"{GITHUB_OWNER}/{GITHUB_REPO}",
            GITHUB_TRUNK_BRANCH,
            connection_arn=GITHUB_CONNECTION_ARN,
        )
        synth_codebuild_step = pipelines.CodeBuildStep(
            "Synth",
            input=pipeline_source,
            partial_build_spec=codebuild.BuildSpec.from_object(build_spec),
            install_commands=["./scripts/install-deps.sh"],
            commands=["pytest", "npx aws-cdk@2.x synth"],
            primary_output_directory="cdk.out",
        )
        pipeline = pipelines.CodePipeline(
            self,
            "CodePipeline",
            cli_version=Pipeline._get_cdk_cli_version(),
            cross_account_keys=True,
            synth=synth_codebuild_step,
        )

        self._add_prod_stage(pipeline)

    @staticmethod
    def _get_cdk_cli_version() -> str:
        package_json_path = (
            pathlib.Path(__file__).resolve().parent.joinpath("package.json")
        )
        with open(package_json_path) as package_json_file:
            package_json = json.load(package_json_file)
        cdk_cli_version = str(package_json["devDependencies"]["aws-cdk"])
        return cdk_cli_version

    def _add_prod_stage(self, codepipeline: pipelines.CodePipeline) -> None:
        prod_stage = FantasyFootballScraper(
            self,
            f"{CDK_APP_NAME}-Prod",
            env=PROD_ENV,
            database_dynamodb_billing_mode=PROD_DATABASE_DYNAMODB_BILLING_MODE,
        )
        codepipeline.add_stage(prod_stage)
