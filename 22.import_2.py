# -*- coding: utf-8 -*-
from datetime import datetime

# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup


def get_train_fare(start_station, end_station):
    t = datetime.now()
    year = t.year
    month = t.month
    day = t.day
    hour = t.hour
    minute = f'{t.minute:02d}'
    url = \
        f"https://transit.yahoo.co.jp/" \
        f"search/result?" \
        f"from={start_station}" \
        f"&to={end_station}" \
        f"&fromgid=&togid=&flatlon=&tlatlon=&via=&viacode=" \
        f"&y={year:04d}" \
        f"&m={month:02d}" \
        f"&d={day:02d}" \
        f"&hh={hour:02d}" \
        f"&m1={minute[0]}" \
        f"&m2={minute[1]}" \
        f"&type=1&ticket=ic&expkind=1&userpass=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return int(soup.select('.fare')[0].select('em')[0].text[:-1])


start_station = '五反田駅'
end_station = '四ツ谷駅'

fare = get_train_fare(start_station, end_station)

print(f'{start_station}から{end_station}までの運賃は{fare}円です！')
# 五反田駅から四ツ谷駅までの運賃は178円です！
