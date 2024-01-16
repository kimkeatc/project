
# -*- coding: utf-8 -*-

import requests
import pandas


def generate_request_header(
        user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        ) -> dict:

    headers = {
        "User-Agent": user_agent,
    }

    return headers


def get_stock_screener(url: str = "https://www.klsescreener.com/v2/screener/quote_results") -> pandas.DataFrame:

    headers = generate_request_header()

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    dataframe = pandas.read_html(response.text)
    dataframe = dataframe[0]

    return dataframe


def get_warrant_screener(url: str = "https://www.klsescreener.com/v2/screener_warrants/quote_results") -> pandas.DataFrame:

    headers = generate_request_header()

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    dataframe = pandas.read_html(response.text)
    dataframe = dataframe[0]

    return dataframe
