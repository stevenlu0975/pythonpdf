from typing import List, Dict, Union,Annotated
from enum import Enum
from notUse.Pojos import *


# 假設有不同的表格 mapping 函數
def map_language_table(data):
    # 處理語文表格的邏輯
    print("Mapping Language Table")
    # 這裡是根據 data 創建 LanguageTable 的實例
    return [LanguageTable(language=row[0], listen=row[1], speak=row[2], read=row[3], write=row[4], other=row[5]) for row in data[1:]]

def map_family_table(data):
    # 處理家庭成員表格的邏輯
    print("Mapping Family Table")
    # 這裡是根據 data 創建 FamilyTable 的實例
    return [FamilyTable(kinship=row[0], name=row[1], age=row[2], career=row[3]) for row in data[1:]]

# 建立 table_index 和 mapping 函數的對應關係
table_mapping = {
    1: map_language_table,
    2: map_family_table,
    # 其他 table_index 對應的 mapping 函數可以依次添加
}

# 處理多個表格的函數
def process_tables(tables):
    results = {}
    for table in tables:
        table_index = table["table_index"]
        data = table["data"]

        # 根據 table_index 找到相應的 mapping 函數
        mapping_func = table_mapping.get(table_index)
        if mapping_func:
            # 執行 mapping 函數並保存結果
            results[table_index] = mapping_func(data)
        else:
            print(f"No mapping function for table_index {table_index}")

    return results

# 示例 JSON 數據
tables_data = [
    {
        "page": 1,
        "table_index": 1,
        "data": [
            ["語文", "聽", "說", "讀", "寫", "撰寫\n手冊"],
            ["英文", "1", "1", "1", "1", ""],
            ["", "", "", "", "", ""]
        ]
    },
    {
        "page": 2,
        "table_index": 2,
        "data": [
            ["關係", "名字", "年齡", "職業"],
            ["兄弟", "小明", 30, "工程師"],
            ["父親", "小王", 55, "商人"]
        ]
    }
]

# 執行處理函數
processed_results = process_tables(tables_data)

# 打印結果
for index, result in processed_results.items():
    print(f"Table Index: {index}")
    for item in result:
        print(item)
