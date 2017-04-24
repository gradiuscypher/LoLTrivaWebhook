import requests


def get_quotes(article_id):
    get_article_url = "http://leagueoflegends.wikia.com/api/v1/Articles/AsSimpleJson?id={}".format(article_id)
    quotes = requests.get(get_article_url).json()
    quote_sections = quotes['sections']

    for quote in quote_sections:
        if quote['title'] != "Laugh" and "Quotes" not in quote['title']:
            for content in quote['content']:
                for element in content['elements']:
                    target_quote = element['text']


def get_quote_articles():
    champion_quote_list = "http://leagueoflegends.wikia.com/api/v1/Articles/List?expand=1&category=Champion+quotes&limit=250"
    champion_quote_json = requests.get(champion_quote_list).json()['items']


def get_all_quotes():
    pass
