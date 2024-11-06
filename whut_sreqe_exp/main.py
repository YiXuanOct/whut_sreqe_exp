import random
import time
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0')
driver = webdriver.Edge(options=options)
driver.get(f"https://www.zhaopin.com/sou/jl763/kwFEBMPLATSLT0MNG8/p1")
time.sleep(30)
cookies = driver.get_cookies()
file = open("../links/算法工程师.txt", "a", encoding="utf-8")
cities = {'538': 31, '763': 13, '765': 37, '736': 15}


def func(city, index):
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(f"https://www.zhaopin.com/sou/jl{city}/kwFEBMPLATSLT0MNG8/p{index}")
    time.sleep(random.uniform(3, 5))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    hrefs = soup.find_all('a', {'class': 'jobinfo__name'})
    for href in hrefs:
        file.write(href['href'] + '\n')


with ThreadPoolExecutor(5) as executor:
    for city, page in cities.items():
        for i in range(1, page + 1):
            executor.submit(func, city, i)
