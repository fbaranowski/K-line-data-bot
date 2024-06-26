# K-line-data-bot
This Python script fetches K-line data from Bybit API, calculates
RSI based on this data. If RSI score is below 30 or above 70, the
script sends an alert on a given discord channel through bot.

## Tech stack
- Python 3.12
- Pipenv
- Discord.py
- ta (Technical Analysis Library)
- Pandas
- Pybit
- Python-dotenv

## Installation

It is necessary to have Docker installed
on your local machine, as well as have Discord and Bybit accounts.

Moreover, it is essential to have api key and secret key for Bybit API
and Discord bot token and Discord channel ID on which this bot can
operate.

Then, using cmd, clone the repository from GitHub:

`git clone https://github.com/fbaranowski/K-line-data-bot`

Now, create `.env` file in directory, where `main.py` file is
and write necessary variables:

`BOT_TOKEN=<your_discord_bot_token>`

`CHANNEL_ID=<discord_channel_id>`

`BYBIT_API_KEY=<your_bybit_api_key>`

`BYBIT_API_SECRET_KEY=<your_bybit_api_secret_key>`

Finally, being in the directory, where `docker-compose.yml` file is
type in cmd `docker-compose up --build` to start the app.
