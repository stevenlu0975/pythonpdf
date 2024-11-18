from typing import List, Dict,Any
from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.middleware import Middleware
from starlette.responses import JSONResponse
from utils.myPDFPlumber import *
import pandas as pd
from ExceptionHandler import *
from myMiddleware import *

middleware = [
    Middleware(PathMiddleWare),
    Middleware(UploadFIleMiddleWare),
    Middleware(PDFFileMiddleWare)
]

app = FastAPI(middleware=middleware)
limiter = Limiter(key_func=get_remote_address)
# 注册 UnicornException 的处理器
app.add_exception_handler(StarletteHTTPException, StarletteHTTPExceptionHandler)
app.add_exception_handler(RequestValidationError, RequestValidationErrorHandler)
app.add_exception_handler(HTTPException, HTTPExceptionHandler)
app.add_exception_handler(RateLimitExceeded, rate_limit_errorHandler)


@app.post("/uploadpdf/")
@limiter.limit("5/minute")
async def upload_pdf(file: UploadFile,request: Request):
   

    # 檢查file 是否為空
    if not file.filename:
        raise HTTPException(status_code=400, detail=Result.error(StatusCodeEnum.NO_FILE_UPLOAD))
    
    # 檢查文件類型
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400,  detail=Result.error(StatusCodeEnum.NOT_PDF_FILE))
    
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
        raise HTTPException(status_code=400, detail=Result.error(StatusCodeEnum.PROCESSING_PDF_FILE_ERROR))

# 清理資料並轉換格式
def parse_certification_status(status_text):
    return "有" if "■有" in status_text else ""


def pandaEtlParse(data: List[List[Any]]) -> List[Any]:
    # 將資料轉換成結構化的 DataFrame
    columns = data[0]  # 使用第一行作為標題
    records = data[1:]  # 去除標題行的實際數據
    df = pd.DataFrame(records, columns=columns)
    # 應用轉換函數
    df["證書"] = df["證書"].apply(parse_certification_status)
    print(df)
    table_index = 1  # 假設這是目前的表格索引
    result = {
        str(table_index): {
            "header": columns,  # 假設您只想要 "證書" 和 "認證單位"
            "data": df[columns].values.tolist() 
        }
    }
    return result


# 處理多個表格的函數
def process_tables(tables):
    results = {}

    print(len(tables))
    for table in tables:
        
        table_index = table["table_index"]
        table_page = table["page"]
        data = table["data"]
        if table_page == 1:
            if table_index == 5:
                return pandaEtlParse(data)

