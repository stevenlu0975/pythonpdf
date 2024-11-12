from fastapi import Request, HTTPException
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
import time
class PathMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        intercept_paths = ["/", "/uploadpdf/"]

        print("request path : "+request.url.path)

        # 若請求路徑不在 allowed_paths 中，返回 500 錯誤

        if request.url.path not in intercept_paths:
            # return JSONResponse(status_code=404, content={"error": "Request not allowed for this path."})
            # return JSONResponse(status_code=404, content=Result.error("Request not allowed for this path.").to_dict())
            raise HTTPException(status_code=404, detail="Request not allowed for this path.")
        start_time = time.perf_counter()
        print("middleware 1 ") 
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print("process cost time : " + str(process_time))    

        return response

class SecondMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        start_time = time.perf_counter()
        print("middleware 2 ") 
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time2"] = str(process_time)
        print("2 process cost time : "+str(process_time))
        return response