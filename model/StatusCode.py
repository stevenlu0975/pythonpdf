# status_codes.py
from enum import Enum
from typing import Dict, Optional,Any
class StatusCodeEnum(Enum):
    SUCCESS = 200
    NO_CONTENT_TYPE = 42200
    CONTENT_TYPE_ILLEGAL = 42201
    MISSING_BOUNDARY = 42202
    REQUEST_NOT_ALLOWED = 40501
    NOT_PDF_FILE = 40001
    PROCESSING_PDF_FILE_ERROR = 40002
    
class StatusCodes:
    """狀態碼與訊息的對應類"""
    
    STATUS_MESSAGES: Dict[int, Dict[str, Optional[Any]]] = {
        200: {
            "message": "success",
        },
        42200: {
            "message": "Field required",
        },
        42201: {
            "message": "Field required",
        },
        42202: {
            "message": "Missing boundary in multipart",
        },
        40501:{
            "message": "request not allowed"
        },
        40001:{
            "message": "File type not supported. Please upload a PDF file"
        },
        40002:{
            "message:": "Error processing PDF file"
        }
    
    }

    @classmethod
    def get_status(cls, code: StatusCodeEnum) -> Optional[Dict[str, Optional[str]]]:
        """根據狀態碼取得對應的訊息"""
        return cls.STATUS_MESSAGES.get(code)

    @classmethod
    def get_message(cls, code: int) -> Optional[str]:
        """根據狀態碼取得對應的訊息內容"""
        status = cls.get_status(code)
        return status.get("message") if status else None

