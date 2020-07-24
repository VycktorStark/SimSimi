## Getting Started

This is a project that will use the simsimi API to create a chatterbot on the telegram to chat with other users, which can be used for testing purposes.

Below, I am providing instructions for you to have a copy of the project. These instructions will show you how to start using it for learning, development and testing purposes.

## Configuring the bot to run on the terminal
You must have your machine up to date and have Python 3 installed, as well as some modules, such as: flask and requests, if you don't have it, you will need to install it this way here:
```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2
$ sudo apt-get update && sudo apt-get upgrade   
$ sudo apt install python3 && python3-pip
$ sudo pip3 install flask && requests
```
With everything installed, we will clone the repository like this:

```
$ git clone https://github.com/VycktorStark/SimSimi.git
```

With the repository installed, you must have the bot token created by [BotFather](http://telegram.me/BotFather); if you don't have one, you'll need to create one (more information on [official robot FAQ page](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get ))

To add your token to the project, I advise you to configure your ".bashrc", putting something like:
```
export LN="en"
export SECRET_KEY="12918981:dFwnfweFw2oju28ru239r8389iEJOIJO"
export SECRET_KEY_SIMSIMI="dFw1weFs212w8r2u239r813JO9"
```

Or just configure the `tools.py`, To obtain a simsimi token key to use this project, visit [developer.simsimi.com](http://developer.simsimi.com/signUp), where you will find all instructions
Note: this API is paid according to usage, and the free version can be used for the period of time established; see this information directly on the [website](http://developer.simsimi.com/pricing)

## Boot process

- To start the bot, run: sudo ./main.py
- To stop the bot, press Ctrl + C.
You can also start the bot with python3 main.py


## Configuring the bot to run on heroku

Click the button below and configure your language, also setting your bot's token.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Only that, the project will already be working.
