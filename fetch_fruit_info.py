import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


def aaa():
    # 啟動瀏覽器
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 不開視窗
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 打開網頁
        driver.get("https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx")
        WebDriverWait(driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        
        #
        date_text = driver.find_element(By.NAME, "ctl00$contentPlaceHolder$txtSTransDate")
        driver.execute_script("arguments[0].value = arguments[1];", date_text, "114/04/26")
        market_text = driver.find_element(By.NAME, "ctl00$contentPlaceHolder$txtMarket")
        driver.execute_script("arguments[0].value = arguments[1];", market_text, "全部市場")
        product_text = driver.find_element(By.NAME, "ctl00$contentPlaceHolder$txtProduct")
        driver.execute_script("arguments[0].value = arguments[1];", product_text, "全部")

        # 點擊「查詢」按鈕
        search_button = driver.find_element(By.NAME, "ctl00$contentPlaceHolder$btnQuery")
        search_button.click()

        # 等待資料表格出現
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_contentPlaceHolder_panel"))
        )
        time.sleep(2)

        # 取得網頁 HTML
        html = driver.page_source

        # 解析 HTML
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("div", id="ctl00_contentPlaceHolder_panel")
        rows = table.find_all("tr")

        # 把表格資料整理成 list
        data = []
        for row in rows:
            cells = row.find_all(["td", "th"])
            cell_text = [cell.get_text(strip=True) for cell in cells]
            data.append(cell_text)

        # 把資料存成 CSV
        with open("fruit_data.csv", mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("✅ 資料已經存成 fruit_data.csv！")

    finally:
        #driver.quit()
        pass

if __name__ == '__main__':
    aaa()