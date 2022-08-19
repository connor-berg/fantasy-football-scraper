import os

from aws_cdk import aws_dynamodb as dynamodb
import aws_cdk as cdk

CDK_APP_NAME = "FantasyFootballScraper"
CDK_APP_PYTHON_VERSION = "3.9"

DEV_ENV = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)
DEV_DATABASE_DYNAMODB_BILLING_MODE = dynamodb.BillingMode.PAY_PER_REQUEST

TEAM_PUT_REQUESTS = \
    [
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "CAR"
                    },
                    "Name": {
                        "S": "Panthers"
                    },
                    "Label": {
                        "S": "Carolina"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "JAX"
                    },
                    "Name": {
                        "S": "Jaguars"
                    },
                    "Label": {
                        "S": "Jacksonville"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "LA"
                    },
                    "Name": {
                        "S": "Rams"
                    },
                    "Label": {
                        "S": "LA Rams"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "BAL"
                    },
                    "Name": {
                        "S": "Ravens"
                    },
                    "Label": {
                        "S": "Baltimore"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "CHI"
                    },
                    "Name": {
                        "S": "Bears"
                    },
                    "Label": {
                        "S": "Chicago"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "NO"
                    },
                    "Name": {
                        "S": "Saints"
                    },
                    "Label": {
                        "S": "New Orleans"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "WAS"
                    },
                    "Name": {
                        "S": "Redskins"
                    },
                    "Label": {
                        "S": "Washington"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "PHI"
                    },
                    "Name": {
                        "S": "Eagles"
                    },
                    "Label": {
                        "S": "Philadelphia"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "PIT"
                    },
                    "Name": {
                        "S": "Steelers"
                    },
                    "Label": {
                        "S": "Pittsburgh"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "ARI"
                    },
                    "Name": {
                        "S": "Cardinals"
                    },
                    "Label": {
                        "S": "Arizona"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "SEA"
                    },
                    "Name": {
                        "S": "Seahawks"
                    },
                    "Label": {
                        "S": "Seattle"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "LAC"
                    },
                    "Name": {
                        "S": "Chargers"
                    },
                    "Label": {
                        "S": "LA Chargers"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "DEN"
                    },
                    "Name": {
                        "S": "Broncos"
                    },
                    "Label": {
                        "S": "Denver"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "DET"
                    },
                    "Name": {
                        "S": "Lions"
                    },
                    "Label": {
                        "S": "Detroit"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "MIA"
                    },
                    "Name": {
                        "S": "Dolphins"
                    },
                    "Label": {
                        "S": "Miami"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "BUF"
                    },
                    "Name": {
                        "S": "Bills"
                    },
                    "Label": {
                        "S": "Buffalo"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "KC"
                    },
                    "Name": {
                        "S": "Chiefs"
                    },
                    "Label": {
                        "S": "Kansas City"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "ATL"
                    },
                    "Name": {
                        "S": "Falcons"
                    },
                    "Label": {
                        "S": "Atlanta"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "GB"
                    },
                    "Name": {
                        "S": "Packers"
                    },
                    "Label": {
                        "S": "Green Bay"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "DAL"
                    },
                    "Name": {
                        "S": "Cowboys"
                    },
                    "Label": {
                        "S": "Dallas"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "HOU"
                    },
                    "Name": {
                        "S": "Texans"
                    },
                    "Label": {
                        "S": "Houston"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "NE"
                    },
                    "Name": {
                        "S": "Patriots"
                    },
                    "Label": {
                        "S": "New England"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "NYJ"
                    },
                    "Name": {
                        "S": "Jets"
                    },
                    "Label": {
                        "S": "NY Jets"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "CLE"
                    },
                    "Name": {
                        "S": "Browns"
                    },
                    "Label": {
                        "S": "Cleveland"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "TEN"
                    },
                    "Name": {
                        "S": "Titans"
                    },
                    "Label": {
                        "S": "Tennessee"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "NYG"
                    },
                    "Name": {
                        "S": "Giants"
                    },
                    "Label": {
                        "S": "NY Giants"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "TB"
                    },
                    "Name": {
                        "S": "Buccaneers"
                    },
                    "Label": {
                        "S": "Tampa Bay"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "LV"
                    },
                    "Name": {
                        "S": "Raiders"
                    },
                    "Label": {
                        "S": "Las Vegas"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "CIN"
                    },
                    "Name": {
                        "S": "Bengals"
                    },
                    "Label": {
                        "S": "Cincinnati"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "IND"
                    },
                    "Name": {
                        "S": "Colts"
                    },
                    "Label": {
                        "S": "Indianapolis"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "SF"
                    },
                    "Name": {
                        "S": "49ers"
                    },
                    "Label": {
                        "S": "San Francisco"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "MIN"
                    },
                    "Name": {
                        "S": "Vikings"
                    },
                    "Label": {
                        "S": "Minneapolis"
                    }
                }
            }
        }
    ]

SEASON_PUT_REQUESTS = \
    [
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2010"
                    },
                    "StartDate": {
                        "S": "2010-09-09"
                    },
                    "EndDate": {
                        "S": "2011-01-02"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2011"
                    },
                    "StartDate": {
                        "S": "2011-09-08"
                    },
                    "EndDate": {
                        "S": "2012-01-01"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2012"
                    },
                    "StartDate": {
                        "S": "2012-09-05"
                    },
                    "EndDate": {
                        "S": "2012-12-30"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2013"
                    },
                    "StartDate": {
                        "S": "2013-09-05"
                    },
                    "EndDate": {
                        "S": "2013-12-29"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2014"
                    },
                    "StartDate": {
                        "S": "2014-09-04"
                    },
                    "EndDate": {
                        "S": "2014-12-28"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2015"
                    },
                    "StartDate": {
                        "S": "2015-09-10"
                    },
                    "EndDate": {
                        "S": "2016-01-03"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2016"
                    },
                    "StartDate": {
                        "S": "2016-09-08"
                    },
                    "EndDate": {
                        "S": "2017-01-01"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2017"
                    },
                    "StartDate": {
                        "S": "2017-09-07"
                    },
                    "EndDate": {
                        "S": "2017-12-31"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2018"
                    },
                    "StartDate": {
                        "S": "2018-09-06"
                    },
                    "EndDate": {
                        "S": "2018-12-30"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2019"
                    },
                    "StartDate": {
                        "S": "2019-09-05"
                    },
                    "EndDate": {
                        "S": "2019-12-29"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2020"
                    },
                    "StartDate": {
                        "S": "2020-09-10"
                    },
                    "EndDate": {
                        "S": "2021-01-03"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2021"
                    },
                    "StartDate": {
                        "S": "2021-09-09"
                    },
                    "EndDate": {
                        "S": "2022-01-09"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2022"
                    },
                    "StartDate": {
                        "S": "2022-09-08"
                    },
                    "EndDate": {
                        "S": "2023-01-08"
                    }
                }
            }
        }
    ]

STATISTIC_PUT_REQUESTS = \
    [
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "completions-per-game"
                    },
                    "Name": {
                        "S": "Completions Per Game"
                    },
                    "Abbreviation": {
                        "S": "Completions"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "first-downs-per-play"
                    },
                    "Name": {
                        "S": "First Downs Per Play"
                    },
                    "Abbreviation": {
                        "S": "1stDown"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "interceptions-per-game"
                    },
                    "Name": {
                        "S": "Interceptions Per Game"
                    },
                    "Abbreviation": {
                        "S": "Int"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "opponent-fumbles-lost-per-game"
                    },
                    "Name": {
                        "S": "Opponent Fumbles Lost Per Game"
                    },
                    "Abbreviation": {
                        "S": "FR"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "opponent-yards-per-game"
                    },
                    "Name": {
                        "S": "Opponent Yards Per Game"
                    },
                    "Abbreviation": {
                        "S": "Yd"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "pass-attempts-per-game"
                    },
                    "Name": {
                        "S": "Pass Attempts Per Game"
                    },
                    "Abbreviation": {
                        "S": "PassAtt"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "passing-first-downs-per-game"
                    },
                    "Name": {
                        "S": "Passing First Downs Per Game"
                    },
                    "Abbreviation": {
                        "S": "Pass1stD"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "passing-touchdowns-per-game"
                    },
                    "Name": {
                        "S": "Passing Touchdowns Per Game"
                    },
                    "Abbreviation": {
                        "S": "PassTd"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "passing-yards-per-game"
                    },
                    "Name": {
                        "S": "Passing Yards Per Game"
                    },
                    "Abbreviation": {
                        "S": "PassYd"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "plays-per-game"
                    },
                    "Name": {
                        "S": "Plays Per Game"
                    },
                    "Abbreviation": {
                        "S": "Plays"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "points-per-game"
                    },
                    "Name": {
                        "S": "Points Per Game"
                    },
                    "Abbreviation": {
                        "S": "Score"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "punt-attempts-per-game"
                    },
                    "Name": {
                        "S": "Punt Attempts Per Game"
                    },
                    "Abbreviation": {
                        "S": "Punts"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "red-zone-scoring-percentage"
                    },
                    "Name": {
                        "S": "Red Zone Scoring Percentage"
                    },
                    "Abbreviation": {
                        "S": "RZ%"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "rushing-yards-per-game"
                    },
                    "Name": {
                        "S": "Rushing Yards Per Game"
                    },
                    "Abbreviation": {
                        "S": "RushYd"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "sacks-per-game"
                    },
                    "Name": {
                        "S": "Sacks Per Game"
                    },
                    "Abbreviation": {
                        "S": "Sacks"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "touchdowns-per-game"
                    },
                    "Name": {
                        "S": "Touchdowns Per Game"
                    },
                    "Abbreviation": {
                        "S": "TD"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "overtime-points-per-game"
                    },
                    "Name": {
                        "S": "Overtime Points Per Game"
                    },
                    "Abbreviation": {
                        "S": "OT"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "defensive-touchdowns-per-game"
                    },
                    "Name": {
                        "S": "Defensive Touchdowns Per Game"
                    },
                    "Abbreviation": {
                        "S": "DefTD"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "1st-quarter-points-per-game"
                    },
                    "Name": {
                        "S": "1st Quarter Points Per Game"
                    },
                    "Abbreviation": {
                        "S": "1stQtr"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "2nd-quarter-points-per-game"
                    },
                    "Name": {
                        "S": "2nd Quarter Points Per Game"
                    },
                    "Abbreviation": {
                        "S": "2ndQtr"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "3rd-quarter-points-per-game"
                    },
                    "Name": {
                        "S": "3rd Quarter Points Per Game"
                    },
                    "Abbreviation": {
                        "S": "3rdQtr"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "4th-quarter-points-per-game"
                    },
                    "Name": {
                        "S": "4th Quarter Points Per Game"
                    },
                    "Abbreviation": {
                        "S": "4thQtr"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "special-teams-touchdowns-per-game"
                    },
                    "Name": {
                        "S": "Special Teams Touchdowns Per Game"
                    },
                    "Abbreviation": {
                        "S": "SpecialTD"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "Id": {
                        "S": "safeties-per-game"
                    },
                    "Name": {
                        "S": "Safeties Per Game"
                    },
                    "Abbreviation": {
                        "S": "Safeties"
                    }
                }
            }
        }
    ]
