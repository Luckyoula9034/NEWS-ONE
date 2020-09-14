from app import app
import urllib.request,json
from models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news_sources(news_results_list)

    return news_results

def process_news_sources(news_sources) :

    results_list=[]

    for news_source in news_sources:
          id=news_source.get("id")
          name=news_source.get("name")
          description=news_source.get("description")
          url=news_source.get("url")
          category=news_source.get('category')


          new_source =News(id,name,description,url,category)

          results_list.append(new_source)     
    return results_list            