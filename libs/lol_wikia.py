import requests
import traceback


def get_quotes(article_id):
    try:
        get_article_url = "http://leagueoflegends.wikia.com/api/v1/Articles/AsSimpleJson?id={}".format(article_id)
        quotes_request = requests.get(get_article_url)
        quotes = quotes_request.json()
        quote_sections = quotes['sections']
        champ_name = quote_sections[0]['title'].split("/")[0]
        quote_list = []

        for quote in quote_sections:
            if quote['title'] != "Laugh" and "Quotes" not in quote['title']:
                for content in quote['content']:
                    for element in content['elements']:
                        target_quote = element['text']
                        quote_list.append(target_quote)
        print(champ_name)
        return champ_name, quote_list

    except:
        print(traceback.format_exc())
        print(quotes_request.status_code)


def get_quote_articles():
    champion_quote_list = "http://leagueoflegends.wikia.com/api/v1/Articles/List?expand=1&category=Champion+quotes&limit=250"
    champion_quote_json = requests.get(champion_quote_list).json()['items']
    return champion_quote_json


def get_all_quotes():
    try:
        all_quotes = {}
        quote_articles = get_quote_articles()
        for article in quote_articles:
            try:
                quotes = get_quotes(article['id'])
                all_quotes[quotes[0]] = quotes[1]
            except:
                print(traceback.format_exc())

        return all_quotes

    except KeyboardInterrupt:
        raise

    except:
        print(traceback.format_exc())

