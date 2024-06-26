import os
import discord
from data_fetcher import SpotKLineDataHandler


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"logged in as {self.user}")
        await self.monitor_rsi()

    async def monitor_rsi(self):
        await self.wait_until_ready()

        channel = self.get_channel(int(os.environ.get("CHANNEL_ID")))

        while not self.is_closed():
            latest_rsi = SpotKLineDataHandler().calculate_rsi()

            if latest_rsi > 70:
                await channel.send(f"RSI Alert: Overbought! - RSI = {latest_rsi:.2f}")
            elif latest_rsi < 30:
                await channel.send(f"RSI Alert: Oversold! - RSI = {latest_rsi:.2f}")
