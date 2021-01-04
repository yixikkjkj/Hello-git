
import requests
requests.packages.urllib3.disable_warnings()
headers = {

    #
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
}
headers2 = {
    #"Host":"music.liuzhijin.cn",
    "Host": "live.kuaishou.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Cookie": "did=web_c0f3196ec94d4837b5f7850e3ebac3b9; didv=1589520098000; clientid=3; client_key=65890b29",
}
def geturl(url0):
    #url0="https://v.kuaishou.com/5loz4u"
    res0 = requests.get(url0,headers=headers,verify=False)
    """转接第二段"""

    cookie = res0.cookies.get_dict()
    cookie = str(cookie).replace("{","").replace("}","").replace(" ","").replace("'","").replace(",",";")

    headers3 ={
            "Host": "v.kuaishou.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Cookie":cookie.replace(":","=")
            }

    headers4 ={
            "Host": "live.kuaishou.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Cookie":cookie.replace(":","=")
            }
    res1 = requests.get(url0,headers=headers3,allow_redirects=False)
    url2 = res1.headers['Location']

    url_00 = url2.split("userId=")[1].split("&")[0]


    """第一部分url"""
    url_0=url2.split("?")[0].split("/")[-1]
    res2 = requests.get(url2,headers=headers3,allow_redirects=False).request.headers

    """第二部分url"""
    url_1 = res2['Cookie'].split(";")[-1].replace(":","=")

    """完整url"""
    url = "https://live.kuaishou.com/u/"+url_00+"/"+url_0+"?"+url_1
    #print(url)

    response  = requests.get(url,headers=headers4)
    text = response.text

    """视频链接"""
    print(text)
    with open('/Users/wangyijun/Hello-git/python_files/yangkeduo_spider/yyyy.html', 'w+') as file_obj:
        file_obj.write(text)

    v_url =text.split('"playUrl":"')[1].split(".mp4")[0]+".mp4"
    v_url = v_url.replace("u002F","")
    #print(v_url)
    return v_url


st="陪伴是最常情的告白，守护是最沉默的陪伴…… #汪星人 #宠物避障挑战 https://v.kuaishou.com/5xXNiL 复制此链接，打开【快手App】直接观看！"
st ="http"+(st.split("复制")[0].split("http")[1].replace(" ",""))
u = geturl(st)
print(u)


a = '_did=web_742578326A0C7438; didv=1608278796021; kuaishou.web.cp.api_st=ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqABcxLt1W3vCv1T738tYUdsF_BkgnEtKFjJHeI7z9CPlV-gPTXZPi0csT9BmCn70Q1R-RLxgqwwPqqUecNoU1l-aByZmVSWwpOXTXiE9RG5_DujDFNcHzN7ceDvocIBbi5s1HOZxGrnNCur9ejPKF27vpCxYMzHa8Wug49DM-QpxmAD2OJIovN78wSAZEvoVxDzED6oRx06hInKaIe0irH_rBoSDGYhfNsTRxfgoBAzOBOtdbfDIiCKvQ15bO-T53TZieTbH4EF72oASNH8Ds5J7EkvZboqNSgFMAE; kuaishou.web.cp.api_ph=7f250dd3b58631e2584bc2313271559f8d13; clientid=3; did=web_bca2bffd6baaf5172f7ec7b335165045; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1608278793,1608278801; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1609140268; kpf=PC_WEB; kpn=KUAISHOU_VISION; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABpOCsw78BzdUSfMRH6slCY4CLi22upeqWagBRQZ20z-suZgJQniwCgyocLn7WQNA2syfuF_SaRIqYeRjXq2mYKgqGQdS1mrddx6mqabVZUvIVUCiGXsxFxusRFCHSPwyqPfHRHZHvY4wc3iJt9hdF02zARHSgHpv0uPIGnanPQzN-DBlBbmrzL5NBOnOv3BKFCkHkmRfw0QDN2eQvMb9r8BoSnIqSq99L0mk4jolsseGdcwiNIiDSPPumCFkpiFhh2TIhMqE0rBr_KvIFxkoCge6z-xuUJSgFMAE; kuaishou.server.web_ph=ea604d0ae1c91daa597fdddd3f620dcac043'
c = '_did=web_742578326A0C7438; didv=1608278796021; kuaishou.web.cp.api_st=ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqABcxLt1W3vCv1T738tYUdsF_BkgnEtKFjJHeI7z9CPlV-gPTXZPi0csT9BmCn70Q1R-RLxgqwwPqqUecNoU1l-aByZmVSWwpOXTXiE9RG5_DujDFNcHzN7ceDvocIBbi5s1HOZxGrnNCur9ejPKF27vpCxYMzHa8Wug49DM-QpxmAD2OJIovN78wSAZEvoVxDzED6oRx06hInKaIe0irH_rBoSDGYhfNsTRxfgoBAzOBOtdbfDIiCKvQ15bO-T53TZieTbH4EF72oASNH8Ds5J7EkvZboqNSgFMAE; kuaishou.web.cp.api_ph=7f250dd3b58631e2584bc2313271559f8d13; clientid=3; did=web_bca2bffd6baaf5172f7ec7b335165045; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1608278793,1608278801; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1609140268; kpf=PC_WEB; kpn=KUAISHOU_VISION; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABpOCsw78BzdUSfMRH6slCY4CLi22upeqWagBRQZ20z-suZgJQniwCgyocLn7WQNA2syfuF_SaRIqYeRjXq2mYKgqGQdS1mrddx6mqabVZUvIVUCiGXsxFxusRFCHSPwyqPfHRHZHvY4wc3iJt9hdF02zARHSgHpv0uPIGnanPQzN-DBlBbmrzL5NBOnOv3BKFCkHkmRfw0QDN2eQvMb9r8BoSnIqSq99L0mk4jolsseGdcwiNIiDSPPumCFkpiFhh2TIhMqE0rBr_KvIFxkoCge6z-xuUJSgFMAE; kuaishou.server.web_ph=ea604d0ae1c91daa597fdddd3f620dcac043'

for index, data in enumerate(d):
    if data != b[index]:
        print(data)
        print(b[index])

for data in b:
    eq = data.index('=')
    print("'"+ data[:eq] +"':", "'" +data[eq+1:]+"',")

cookies = {
    '_did': 'web_742578326A0C7438',
    'didv': '1608278796021',
    'kuaishou.web.cp.api_st': 'ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqABcxLt1W3vCv1T738tYUdsF_BkgnEtKFjJHeI7z9CPlV-gPTXZPi0csT9BmCn70Q1R-RLxgqwwPqqUecNoU1l-aByZmVSWwpOXTXiE9RG5_DujDFNcHzN7ceDvocIBbi5s1HOZxGrnNCur9ejPKF27vpCxYMzHa8Wug49DM-QpxmAD2OJIovN78wSAZEvoVxDzED6oRx06hInKaIe0irH_rBoSDGYhfNsTRxfgoBAzOBOtdbfDIiCKvQ15bO-T53TZieTbH4EF72oASNH8Ds5J7EkvZboqNSgFMAE',
    'kuaishou.web.cp.api_ph': '7f250dd3b58631e2584bc2313271559f8d13',
    'clientid': '3',
    'did': 'web_bca2bffd6baaf5172f7ec7b335165045',
    'client_key': '65890b29',
    'Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1608278793,1608278801',
    'Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1609140268',
    'kpf': 'PC_WEB',
    'kpn': 'KUAISHOU_VISION',
    'kuaishou.server.web_st': 'ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABpOCsw78BzdUSfMRH6slCY4CLi22upeqWagBRQZ20z-suZgJQniwCgyocLn7WQNA2syfuF_SaRIqYeRjXq2mYKgqGQdS1mrddx6mqabVZUvIVUCiGXsxFxusRFCHSPwyqPfHRHZHvY4wc3iJt9hdF02zARHSgHpv0uPIGnanPQzN-DBlBbmrzL5NBOnOv3BKFCkHkmRfw0QDN2eQvMb9r8BoSnIqSq99L0mk4jolsseGdcwiNIiDSPPumCFkpiFhh2TIhMqE0rBr_KvIFxkoCge6z-xuUJSgFMAE',
    'kuaishou.server.web_ph': 'ea604d0ae1c91daa597fdddd3f620dcac043',
}
data = {
    'operatonName': 'recoDataQuery',
    'query': """fragment feedContent on Feed {
  type
  author {
    id
    name
    headerUrl
    following
    headerUrls {
      url
      __typename
    }
    __typename
  }
  photo {
    id
    duration
    caption
    likeCount
    realLikeCount
    coverUrl
    photoUrl
    coverUrls {
      url
      __typename
    }
    timestamp
    expTag
    __typename
  }
  canAddComment
  llsid
  status
  currentPcursor
  __typename
}

fragment photoResult on PhotoResult {
  result
  llsid
  expTag
  serverExpTag
  pcursor
  feeds {
    ...feedContent
    __typename
  }
  __typename
}

query recoDataQuery($pcursor: String, $semKeyword: String, $semCrowd: String, $utmSource: String, $utmMedium: String, $page: String) {
  recoData(tabId: 0, pcursor: $pcursor, semKeyword: $semKeyword, semCrowd: $semCrowd, utmSource: $utmSource, utmMedium: $utmMedium, page: $page) {
    ...photoResult
    __typename
  }
}
""",
    'variables': {
        'page': 'homepage',
        'pcursor': "2",
    },
}

res = requests.post('https://video.kuaishou.com/graphql', data, cookies=cookies)
