from typing import List, Dict,Any
import pdfplumber
# 使用class mapping 的方法
# 轉換普通表格
def parseNormalTable(table_class: Any,data: List[List[Any]]) -> List[Any]:
    # 將資料轉換成類別實例
# 將資料轉換成類別實例
    objects = []
    headers = data[0]  # 假設第一行是表頭
    
    # 構建欄位映射
    column_map = table_class.columns_map

    for row in data[1:]:  # 跳過表頭行
        # 建立包含表頭和數據的字典
        row_data = {}
        for index, value in enumerate(row):
            column_name = headers[index]
            if column_name in column_map:  # 如果該欄位有對應的類屬性
                
                field_name = column_map[column_name]
                print("field_name "+ field_name+"\n")
                row_data[field_name] = value
        
        # 使用 **row_data 解包參數並初始化類別
        obj = table_class(**row_data)
        objects.append(obj)
    return objects