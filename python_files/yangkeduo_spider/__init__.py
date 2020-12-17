import requests

request_url = 'https://yangkeduo.com/goods.html?goods_id=192732208869'
data = {'goods_id': 192732208869}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'api_uid=CkhYD1+zgog34gBUXQYxAg==; _nano_fp=XpEonpEonpU8n5TqX9_HseJlBjJn9vEQW0TSRWjR; ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F87.0.4280.88%20Safari%2F537.36%20Edg%2F87.0.664.60; webp=1; chat_list_rec_list=chat_list_rec_list_dDyAI3; msec=1800000; JSESSIONID=DF8ACF1879A6F801A99B3AA46064ECAF; rec_list_personal=rec_list_personal_0dn7t6; pdd_vds=gaLfNdGDObnBtDGltxmbmuGwNBtdmNPmysPxLfynIdQsmsNdydElEeLDmmiu',
    'Host': 'yangkeduo.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
}
res = requests.get(request_url, data, headers=headers)

primiary_url = 'https://yangkeduo.com'
res = requests.get(primiary_url)

def request_search_suggest(word):
    data = {
        'goods_id': 192732208869
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
