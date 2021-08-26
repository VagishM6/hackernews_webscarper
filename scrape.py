import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_news_by_votes(news_info):
    return sorted(news_info, key= lambda k:k['votes'], reverse=True)


def get_news_info(links, subtext):
    for index, item in enumerate(links):
        news_info = []

        for index, item in enumerate(links):
            title = links[index].getText()
            href = links[index].get('href', None)
            vote = subtext[index].select('.score')

            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                
                if points > 99:
                    news_info.append({'title': title, 'href': href, 'votes': points})

        return sort_news_by_votes(news_info)


pprint.pprint(get_news_info(links, subtext))
