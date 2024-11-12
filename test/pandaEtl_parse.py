import pandas as pd
import json

# 原始資料
data = [
    [
        "專業證照、政府/考試名稱",
        "認證單位",
        "認證年月",
        "證書"
    ],
    [
        "Certification 1",
        "systex",
        "2024/12/31",
        "■有 □無"
    ],
    [
        "Certification 2",
        "systex",
        "2024/01/01",
        "■有 □無"
    ],
    [
        "",
        "",
        "",
        "□有 □無"
    ]
]

# 將資料轉換成結構化的 DataFrame
columns = data[0]  # 使用第一行作為標題
records = data[1:]  # 去除標題行的實際數據
df = pd.DataFrame(records, columns=columns)

# 清理資料並轉換格式
def parse_certification_status(status_text):
    return "有" if "■有" in status_text else ""

# 應用轉換函數
df["證書"] = df["證書"].apply(parse_certification_status)
# df.replace("", pd.NA, inplace=True)

print(df)

# 將 DataFrame 轉換成指定的 JSON 格式
json_result = []
# for _, row in df.iterrows():
#     row_data = []
#     for col_name, value in row.items():
#         # if pd.notna(value):  # 避免加入 NaN 值
#         row_data.append({"key": col_name, "value": value})
#     json_result.append(row_data)


# # 輸出 JSON
# json_output = json.dumps(json_result, ensure_ascii=False, indent=4)
# print(json_output)

# 構建最終的 JSON 結構
# 準備轉換成 JSON 的結構
table_index = 1  # 假設這是目前的表格索引
result = {
    str(table_index): {
        "head": columns,  # 假設您只想要 "證書" 和 "認證單位"
        "data": df[columns].values.tolist()  # 轉換為 list 格式
    }
}

# 輸出結果轉為 JSON 格式
json_result = json.dumps(result, ensure_ascii=False, indent=4)

print(json_result)
