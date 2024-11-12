from myFastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from model.Result import *
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# app = FastAPI()


# fastapi 自訂的exception 例如: 以get訪問
async def StarletteHTTPExceptionHandler(request: Request, exc: StarletteHTTPException):
        # 捕獲詳細錯誤訊息
    status_code = exc.status_code
    detail = exc.detail
    return JSONResponse(
        status_code=status_code,
        # content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
        # content={"message": f"Oops! did something. There goes a rainbow..."},
       content=Result.error(detail).to_dict(),
    )

#422 沒有contenttype等等 
async def RequestValidationErrorHandler(request: Request, exc: RequestValidationError):
    # 捕獲詳細錯誤訊息
    errors = exc.errors()  # 返回錯誤的列表
    error_msgs = [error['msg'] for error in errors]  # 提取每個錯誤的 msg
    # 將錯誤消息合併成一個字符串，而不是列表
    error_message = ', '.join(error_msgs)
    
    return JSONResponse(
        status_code=422,
        # content={
        #     "detail2": f"Method Not Allowed: {', '.join(error_msgs) or 'This method is not supported for the requested resource.'}"
        # },
        content=Result.error(error_message).to_dict(),
    )
# 手動設置的exception
async def HTTPExceptionHandler(request: Request, exc: HTTPException):
        # 捕獲詳細錯誤訊息
    status_code = exc.status_code
    detail = exc.detail

    # 500改成415
    if status_code == 500:
        status_code=415
    return JSONResponse(
        status_code=status_code,
        # content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
        # content={"message": f"Oops! did something. There goes a rainbow..."},
        content=Result.error(detail).to_dict(),
    )

