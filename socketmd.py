import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import random
from openrouter import OpenRouter
import re

# --------------------
load_dotenv()
app = App(token=os.getenv("SLACK_BOT_TOKEN"))
client = OpenRouter(
    api_key=(os.getenv("HCAI-API_KEY")),
    server_url="https://ai.hackclub.com/proxy/v1",
)
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
# --------------------

@app.message(re.compile("woof|wruff|wooof", re.IGNORECASE))
def woof_reaction(message, client, say):
    print("Woof message detected")
    client.reactions_add(
        channel=message["channel"],
        timestamp=message["ts"],
        name=random.choice(emojis)
    )
    guess = random.randint(1, 3)
    thread_ts = message.get("thread_ts", message["ts"])
    if guess == 3:
        say(
                text="Here's a cute dog pic!",
                blocks=[
                    {
                        "type": "image",
                        "image_url": random.choice(dog_pics),
                        "alt_text": "Cute Dog"
                    },
                ],
                thread_ts=thread_ts
    )
    elif guess == 2:
        say(
            text="Woof!",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Woof!*"
                    }
                },
            ],
            thread_ts=thread_ts
        )
    else:
        pass

@app.message(re.compile("meow", re.IGNORECASE))
def meow_reaction(message, client, say):
    print("Meow message detected")
    client.reactions_add(
        channel=message["channel"],
        timestamp=message["ts"],
        name="neodog_evil"
    )
    thread_ts = message.get("thread_ts", message["ts"])
    say(
        text="i feel betrayed!",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*i feel betrayed!* :neodog_evil:."
                }
            },
        ],
        thread_ts=thread_ts
    )

@app.event("message")
def handle_other_messages():
    pass

@app.event("app_mention")
def handle_mention(event, say, client):
    print("Bot mentioned in message")
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
def woof_ideas_command(ack, say, respond):
    ack()
    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Got you! Generating a creative dog-related project idea now... :woofwoof:"
                }
            },
        ]
    )    
    print("Ideas command invoked & preview sent")
    response = client.chat.send(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "user", "content": "You are a AI Slack Bot, your only duty is to respond with SHORT one sentance creative project idea related to dogs and would take 5 hourse to code. Please do not use markdown formatting or any other formatting. Just respond with the idea."}
        ],
        stream=False,
    )
    print("Received response from OpenRouter: ", response.choices[0].message.content)
    idea_text = "Here's your idea: " + response.choices[0].message.content
    say(
        text=idea_text,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": idea_text
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
