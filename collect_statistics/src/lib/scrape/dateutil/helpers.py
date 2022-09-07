import math
from datetime import date, timedelta

from lib.scrape.dateutil import constants


def calculate_week(season_start_date, season_end_date, target_date=date.today()):
    """Determines the week of the season based on the given dates."""
    print(
        f"Calculating the number of weeks between "
        f"{season_start_date} and {season_end_date}"
    )
    if season_start_date >= season_end_date:
        raise ValueError(
            "The start date cannot be greater than or equal to the end date"
        )

    if target_date < season_start_date or target_date > season_end_date:
        raise ValueError(
            f"The target_date must be within the season_start_date {season_start_date}"
            f"and season_end_date {season_end_date}"
        )
    return (
        math.floor((target_date - season_start_date).days / constants.DAY_OF_WEEK) + 1
    )


def calculate_week_end(
    season_start_date: date, season_end_date: date, week: int = None
) -> date:
    """Determines the date the given week finished."""
    if season_start_date >= season_end_date:
        raise ValueError(
            "The start date cannot be greater than or equal to the end date"
        )

    weeks = weeks_in_season(season_start_date, season_end_date)
    if week < 1 or week > weeks_in_season(season_start_date, season_end_date):
        raise ValueError(f"The week parameter must be between 1 and {weeks}")

    if week is None:
        week = calculate_week(season_start_date, season_end_date)

    days = constants.DAYS_IN_WEEK * (week - 1)
    week_end_date = season_start_date + timedelta(days=days)
    while week_end_date.weekday() != constants.Weekday.WEDNESDAY.value:
        week_end_date += timedelta(days=1)
    return week_end_date


def weeks_in_season(season_start_date, season_end_date):
    """Determines the number of weeks in the season."""
    if season_start_date >= season_end_date:
        raise ValueError(
            "The start date cannot be greater than or equal to the end date"
        )

    return math.ceil(
        (season_end_date - season_start_date).days / constants.DAYS_IN_WEEK
    )


def months_between(start_date, end_date):
    """Calculate the number of months between two dates."""
    print(f"Calculating the number of months between {start_date} and {end_date}")
    return ((end_date.year - start_date.year) * constants.MONTHS_IN_YEAR) + (
        end_date.month - start_date.month
    )
