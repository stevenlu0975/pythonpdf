from enum import Enum
from typing import Dict, Optional,Any
class StatusCodeEnum(Enum):
    SUCCESS = 200
    NO_CONTENT_TYPE = 1001
    CONTENT_TYPE_ILLEGAL = 1002
    MISSING_BOUNDARY = 1003
    REQUEST_PARAM_VALIDATION_ERROR = 3002
    REQUEST_PATH_NOT_ALLOWED = 2001
    NOT_PDF_FILE = 3001
    PROCESSING_PDF_FILE_ERROR = 4001
    UNKNOWN_DETAIL_TYPE=5001
    OTHER_HTTPEXCEPTION=5002
    NO_FILE_UPLOAD = 3003
    REQUEST_METHOD_ERROR = 2002
class StatusCodes:
    
    STATUS_MESSAGES: Dict[int, Dict[str, Optional[Any]]] = {
        200: {
            "message": "success",
        },
        1001: {
            "message": "No content type",
        },
        1002: {
            "message": "Content type illegel",
        },
        1003: {
            "message": "Missing boundary in multipart",
        },
        2001: {
            "message": "request not allowed"
        },
        3001: {
            "message": "File type not supported. Please upload a PDF file"
        },
        4001: {
            "message": "Error processing PDF file"
        },
        5001: {
            "message": "unknown message detail type error"
        },
        3003:{
            "message": "No file uploaded. Please upload a PDF file"
        },
        2002:{
            "message": "Method Not Allowed"
        }
    
    }

    @classmethod
    def get_status(cls, code: StatusCodeEnum) -> Optional[Dict[str, Optional[str]]]:
        return cls.STATUS_MESSAGES.get(code)

    @classmethod
    def get_message(cls, code: int) -> Optional[str]:
        status = cls.get_status(code)
        return status.get("message") if status else None

