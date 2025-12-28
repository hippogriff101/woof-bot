import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import random
from openrouter import OpenRouter

load_dotenv()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))

client = OpenRouter(
    api_key=(os.getenv("HCAI-API_KEY")),
    server_url="https://ai.hackclub.com/proxy/v1",
)

@app.message("woof")
def woof_reaction(message, client):
    print("Woof message detected")
    client.reactions_add(
        channel=message["channel"],
        timestamp=message["ts"],
        name=random.choice(["dog", "dog2", "woofwoof", "dogheart","neodog"])
    )

@app.command("/woof")
def woof_command(ack, respond):
    print("Woof command invoked")
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

@app.command("/ideas")
def woof_ideas_command(ack, respond):
    ack()
    
    response = client.chat.send(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "user", "content": "You are a AI Slack Bot, your only duty is to respond with SHORT one sentance creative project idea related to dogs and would take 5 hourse to code."}
        ],
        stream=False,
    )
    
    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": response.choices[0].message.content
                }
            },
        ]
    )
@app.command("/dogpics")
def woof_pics_command(ack, respond):
    print("Dog pics command invoked")
    ack()
    
    pic = random.choice([
        "https://hc-cdn.hel1.your-objectstorage.com/s/v3/60fa7a51d405c463_puppy1.jpg",
        "https://hc-cdn.hel1.your-objectstorage.com/s/v3/bcf2e616df58f07b_puppy3.jpg",
        "https://hc-cdn.hel1.your-objectstorage.com/s/v3/7b6cf411b025736c_puppy2.jpg",
    ])

    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here are some cute dog pictures for you! :dog:"
                }
            },
            {
                "type": "image",
                "image_url": pic,
                "alt_text": "Cute Dog"
            },
        ]
    )

if __name__ == "__main__":
    SocketModeHandler(
        app,
        os.getenv("SLACK_APP_TOKEN")
    ).start()
