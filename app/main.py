import os
import discord
from discord_client import MyClient


def main():
    client = MyClient(intents=discord.Intents.all())
    client.run(os.environ.get("BOT_TOKEN"))


if __name__ == "__main__":
    main()
