import aws_cdk as core
import aws_cdk.assertions as assertions

from fantasy_football_scraper.fantasy_football_scraper_stack import FantasyFootballScraperStack

# example tests. To run these tests, uncomment this file along with the example
# resource in fantasy_football_scraper/fantasy_football_scraper_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FantasyFootballScraperStack(app, "fantasy-football-scraper")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
