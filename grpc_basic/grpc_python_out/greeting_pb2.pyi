from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DrawReply(_message.Message):
    __slots__ = ["image", "name"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    name: str
    def __init__(self, name: _Optional[str] = ..., image: _Optional[bytes] = ...) -> None: ...

class DrawRequest(_message.Message):
    __slots__ = ["image", "name"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    name: str
    def __init__(self, name: _Optional[str] = ..., image: _Optional[bytes] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImageReply(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImageRequest(_message.Message):
    __slots__ = ["image", "name"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    name: str
    def __init__(self, name: _Optional[str] = ..., image: _Optional[bytes] = ...) -> None: ...

class VideoReply(_message.Message):
    __slots__ = ["name", "video"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    name: str
    video: bytes
    def __init__(self, name: _Optional[str] = ..., video: _Optional[bytes] = ...) -> None: ...

class VideoRequest(_message.Message):
    __slots__ = ["name", "video"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    name: str
    video: bytes
    def __init__(self, name: _Optional[str] = ..., video: _Optional[bytes] = ...) -> None: ...
