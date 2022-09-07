import math
from datetime import date


class Season(object):

    DAYS_IN_WEEK = 7

    def __init__(self, year: int, start_date: date, end_date: date):
        self.year = year
        self.start_date = start_date
        self.end_date = end_date

        if self.start_date >= self.end_date:
            raise ValueError(
                "The season start dateutil cannot be greater than or equal to the end"
                "dateutil"
            )
        else:
            self.weeks = self._weeks_in_season()

    def __str__(self):
        return (
            f"Season(\n"
            f"\tYear={self.year},\n"
            f"\tStartDate={self.start_date},\n"
            f"\tEndDate={self.end_date},\n"
            f"\tWeeks={self.weeks},\n"
            f")"
        )

    def _weeks_in_season(self) -> int:
        """Determines the number of weeks in the season."""
        return math.ceil((self.end_date - self.start_date).days / self.DAYS_IN_WEEK)
