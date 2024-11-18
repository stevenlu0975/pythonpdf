from typing import Generic, TypeVar, Optional
from model.StatusCode import *
T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, code: Optional[int] = None, message: Optional[str] = None, data: Optional[T] = None):
        self.code = code
        self.message = message
        self.data = data
    def to_dict(self):
        if self.message == "":
            self.message = StatusCodes.get_message(self.code)
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }
    
    @staticmethod
    def success(data: Optional[T] = None) -> 'Result[T]':
        result = Result[T]()
        result.code = StatusCodes.get_status(200)
        result.message = "success"
        result.data = data
        return result

    @staticmethod
    def error_with_message(message: str) -> 'Result[T]':
        result = Result[T]()
        result.code = 0
        result.message = message
        return result
    @staticmethod
    def error(code: StatusCodeEnum) -> 'Result[T]':
        
        result = Result[T]()
        result.code = code.value
        result.message = StatusCodes.get_message(result.code)
        return result
    
    def get_code(self) -> Optional[int]:
        return self.code

    def set_code(self, code: int) -> None:
        self.code = code
        return self
    def get_message(self) -> Optional[str]:
        return self.message

    def set_message(self, message: str) -> None:
        self.message = message
        return self
    def get_data(self) -> Optional[T]:
        return self.data

    def set_data(self, data: T) -> None:
        self.data = data
        return self
    def __repr__(self) -> str:
        return f"Result(code={self.code}, message={self.message}, data={self.data})"
