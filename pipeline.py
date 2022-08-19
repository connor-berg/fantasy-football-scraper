import json
import pathlib

import aws_cdk as cdk
from aws_cdk import (
    aws_codebuild as codebuild,
    pipelines
)
from constructs import Construct

import constants
from deployment import FantasyFootballScraper


class Pipeline(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        build_spec = {
            "phases": {
                "install": {
                    "runtime-versions": {"python": constants.CDK_APP_PYTHON_VERSION}
                }
            }
        }
        pipeline_source = pipelines.CodePipelineSource.connection(
            f"{constants.GITHUB_OWNER}/{constants.GITHUB_REPO}",
            constants.GITHUB_TRUNK_BRANCH,
            connection_arn=constants.GITHUB_CONNECTION_ARN,
        )
        synth_codebuild_step = pipelines.CodeBuildStep(
            "Synth",
            input=pipeline_source,
            partial_build_spec=codebuild.BuildSpec.from_object(build_spec),
            install_commands=["./scripts/install-deps.sh"],
            commands=["./scripts/run-tests.sh", "npx aws-cdk@2.x synth"],
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
            f"{constants.CDK_APP_NAME}-Prod",
            env=constants.PROD_ENV,
            database_dynamodb_billing_mode=constants.PROD_DATABASE_DYNAMODB_BILLING_MODE,
        )
        codepipeline.add_stage(prod_stage)
