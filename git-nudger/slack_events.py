import os
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from dotenv import load_dotenv

load_dotenv()

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

app_handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_app_mention_events(body, say):
    """Handles app mention events and responds."""
    text = body["event"]["text"]
    say(f"You mentioned me, and said: '{text}'")


@app.command("/list_prs")
def list_prs(ack, say, command):
    """Lists open pull requests."""
    ack()
    say("Listing open PRs...")
    # In a real app, you'd fetch this from GitHub
    say("1. [FEAT] Add new login page - #123")
    say("2. [FIX] Fix bug in user profile - #456")
