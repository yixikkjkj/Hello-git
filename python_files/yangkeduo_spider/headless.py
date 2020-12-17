from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')

browser = webdriver.Chrome(chrome_options=options)

browser.get('https://ads.huhuguanjia.com')
ele = browser.find_element_by_link_text('进入软件')
eles = browser.find_elements_by_tag_name('a')
eles[0]

