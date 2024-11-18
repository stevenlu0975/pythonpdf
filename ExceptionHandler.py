from myFastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from model.Result import *
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# fastapi 自訂的exception 例如: 以get訪問
async def StarletteHTTPExceptionHandler(request: Request, exc: StarletteHTTPException):
    status_code = exc.status_code
    detail = exc.detail
    return JSONResponse(
        status_code=status_code,
        content=Result.error_with_message(detail).set_code(status_code).to_dict(),
    )

#422 沒有contenttype等等 
async def RequestValidationErrorHandler(request: Request, exc: RequestValidationError):
    errors = exc.errors()  
    error_msgs = [error['msg'] for error in errors]  
    error_message = ', '.join(error_msgs)
    
    return JSONResponse(
        status_code=422,
        content=Result.error_with_message(error_message).set_code(StatusCodeEnum.REQUEST_PARAM_VALIDATION_ERROR.value).to_dict(),
    )
# 手動設置的exception
async def HTTPExceptionHandler(request: Request, exc: HTTPException):
    status_code = exc.status_code
    detail = exc.detail

    if isinstance(detail, Result):
        content=detail
    elif isinstance(detail, str):
        content=Result.error_with_message(detail).set_code(StatusCodeEnum.OTHER_HTTPeXCEPTION)
    else:
        content=Result.error(StatusCodeEnum.UNKNOWN_DETAIL_TYPE)
    return JSONResponse(
        status_code=status_code,
        content=content.to_dict(),
    )

async def rate_limit_errorHandler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content=Result.error_with_message("Please wait before sending more requests").set_code(5003).to_dict()
    )