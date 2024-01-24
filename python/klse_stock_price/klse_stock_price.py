
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import requests
import pandas
import pytz

_datetime_now = datetime.now()

timestamp_year1970_january_1 = int(datetime(1970, 1, 1, 0, 0, 0, 0, pytz.utc).timestamp())  # 0
timestamp_year2000_january_1 = int(datetime(2000, 1, 1, 0, 0, 0, 0, pytz.utc).timestamp())  # 946684800

timestamp_today = int(datetime(_datetime_now.year, _datetime_now.month, _datetime_now.day, 0, 0, 0, 0, pytz.utc).timestamp())
timestamp_tomorrow = timestamp_today + (24 * 60 * 60)
timestamp_yesterday = timestamp_today - (24 * 60 * 60)
timestamp_last_week = timestamp_today - (7 * 24 * 60 * 60)


class Miscellaneous:

    def __init__(self):
        pass

    def generate_request_header(
            self,
            user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
            ) -> dict:

        headers = {
            "User-Agent": user_agent,
        }
        return headers

    def update_data(self, t: list = [], o: list = [], h: list = [], l: list = [], c: list = [], v: list = []):
        data = {
            "timestamp": t,
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": v,
        }
        return data

    def send_request(self, url: str) -> pandas.DataFrame:

        data = self.update_data()
        dataframe = pandas.DataFrame(data)

        response = requests.get(url=url, headers=self.generate_request_header())
        response.raise_for_status()

        d = response.json()

        _ = d["s"]  # status
        _ = d["count"]  # count
        _ = d["from"]  # start
        _ = d["to"]  # end

        data = self.update_data(d["t"], d["o"], d["h"], d["l"], d["c"], d["v"])
        dataframe = pandas.DataFrame(data)

        dataframe.insert(1, "date", pandas.to_datetime(dataframe["timestamp"], unit="s"))
        if "resolution=1D" not in url:
            dataframe["date"] = dataframe["date"] + timedelta(hours=8)

        dataframe.sort_values(by=["timestamp"], inplace=True)
        dataframe.reset_index(drop=True, inplace=True)
        return dataframe


class Stock(Miscellaneous):

    def __init__(self, code: str):
        super().__init__()
        self.code = code

    def generate_url(self, resolution: str, start: int = None, end: int = timestamp_tomorrow, countback: int = None):
        if start is None:
            start = timestamp_year1970_january_1
        if end is None:
            end = timestamp_tomorrow
        url = f"https://www.klsescreener.com/v2/trading_view/history?symbol={self.code}&resolution={resolution}&from={start}&to={end}&currency=MYR"
        if countback is not None:
            url = f"{url}&countback={countback}"
        return url

    def get_daily(self, start=None, end=None, countback=None, *, resolution="1D"):
        url = self.generate_url(resolution, start, end, countback)
        dataframe = self.send_request(url)
        return dataframe

    def get_1hour(self, start=None, end=None, countback=None, *, resolution="60"):
        url = self.generate_url(resolution, start, end, countback)
        dataframe = self.send_request(url)
        return dataframe

    def get_30minutes(self, start=None, end=None, countback=None, *, resolution="30"):
        url = self.generate_url(resolution, start, end, countback)
        dataframe = self.send_request(url)
        return dataframe

    def get_15minutes(self, start=None, end=None, countback=None, *, resolution="15"):
        url = self.generate_url(resolution, start, end, countback)
        dataframe = self.send_request(url)
        return dataframe

    def get_5mintues(self, start=None, end=None, countback=None, *, resolution="5"):
        url = self.generate_url(resolution, start, end, countback)
        dataframe = self.send_request(url)
        return dataframe

    def get_60seconds(self, start=None, end=None, countback=None, *, resolution="1"):
        url = self.generate_url(resolution, start, end, countback)
        dataframe = self.send_request(url)
        return dataframe
