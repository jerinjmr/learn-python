"""Fetch stock calls and market news."""
import requests
from bs4 import BeautifulSoup
# import pprint

res1 = requests.get('https://www.moneycontrol.com/news/business/stocks/')
res2 = requests.get('https://www.moneycontrol.com/news/business/stocks/page-2')
soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# heads up! .storylink changed to .titlelink
link1 = soup1.select('#cagetory')
link2 = soup2.select('#cagetory')
links = link1 + link2


def fetch_buy_calls(links):
    """Fetch market feeds."""
    calls = []
    for item in links:
        level1 = item.select('.clearfix')
        for element in level1:
            # sub_element = element.h2
            level2 = element.a
            calls.append(level2.get('title'))
    return calls


# pprint.pprint
calls = fetch_buy_calls(links)
for call in calls:
    print(call)
