from typing import List, Dict, Union,Annotated,Any
from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from enum import Enum
from utils.myPDFPlumber import *
import pandas as pd
import json
from ExceptionHandler import *
from myMiddleware import *

middleware = [
    Middleware(PathMiddleWare),
    Middleware(UploadFIleMiddleWare),
    Middleware(PDFFileMiddleWare)
]

# # 建立 table_index 和 mappingClass 函數的對應關係
# table_class_mapping = {
#     1: LanguageTable
#     # 其他 table_index 對應的 mapping 函數可以依次添加
# }

app = FastAPI(middleware=middleware)

# 注册 UnicornException 的处理器
app.add_exception_handler(StarletteHTTPException, StarletteHTTPExceptionHandler)
app.add_exception_handler(RequestValidationError, RequestValidationErrorHandler)
app.add_exception_handler(HTTPException, HTTPExceptionHandler)




@app.post("/uploadpdf/")
#async def upload_pdf(file: UploadFile = File(...)) -> Dict[str, Union[str, List[Dict[str, Union[str, List[List[str]]]]]]]:
async def upload_pdf(file: UploadFile,request: Request):
   

    # 檢查是否有文件上傳
    # if not file:
    #     raise HTTPException(status_code=400, detail="No file uploaded. Please upload a PDF file.")
    
    # 檢查文件類型
    
    if not file.filename.endswith('.pdf'):
        print(f"*************** {StatusCodes.get_message(StatusCodeEnum.NOT_PDF_FILE)}")
        # raise HTTPException(status_code=400, detail="File type not supported. Please upload a PDF file.")
        # raise HTTPException(status_code=400,  detail=StatusCodes.get_message(StatusCodeEnum.NOT_PDF_FILE.value))
        raise HTTPException(status_code=400,  detail=Result.error(StatusCodeEnum.NOT_PDF_FILE))
        # raise HTTPException(status_code=400,  detail="12345678")
    
    print(request.url.path)
    return await parsetToJson(file)

# return json
async def parsetToJson(file):
    pdf_text = []
    pdf_tables = []
    try:
        with pdfplumber.open(file.file) as pdf:
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                
                # 提取文字
                text = page.extract_text()
                pdf_text.append({"page": page_num + 1, "text": text})
                
                # 提取表格
                tables = page.extract_tables()
                for table_index, table in enumerate(tables):
                    pdf_tables.append({
                        "page": page_num + 1,
                        "table_index": table_index + 1,
                        "data": table
                    })
        return Result.success({
            # "text": pdf_text,
            "tables": process_tables(pdf_tables)
        }).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF file: {str(e)}")

# 清理資料並轉換格式
def parse_certification_status(status_text):
    return "有" if "■有" in status_text else ""

# 使用etl 轉換data
def pandaEtlParse(data: List[List[Any]]) -> List[Any]:
    # 將資料轉換成結構化的 DataFrame
    columns = data[0]  # 使用第一行作為標題
    records = data[1:]  # 去除標題行的實際數據
    df = pd.DataFrame(records, columns=columns)
    # 應用轉換函數
    df["證書"] = df["證書"].apply(parse_certification_status)
    print(df)
    json_result = []
    # 準備轉換成 JSON 的結構
    table_index = 1  # 假設這是目前的表格索引
    result = {
        str(table_index): {
            "header": columns,  # 假設您只想要 "證書" 和 "認證單位"
            "data": df[columns].values.tolist()  # 轉換為 list 格式
        }
    }
    # 輸出結果轉為 JSON 格式
    # json_result = json.dumps(result, ensure_ascii=False)
    return result


# 處理多個表格的函數
def process_tables(tables):
    results = {}
    print("==========================")
    print(len(tables))
    print("--------------------------")
    for table in tables:
        
        table_index = table["table_index"]
        table_page = table["page"]
        print("table_index: "+str(table_index))
        data = table["data"]
        if table_page == 1:
            if table_index == 5:
                # 使用class mapping 的方法
                # print(table)
                # # 根據 table_index 找到相應的 mapping 函數
                # mapping_class = table_class_mapping.get(table_index)
                # if mapping_class:
                #     print(f"Calling mapping function for table_index {table_index} with data: {data}")
                #     # 執行 mapping 函數並保存結果
                #     # results[table_index] = parseNormalTable(mapping_class,data)
                #     results[table_index] = parseNormalTable(mapping_class,data)
                # else:
                #     print(f"No mapping function for table_index {table_index}")

                return pandaEtlParse(data)

