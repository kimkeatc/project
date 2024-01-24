
# -*- coding: utf-8 -*-

import requests


class Malaysia4DResult:

    def __init__(self):
        self.url = f"https://ajax01.4d88.asia/ajax/G1.json"
        self.result = self.send_request(self.url)

    @staticmethod
    def send_request(url):
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data

    def magnum_4d(self):
        return self.result["P1"]["4D"]

    def magnum_life(self):
        return self.result["P1"]["LF"]

    def magnum_gold(self):
        return self.result["P1"]["GLD"]

    def magnum_dd(self):
        return self.result["P1"]["DD"]

    def magnum_dd(self):
        return self.result["P1"]["DN"]
    
    def toto_6d(self):
        return self.result["P2"]["6D"]

    def toto_5d(self):
        return self.result["P2"]["5D"]

    def toto_4d(self):
        return self.result["P2"]["4D"]

    def toto_supreme_58(self):
        return self.result["P2"]["SPM"]

    def toto_power_55(self):
        return self.result["P2"]["PWR"]

    def toto_star_50(self):
        return self.result["P2"]["STR"]

    def dmc_4d(self):
        return self.result["P3"]["4D"]

    def dmc_3p3d(self):
        return self.result["P3"]["3P3D"]

'''
# Magnum
https://app-apdapi-prod-southeastasia-01.azurewebsites.net/draw-dates/available-for-year

https://app-apdapi-prod-southeastasia-01.azurewebsites.net/results/past/between-dates/01-12-1985/11-12-1985/9
https://app-apdapi-prod-southeastasia-01.azurewebsites.net/results/past/between-dates/05-12-1985/15-12-1985/9
https://app-apdapi-prod-southeastasia-01.azurewebsites.net/results/past/between-dates/07-12-1985/17-12-1985/9
https://app-apdapi-prod-southeastasia-01.azurewebsites.net/results/past/between-dates/13-01-2024/23-01-2024/9
https://app-apdapi-prod-southeastasia-01.azurewebsites.net/results/past/latest-before/14-01-2024/9

'''
