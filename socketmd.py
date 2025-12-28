import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))

@app.message("woof")
def woof_reaction(message, client):
    client.reactions_add(
        channel=message["channel"],
        timestamp=message["ts"],
        name="woofwoof"
    )

@app.command("/woof")
def woof_command(ack, respond):
    ack()

    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Woof!* :woofwoof:."
                }
            },
        ]
    )

if __name__ == "__main__":
    SocketModeHandler(
        app,
        os.getenv("SLACK_APP_TOKEN")
    ).start()
