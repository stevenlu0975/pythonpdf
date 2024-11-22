import re

# # 範例字串
text = "2024/09 ~ 2025/01"

# # 正則表達式：匹配年和月的組合，允許用 "/", "~", 或空格分隔
# pattern = r"(\d{4})[\/~\s]?(\d{2})[\/~\s]+(\d{4})[\/~\s]?(\d{2})"

# # 使用 re.match 進行匹配
# match = re.match(pattern, text)
# if match:
#     year1, month1, year2, month2 = match.groups()
#     print(f"第一組：{year1}-{month1}")
#     print(f"第二組：{year2}-{month2}")
# else:
#     print("無法匹配")

def parse_start_end_status(value: str) -> str:
    date_pattern = r"(\d{4})[/~\s]?(\d{2})[/~\s]+(\d{4})[/~\s]?(\d{2})"
    match = re.match(date_pattern, value)
    start_date:str
    end_date :str
    
    if match:
        # year1, month1, year2, month2 = match.groups()
        year1= match.group(1)
        month1= match.group(2)
        year2= match.group(3)
        month2= match.group(4)
        print(f"col: {year1}")
        print(f"col: {month1}")
        print(f"col: {year2}")
        print(f"col: {month2}")
        # start_date = match.group(1)  # 起始日期
        # end_date = match.group(2)    # 結束日期
        # print(f"第一組：{year1}-{month1}")
        # print(f"第二組：{year2}-{month2}")

    return year1


parse_start_end_status(text)

