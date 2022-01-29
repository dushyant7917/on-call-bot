import json
import requests
import os

from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient
from dotenv import load_dotenv


ENV_FILE_PATH = ".env"
load_dotenv(ENV_FILE_PATH)

SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
EVENT_PROCESSING_SERVICE_URL = os.environ["EVENT_PROCESSING_SERVICE_URL"]

slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events")
slack_client = WebClient(SLACK_BOT_TOKEN)

def send_data(data, url=EVENT_PROCESSING_SERVICE_URL):
    requests.post(url, data=data)


@slack_events_adapter.on("message")
def handle_message(event_data):
    send_data(event_data)


@slack_events_adapter.on("app_mention")
def handle_mentions(event_data):
    send_data(event_data)


slack_events_adapter.start(port=3000)