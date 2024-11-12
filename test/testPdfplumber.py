import pdfplumber

# 打開PDF文件
pdf_path = "C:\\workspace\\pdf\\77777.pdf"
with pdfplumber.open(pdf_path) as pdf:
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        
        # 提取文字
        text = page.extract_text()
        print(f"Page {page_num + 1} Text:\n{text}\n")
        
        # 提取表格
        tables = page.extract_tables()
        for table_index, table in enumerate(tables):
            print(f"Table {table_index + 1} on Page {page_num + 1}:")
            for row in table:
                print(row)  # 打印每一行的數據

