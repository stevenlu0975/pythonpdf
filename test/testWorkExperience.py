import pandas as pd
import re

# 原始資料
data = [
[
                    "公司名稱/人數規模",
                    "部門/職稱/工作內容",
                    "起訖年月(西元)",
                    "離職原因",
                    "離職月薪",
                    "年薪"
                ],
                [
                    "公司:comp1\n部門:dep1",
                    "職稱：sub1\n工作內容：cont1\n擔任主管：□是□否",
                    "自 123 年4 月\n至124 年5 月",
                    "",
                    "固 定 月 薪 ： 100000\n元\n____津貼： 元\n其他 ： 元\n合計月薪： 元",
                    "固定月薪 1 個月\n績效獎金 1個月\n年終獎金_1_個月\n合計年薪_1_個月"
                ],
                [
                    "公司:comp1\n部門:dep2",
                    "職稱：\n工作內容：\n擔任主管：□是□否",
                    "自 年 月\n至 年 月",
                    "",
                    "固定月薪： 元\n____津貼： 元\n其他 ： 元\n合計月薪： 元",
                    "固定月薪 個月\n績效獎金 個月\n年終獎金___個月\n合計年薪___個月"
                ],
                [
                    "公司:\n部門:",
                    "職稱：\n工作內容：\n擔任主管：□是□否",
                    "自 年 月\n至 年 月",
                    "",
                    "固定月薪： 元\n____津貼： 元\n其他 ： 元\n合計月薪： 元",
                    "固定月薪 個月\n績效獎金 個月\n年終獎金___個月\n合計年薪___個月"
                ],
                [
                    "公司:\n部門:",
                    "職稱：\n工作內容：\n擔任主管：□是□否",
                    "自 年 月\n至 年 月",
                    "",
                    "固定月薪： 元\n____津貼： 元\n其他 ： 元\n合計月薪： 元",
                    "固定月薪 個月\n績效獎金 個月\n年終獎金___個月\n合計年薪___個月"
                ]
]

# 定義一個函數來解析每個欄位中的數據
def parse_company_info(text):
    company_match = re.search(r"公司:(.*?)\n", text)
    department_match = re.search(r"部門:(.*)", text)
    company = company_match.group(1) if company_match else None
    department = department_match.group(1) if department_match else None
    return company, department

def parse_position_info(text):
    title_match = re.search(r"職稱：(.*?)\n", text)
    content_match = re.search(r"工作內容：(.*?)\n", text)
    supervisor_match = re.search(r"擔任主管：(□是|□否)", text)
    title = title_match.group(1) if title_match else None
    content = content_match.group(1) if content_match else None
    supervisor = supervisor_match.group(1) if supervisor_match else None
    return title, content, supervisor

def parse_date_info(text):
    start_date_match = re.search(r"自 (\d+ 年\d+ 月)", text)
    end_date_match = re.search(r"至(\d+ 年\d+ 月)", text)
    start_date = start_date_match.group(1) if start_date_match else None
    end_date = end_date_match.group(1) if end_date_match else None
    return start_date, end_date

def parse_salary_info(text):
    salary_match = re.search(r"固 定 月 薪 ： (\d+)", text)
    salary = int(salary_match.group(1)) if salary_match else None
    return salary

# 構建 DataFrame
columns = ["公司名稱", "部門", "職稱", "工作內容", "擔任主管", "起始日期", "結束日期", "月薪"]
records = []

for entry in data[1:]:  # 跳過標題列
    company, department = parse_company_info(entry[0])
    title, content, supervisor = parse_position_info(entry[1])
    start_date, end_date = parse_date_info(entry[2])
    salary = parse_salary_info(entry[4])

    # 將數據加入到列表中
    records.append([company, department, title, content, supervisor, start_date, end_date, salary])

# 轉換成 DataFrame
df = pd.DataFrame(records, columns=columns)

print(df)
