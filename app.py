#!/usr/bin/env python3
import os

import aws_cdk as cdk

from fantasy_football_scraper.fantasy_football_scraper_stack import FantasyFootballScraperStack


app = cdk.App()
FantasyFootballScraperStack(app, "FantasyFootballScraperStack")

app.synth()
