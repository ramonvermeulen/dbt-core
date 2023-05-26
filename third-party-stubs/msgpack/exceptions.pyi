from typing import Any

class UnpackException(Exception): ...
class BufferFull(UnpackException): ...
class OutOfData(UnpackException): ...
class FormatError(ValueError, UnpackException): ...
class StackError(ValueError, UnpackException): ...

UnpackValueError = ValueError

class ExtraData(UnpackValueError):
    def __init__(self, unpacked: Any, exta: Any) -> None: ...

PackException = Exception
PackValueError = ValueError
PackOverflowError = OverflowError
