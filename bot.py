import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random

load_dotenv()

token = os.getenv("SLACK_TOKEN")
if not token:
	raise RuntimeError("SLACK_TOKEN missing in environment or .env")

client = WebClient(token=token)

message = random.choice([
	"Woof!",
	"Barkkkk",
	"Grrr...",
	"Woof woof!",
])
try:
	client.chat_postMessage(channel="#woof-orgs", text=message) # To hackclubber, this is a private channel for the Woof Orgs
except SlackApiError as e:
	print(f"Slack error: {e.response.get('error')}")
except Exception as e:
	print(f"Unexpected error: {e}")