import json
from datetime import date

from lib.model import nfl
from lib.scrape import team_rankings as tr


def handler(event, context):
    """Collect the statistic for the week of a specific NFL season."""
    teams = event["teams"]
    season_dict = event["season"]
    week = int(event["week"])
    statistic = event["statistic"]

    year = int(season_dict["Id"])
    start_date = date.fromisoformat(season_dict["StartDate"])
    end_date = date.fromisoformat(season_dict["EndDate"])
    season = nfl.Season(year, start_date, end_date)

    print(f"Collecting statistics for week {week} between {start_date} and {end_date}")

    if week < 1 or week > season.weeks:
        raise ValueError(f"Invalid week for the {season.year} season")

    statistics = tr.collect_statistics(teams, season, week, statistic)
    data = json.loads(statistics.to_json(orient="records"))
    return {statistic["Id"]: data}
