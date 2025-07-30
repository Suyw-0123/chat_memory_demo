from db import init_db, insert_message, get_history

# 初始化資料庫
init_db()

# 插入幾筆測試資料
insert_message("Alice", "你是誰？", "我是 ChatGPT")
insert_message("Bob", "今天天氣如何？", "今天很晴朗")

# 查詢歷史紀錄
history = get_history()
for row in history:
    print(row)
