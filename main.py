import os
import discord
import pandas as pd
from ta.momentum import RSIIndicator
from pybit.unified_trading import HTTP
from dotenv import load_dotenv


load_dotenv()


class SpotKLineDataHandler:
    session = HTTP(
        testnet=False,
        api_key=os.getenv("BYBIT_API_KEY"),
        api_secret=os.getenv("BYBIT_API_SECRET_KEY"),
    )
    data = session.get_kline(
        category="spot",
        symbol="SOLUSDT",
        interval=60,
    )

    def fetch_data(self):
        result = self.data["result"]["list"]
        df = pd.DataFrame(
            result,
            columns=[
                "start_time",
                "open_price",
                "high_price",
                "low_price",
                "close_price",
                "volume",
                "turnover",
            ],
        )

        close_price = df["close_price"].astype(float)
        return close_price

    def calculate_rsi(self):
        data_to_calc = self.fetch_data()
        rsi = RSIIndicator(data_to_calc, window=14).rsi()
        latest_rsi = rsi.iloc[-1]
        return latest_rsi


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"logged in as {self.user}")
        await self.monitor_rsi()

    async def monitor_rsi(self):
        await self.wait_until_ready()

        channel = self.get_channel(int(os.getenv("CHANNEL_ID")))

        while not self.is_closed():
            latest_rsi = SpotKLineDataHandler().calculate_rsi()

            if latest_rsi > 70:
                await channel.send(f"RSI Alert: Overbought! - RSI = {latest_rsi:.2f}")
            elif latest_rsi < 30:
                await channel.send(f"RSI Alert: Oversold! - RSI = {latest_rsi:.2f}")


def main():
    client = MyClient(intents=discord.Intents.all())
    client.run(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    main()
