from fastapi import Request, HTTPException
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from model.Result import *

import time
INTERCEPT_PATHS = ["/", "/uploadpdf/"]
UPLOAD_FILE_PATHS =["/uploadpdf/"]
class PathMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        INTERCEPT_PATHS = ["/", "/uploadpdf/"]

        print("request path : "+request.url.path)

        # 若請求路徑不在 allowed_paths 中，返回 500 錯誤

        if request.url.path not in INTERCEPT_PATHS:
            # return JSONResponse(status_code=404, content={"error": "Request not allowed for this path."})
             return JSONResponse(status_code=404, content=Result.error(StatusCodeEnum.REQUEST_NOT_ALLOWED).to_dict())
            # raise HTTPException(status_code=404, detail="Request not allowed for this path.")
        start_time = time.perf_counter()
        print("middleware 1 ") 
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print("process cost time : " + str(process_time))    

        return response
    
# 判斷上傳檔案的head body
class UploadFIleMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        print("middleware 2 ") 
        # 假設這裡是處理一些情況，你可以根據不同的條件設置不同的返回值

        if request.url.path in UPLOAD_FILE_PATHS:
            # 422錯誤，根據錯誤代碼設置不同的message和detail
            # 例如: 根據 `request.content_type` 或其他條件進行具體錯誤處理
            content_type = request.headers.get("Content-Type", "")
            if not content_type:
                print("NO_CONTENT_TYPE")
                return JSONResponse(
                    status_code=422,  # 自定義錯誤碼
                    content=Result.error(StatusCodeEnum.NO_CONTENT_TYPE).to_dict()
                )
            if "multipart/form-data" not in content_type:
                print("CONTENT_TYPE_ILLEGAL")
                return JSONResponse(
                    status_code=422,
                    content=Result.error(StatusCodeEnum.CONTENT_TYPE_ILLEGAL).to_dict(),
                )

            # 如果 Content-Type 是 multipart/form-data 但缺少 boundary
            if "boundary" not in content_type:
                print("MISSING_BOUNDARY")
                return JSONResponse(
                    status_code=422,
                    content=Result.error(StatusCodeEnum.MISSING_BOUNDARY).to_dict(),
                )
            ## todo postman 裡面用 預設的contype 不會有 400 There was an error parsing the body",
            # 取得 request 的 body（假設是 JSON 格式，若為表單資料則需額外處理）
            # try:
            #     print("111111111111111111")
            #     form = await request.form()
            #     print("222222222222222222")
            #     if 'file' not in form:
            #         print("FILED_NO_DATA")
            #         return JSONResponse(
            #             status_code=422,  # 自定義錯誤碼
            #             content=Result.error(StatusCodeEnum.FILED_NO_DATA).to_dict()
            #         )
                
            #     # 檢查 file 欄位中是否有 data
            #     file = form.get('file')
            #     print("file : "+file)
            #     if not file:
            #         print("FILED_HAS_NO_DATA")
            #         return JSONResponse(
            #             status_code=422,  # 自定義錯誤碼
            #             content=Result.error(StatusCodeEnum.FILED_HAS_NO_DATA).to_dict()
            #         )
                
            # except HTTPException as e:
            #     print("HTTPException: " + str(e))

            # except Exception as e:
            #     print("Exception: " + str(e))

        
        response = await call_next(request)
        
        return response

# 判斷檔案室不是.pdf結委
class PDFFileMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        print("middleware 3 ") 
        response = await call_next(request)
        return response