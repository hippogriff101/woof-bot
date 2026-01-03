import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import random
from openrouter import OpenRouter
import re

# I promis it aint ai just my dody comments

load_dotenv() # .env!!!!

app = App(token=os.getenv("SLACK_BOT_TOKEN"))

# ai.hackclub.com!
client = OpenRouter(
    api_key=(os.getenv("HCAI-API_KEY")),
    server_url="https://ai.hackclub.com/proxy/v1",
)
# Veriables for everything:
emojis = ["dog", "dog2", "woofwoof", "dogheart","neodog"]
dog_pics = [
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/882540f107764bbc_275c634a-ee0a-43c5-b820-1e90c75f91e2.jpeg",
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/db3d590ad90c3e09_img_0422.jpg",
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/1363c8a1eec46da9_monzi.jpg",
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/0458730ae579c1bb_fullsizerender.jpg",
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/600a6274d27e6a31_59ffb974-acb4-400a-955c-d11b5dd5faa1-1_all_43378.jpg",
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/227d7c199c51969d_img_8431.jpg",
    "https://hc-cdn.hel1.your-objectstorage.com/s/v3/31016a72efd0661f_img_9854.jpg",
]

@app.event("message") #idk what this does but it kept bugging me in terminal
def handle_other_messages():
    pass

@app.message(re.compile("woof", re.IGNORECASE)) # random dog emojiiii
def woof_reaction(message, client):
    print("Woof message detected")
    client.reactions_add(
        channel=message["channel"],
        timestamp=message["ts"],
        name=random.choice(emojis)
    )

@app.event("app_mention")
def handle_mention(event, say, client):
    print("Bot mentioned in message")
    pic = random.choice(dog_pics)
    client.reactions_add(
        channel=event["channel"],
        timestamp=event["ts"],
        name=random.choice(emojis)
    )
    say(
        text="Here's a cute dog pic!",
        blocks=[
            {
                "type": "image",
                "image_url": random.choice(dog_pics),
                "alt_text": "Cute Dog"
            },
        ],
        thread_ts=event["ts"]
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
def woof_ideas_command(ack, say):
    ack()
    print("Ideas command invoked")
    response = client.chat.send(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "user", "content": "You are a AI Slack Bot, your only duty is to respond with SHORT one sentance creative project idea related to dogs and would take 5 hourse to code. Please do not use markdown formatting or any other formatting. Just respond with the idea."}
        ],
        stream=False,
    )
    print("Received response from OpenRouter:", response)
    say(
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
    print("Idea sent to channel")

@app.command("/dogpics")
def woof_pics_command(ack, respond):
    print("Dog pics command invoked")
    ack()

    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Here are some cute dog pictures for you! :{random.choice(emojis)}:"
                }
            },
            {
                "type": "image",
                "image_url": random.choice(dog_pics),
                "alt_text": "Cute Dog"
            },
        ]
    )

if __name__ == "__main__":
    SocketModeHandler(
        app,
        os.getenv("SLACK_APP_TOKEN")
    ).start()
