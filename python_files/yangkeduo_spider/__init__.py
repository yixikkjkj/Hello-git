import requests
import logging

logger = logging.getLogger(__name__)

def request_search_suggest(word):
    data = {
        'pdduid': 0,
        'query': word,
    }
    res = requests.get('http://yangkeduo.com/proxy/api/search_suggest', data)
    ret = res.json()
    if res.status_code != 200:
        raise ValueError('yangkeduo request %s'%(ret['error']))
    ret = res.json()
    logger.info('request return ')
    return ret['suggest']


if __name__ == "__main__":
    word = '栏杆'
    request_search_suggest(word)
