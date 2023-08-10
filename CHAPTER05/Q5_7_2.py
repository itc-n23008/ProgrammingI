# 表データの生成
data = [
    ["0001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["0002", "male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["0003", "Female", "Tanaka", "Yuko", 25, "Saitama"],
    ["0004", "Male", "Suzuki", "Ichirou", 35, "Hokkaido"],
]
print(data)

# 辞書変数生成
member_information = {}

# 表データをレコード毎に格納する
for record in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info
