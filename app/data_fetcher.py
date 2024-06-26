import os
import pandas as pd
from ta.momentum import RSIIndicator
from pybit.unified_trading import HTTP


class SpotKLineDataHandler:
    session = HTTP(
        testnet=False,
        api_key=os.environ.get("BYBIT_API_KEY"),
        api_secret=os.environ.get("BYBIT_API_SECRET_KEY"),
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
