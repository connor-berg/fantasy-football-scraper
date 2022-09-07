import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from lib.model import nfl
from lib.scrape.dateutil import helpers

BASE_URL = "https://www.teamrankings.com/nfl/stat/"
DEFAULT_STAT_COLUMN_HEADER = "Last 1"


def _parse_columns(table: Tag) -> list[str]:
    """Parse the table headers into a list of header names."""
    thead = table.find("thead")
    tr = thead.find("tr")
    columns = [column.text for column in tr if column.text != "\n"]
    return columns


def _parse_data(table: Tag) -> list[list]:
    """Parse the table data into a list of rows."""
    data = list()
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        text = [td.text for td in tds]
        data.append(text)
    return data


def _table_to_dataframe(table: Tag) -> pd.DataFrame:
    """Convert the table to a Pandas DataFrame."""
    columns = _parse_columns(table)
    data = _parse_data(table)
    return pd.DataFrame(columns=columns, data=data)


def _scrape_table(url: str) -> Tag:
    """Find the table with data with the given Selenium WebDriver."""
    page = requests.get(url)
    if page.status_code != 200:
        # TODO: error
        return None
    soup = BeautifulSoup(page.text, "html.parser")
    return soup.find("table", {"class": "datatable"})


def _format_dataframe(teams: dict, stats_df: pd.DataFrame) -> pd.DataFrame:
    """Format the stats DataFrame by dropping unnecessary columns, renaming columns,
    and sorting the data."""
    teams_df = pd.DataFrame.from_dict(data=teams)
    teams_df.drop(columns=["Id", "Name"], inplace=True)
    teams_df.columns = ["Team"]

    formatted_df = teams_df.merge(stats_df[["Team", "Last 1"]], on="Team")
    formatted_df.rename(columns={DEFAULT_STAT_COLUMN_HEADER: "Stat"}, inplace=True)
    to_replace = {team["Label"]: team["Name"] for team in teams}
    formatted_df["Team"].replace(to_replace, inplace=True)
    formatted_df.sort_values(by=["Team"], inplace=True)
    return formatted_df


def collect_statistics(
    teams: dict, season: nfl.Season, week: int, statistic: dict
) -> pd.DataFrame:
    """Collect the given statistic for each NFL team for the given week in the
    given season."""

    print("Collecting statistics")
    target_date = helpers.calculate_week_end(season.start_date, season.end_date, week)
    url = f"{BASE_URL}{statistic['Id']}?date={target_date.isoformat()}"

    table = _scrape_table(url)
    if table is None:
        print("ERROR - couldn't find table")
        return None
    else:
        df = _table_to_dataframe(table)
        df = _format_dataframe(teams=teams, stats_df=df)
        with pd.option_context("display.max_rows", None, "display.max_columns", None):
            print(df)
        return df
