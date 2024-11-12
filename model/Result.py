from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, code: Optional[int] = None, message: Optional[str] = None, data: Optional[T] = None):
        self.code = code
        self.message = message
        self.data = data
    # 覆寫 __dict__ 方法
    def to_dict(self):
        return {
            # "code": self.code,
            "message": self.message,
            "data": self.data
        }
    
    @staticmethod
    def success(data: Optional[T] = None) -> 'Result[T]':
        result = Result[T]()
        result.code = 1
        result.data = data
        return result

    @staticmethod
    def error(message: str) -> 'Result[T]':
        result = Result[T]()
        result.code = 0
        result.message = message
        return result

    def get_code(self) -> Optional[int]:
        return self.code

    def set_code(self, code: int) -> None:
        self.code = code

    def get_message(self) -> Optional[str]:
        return self.message

    def set_message(self, message: str) -> None:
        self.message = message

    def get_data(self) -> Optional[T]:
        return self.data

    def set_data(self, data: T) -> None:
        self.data = data

    def __repr__(self) -> str:
        # return f"Result(code={self.code}, message={self.message}, data={self.data})"
        return f"Result(message={self.message}, data={self.data})"
