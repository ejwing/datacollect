import requests
import json
from datetime import date

url = "https://data.moa.gov.tw/api/v1/AgriProductsTransType"  # 政府蔬果價格 API 範例
params = {
    # "Start_time": date.today().strftime("%Y-%m-%d"),
    # "End_time": date.today().strftime("%Y-%m-%d")
    "Start_time": "114.03.01",
    "End_time": "114.03.10"
}

response = requests.get(url, params=params)
data = response.json()

# 過濾部分欄位
# filtered = [
#     {
#         "交易日期": item["TransDate"],
#         "品名": item["CropName"],
#         "平均價": item["Avg_Price"],
#         "市場": item["MarketName"]
#     }
#     for item in data.get("Data", [])
# ]

# 儲存 JSON
with open("price.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
