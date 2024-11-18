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
             return JSONResponse(status_code=404, content=Result.error(StatusCodeEnum.REQUEST_PATH_NOT_ALLOWED).to_dict())
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
        if request.method =='GET':
            return JSONResponse(
                    status_code=422,  
                    content=Result.error(StatusCodeEnum.REQUEST_METHOD_ERROR).to_dict()
            )
        if request.url.path in UPLOAD_FILE_PATHS:
            content_type = request.headers.get("Content-Type", "")
            if not content_type:
                return JSONResponse(
                    status_code=422,  
                    content=Result.error(StatusCodeEnum.NO_CONTENT_TYPE).to_dict()
                )
            if "multipart/form-data" not in content_type:
                return JSONResponse(
                    status_code=422,
                    content=Result.error(StatusCodeEnum.CONTENT_TYPE_ILLEGAL).to_dict(),
                )

            # 如果 Content-Type 是 multipart/form-data 但缺少 boundary
            if "boundary" not in content_type:
                return JSONResponse(
                    status_code=422,
                    content=Result.error(StatusCodeEnum.MISSING_BOUNDARY).to_dict(),
                )
        
        response = await call_next(request)
        
        return response

# 判斷檔案是不是.pdf結尾 
class PDFFileMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        print(f"middleware 3 {request.method}")         
        response = await call_next(request)
        return response