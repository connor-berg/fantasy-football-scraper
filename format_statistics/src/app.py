import json
import os

import boto3
import pandas as pd


def _update_header(stat: dict, headers: dict) -> str:
    old_header = list(stat.keys())[0]
    new_header = headers[
        old_header
    ]  # TODO: handle scenario where old header doesn't exist
    stat[new_header] = stat[old_header]
    del stat[old_header]
    return new_header


def handler(event, context):
    """Format the statistics collected for the week of a specific NFL season."""

    dynamodb = boto3.resource("dynamodb")
    statistic_table = dynamodb.Table(os.environ.get("STATISTIC_TABLE_NAME"))

    response = statistic_table.scan()
    statistics = response["Items"]
    while "LastEvaluatedKey" in response:
        response = statistic_table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        statistics.extend(response["Items"])
    headers = {statistic["Id"]: statistic["Abbreviation"] for statistic in statistics}

    stats_df = None
    collected_stats = [i["Payload"] for i in event]
    for stat in collected_stats:
        header = _update_header(stat, headers)
        value = stat[header]
        value["columns"] = [header if i == "Stat" else i for i in value["columns"]]
        if stats_df is None:
            stats_df = pd.read_json(json.dumps(stat[header]), orient="split")
        else:
            stats_df = pd.read_json(json.dumps(stat[header]), orient="split").merge(
                stats_df, on="Team"
            )

    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(stats_df)

    return json.loads(stats_df.to_json(orient="split"))
