<img width="500" height="auto" alt="WoofBot Banner" src="https://github.com/user-attachments/assets/6997cca0-830f-4a5d-94a4-da67eb7cfe39" />

## 🐶 WoofBot
This is a Slack Bot for the YSWS Woof!

You can have a look at our website [here](https://woof.hackclub.com)

This project is being submitted to [Flavortown](flavortown.hackclub.com)

![](https://hackatime-badge.hackclub.com/U078VN0UU2K/woof-bot)

> [!NOTE]
> This is not currently being hosted! 😢

### Features

- 🐕 Reacts with a random emoji (from list) and has a 1 in 3 chance of either: replying in thread, sending a dog pic in thread or passing when user types 'woof' in channel 
- ```/woofpics``` sends a picture of a communinity members dog (powered by ```#cdn``` 😁)
- 🧠 ```/idea``` uses [Hack Club AI](ai.hackclub.com) to generate a idea for a dog themed project
- 🐩 ```/woof```
- 🦴 ```@woofBot``` reacts to message and sends dog image in thread
- 😾 Reacts with ```:neocat_evil``` (_hc slack exclusive_) and sends message in thread when 'meow' is typed in chat

### Try it out

The Slack Channel is over [here (#woofbot-spam)](https://hackclub.enterprise.slack.com/archives/C0A5XDSUZV3) 

_only avalible to members of Hack Club!_

### Install
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
_if having issues then manually install the packages_

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
