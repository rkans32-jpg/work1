from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import time

base_url = "https://www.fsc.go.kr/no010102"
data = []

# Selenium 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 1~10페이지 반복
for page in range(1, 11):
    url = f"{base_url}?page={page}"
    driver.get(url)
    time.sleep(2.5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # 부모 ul selector로 접근
    ul = soup.select_one("#container > div.content-body > div > div.board-list-wrap > ul")
    if not ul:
        print(f"{page}페이지에서 리스트를 찾지 못했습니다.")
        continue

    items = ul.select("li")  # ul 하위 li 모두 선택

    for item in items:
        a_tag = item.select_one("div.cont > div.subject > a")
        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = urljoin(base_url, a_tag.get("href"))

        date_tag = item.select_one("div.other-info > span.date")
        date = date_tag.get_text(strip=True) if date_tag else "날짜없음"

        data.append({
            "날짜": date,
            "제목": title,
            "링크": link
        })

    print(f"{page}페이지 완료")

driver.quit()

df = pd.DataFrame(data)

if not df.empty:
    df.to_excel("금융위_보도자료_스크래핑.xlsx", index=False)
    print("📁 '금융위_보도자료_스크래핑.xlsx' 저장 완료")
else:
    print("❗ 수집된 데이터가 없어 엑셀로 저장하지 않았습니다.")
