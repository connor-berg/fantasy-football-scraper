import os
from datetime import date

import boto3


def _get_season(season_table) -> dict:
    """Retrieves the current season from the provided DynamoDB table"""
    year = str(date.today().year - 1)  # TODO just for testing
    response = season_table.get_item(Key={"Id": year})
    # TODO: handle scenario where we're in the next year,
    #  but it's still the previous year's season
    return response["Item"]


def handler(event, context):
    """Handle lambda"""
    dynamodb = boto3.resource("dynamodb")
    team_table = dynamodb.Table(os.environ.get("TEAM_TABLE_NAME"))
    season_table = dynamodb.Table(os.environ.get("SEASON_TABLE_NAME"))
    statistic_table = dynamodb.Table(os.environ.get("STATISTIC_TABLE_NAME"))

    response = team_table.scan()
    teams = response["Items"]
    while "LastEvaluatedKey" in response:
        response = statistic_table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        teams.extend(response["Items"])

    season = _get_season(season_table)

    response = statistic_table.scan()
    statistics = response["Items"]
    while "LastEvaluatedKey" in response:
        response = statistic_table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        statistics.extend(response["Items"])

    print("Setting up statistics for the following teams:")
    for team in teams:
        print(team)

    print("Setting up the following statistics:")
    for statistic in statistics:
        print(statistic)

    return {"teams": teams, "season": season, "week": 1, "statistics": statistics}
