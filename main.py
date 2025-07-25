from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

search_word = sys.argv[1]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# connect to naver
driver.get("https://www.naver.com")

# select search tab
search_box = driver.find_element(By.CSS_SELECTOR, "input#query")

# input search what you wants (input parameter when script run)
search_box.send_keys(search_word)

# enter the search input
search_box.send_keys(Keys.ENTER)

# click news tab
time.sleep(2)  # waiting for page changing
news_tab = driver.find_element(By.LINK_TEXT, "뉴스")
news_tab.click()

time.sleep(2)  # waiting for news page loading

from bs4 import BeautifulSoup

# get current page HTML
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

# select span tag in news title
title_spans = soup.select("span.sds-comps-text-type-headline1")

print(f"총 {len(title_spans)}개의 뉴스 제목을 찾았습니다.\n")

for i, title_span in enumerate(title_spans, 1):
    print(f"{i}. {title_span.get_text(strip=True)}")

driver.quit()