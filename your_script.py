from datetime import datetime

file_path = "data.txt"

with open(file_path, "w") as f:
    f.write(f"更新時間：{datetime.now()} UTC\n")
