import random
import time
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from selenium import webdriver

link = open('../links/算法工程师.txt', 'r', encoding='utf-8')
file = open('../data/算法工程师.txt', 'a', encoding='utf-8')
options = webdriver.EdgeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0')
driver = webdriver.Edge(options=options)


def func(line):
    driver.get(line)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(random.uniform(3, 5))
    text = soup.find('div', {'class': 'describtion__detail-content'}).get_text()
    file.write(text + '\n')


with ThreadPoolExecutor(5) as executor:
    for line in link:
        executor.submit(func, line)
