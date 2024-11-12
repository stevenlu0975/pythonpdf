import datetime
from typing import List, Type, Any, Dict
import json

# 定義對應的類別 (僅部分作為示例)
class LanguageTable:
    columns_map = {
        "語文": "language",
        "聽": "listen",
        "說": "speak",
        "讀": "read",
        "寫": "write",
        "撰寫\n手冊": "other"
    }
    
    def __init__(self, language: str, listen: int, speak: int, read: int, write: int, other: str):
        self.language = language
        self.listen = listen
        self.speak = speak
        self.read = read
        self.write = write
        self.other = other

    def __str__(self):
        return f"LanguageTable(language={self.language}, listen={self.listen}, speak={self.speak}, read={self.read}, write={self.write}, other={self.other})"

class FamilyTable:
    columns_map = {
        "稱謂": "kinship",
        "姓名": "name",
        "年齡": "age",
        "職業": "career"
    }
    
    def __init__(self, kinship: str, name: str, age: int, career: str):
        self.kinship = kinship
        self.name = name
        self.age = age
        self.career = career

    def __str__(self):
        return f"FamilyTable(kinship={self.kinship}, name={self.name}, age={self.age}, career={self.career})"

# 設置表格名稱與類別的映射
table_class_mapping = {
    "LanguageTable": LanguageTable,
    "FamilyTable": FamilyTable,
    # 增加其他表格映射...
}

# 通用解析函數
def parse_table_data(table_name: str, data: List[List[Any]]) -> List[Any]:
    # 取得對應的類別
    table_class = table_class_mapping.get(table_name)
    if not table_class:
        raise ValueError(f"No class mapping found for table: {table_name}")
    
    # 將資料轉換成類別實例
    objects = []
    headers = data[0]  # 假設第一行是表頭
    
    # 構建欄位映射
    column_map = table_class.columns_map

    for row in data[1:]:  # 跳過表頭行
        # 建立包含表頭和數據的字典
        row_data = {}
        for index, value in enumerate(row):
            column_name = headers[index].lower()
            if column_name in column_map:  # 如果該欄位有對應的類屬性
                field_name = column_map[column_name]
                row_data[field_name] = value
        
        # 使用 **row_data 解包參數並初始化類別
        obj = table_class(**row_data)
        objects.append(obj)

    return objects

# 示例 JSON 資料 (表格名稱及資料)
json_data = {
    "LanguageTable": [
        ["語文", "聽", "說", "讀", "寫", "撰寫\n手冊"],
        ["英文", 1, 1, 1, 1, ""]
    ],
    "FamilyTable": [
        ["稱謂", "姓名", "年齡", "職業"],
        ["父親", "張三", 50, "教師"]
    ]
}

# 自動處理每個表格
for table_name, data in json_data.items():
    instances = parse_table_data(table_name, data)
    for instance in instances:
        print(instance)

        # 將類實例轉換為 JSON 字符串
        instance_str = json.dumps(instance, default=lambda o: o.__dict__)
        print(instance_str)
