<img width="400" height="auto" alt="woof_ysws_logo" src="https://github.com/user-attachments/assets/45f89700-0b65-45a2-a2f5-f74908c68747" />

## 🐶 WoofBot
This is a Slack Bot for the YSWS Woof!

You can have a look at our website [here](https://woof.hackclub.com)

### ⭐ Features

- 🐕 Reacts with a random emoji (from list) when user types 'woof' in channel
- ```/woofpics``` sends a picture of a communinity members dog (powered by ```#cdn``` 😁)
- 🧠 ```/idea``` uses [Hack Club AI](ai.hackclub.com) to generate a idea for a dog themed project
- 🐩 ```/woof```
- 🦴 ```@woofBot``` reacts to message and sends dog image in thread

### 🧪 Try it out

The Slack Channel is over [here (#woofbot-spam)](https://hackclub.enterprise.slack.com/archives/C0A5XDSUZV3) _only avalible to members of Hack Club!_

### 👷‍♂️ Install
_make sure ```git``` is installed on your device_

- Clone the Repo
``` 
git clone https://github.com/hippogriff101/woof-bot
```
- Install dependencies

1. Make a virtual environment:
```
python -m venv .venv
```
2. Activate the ```.venv```
```
# on macOS and Linux
source .venv/bin/activate
# on windows
.\venv\Scripts\activate.bat
```
3. Install
```
pip install -r requirements.txt
```
- Make a ```.env``` _(demo ```.env``` will me made soon)_

_make sure to never commit private variables_

You need:
```
SLACK_BOT_TOKEN=
HCAI-API_KEY=
SLACK_APP_TOKEN=
```

- Install to channel on Slack
- Run Script
```
python socketmd.py
```
- WOOF 🐶
