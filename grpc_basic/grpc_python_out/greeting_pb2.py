# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egreeting.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"*\n\x0b\x44rawRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\"(\n\tDrawReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\"+\n\x0cImageRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\"\x1a\n\nImageReply\x12\x0c\n\x04name\x18\x01 \x01(\t\"+\n\x0cVideoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05video\x18\x02 \x01(\x0c\")\n\nVideoReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05video\x18\x02 \x01(\x0c\x32\xbc\x01\n\tGreetings\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x12\'\n\tDrawHello\x12\x0c.DrawRequest\x1a\n.DrawReply\"\x00\x12,\n\nImageHello\x12\r.ImageRequest\x1a\x0b.ImageReply\"\x00(\x01\x12.\n\nVideoHello\x12\r.VideoRequest\x1a\x0b.VideoReply\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=18
  _HELLOREQUEST._serialized_end=46
  _HELLOREPLY._serialized_start=48
  _HELLOREPLY._serialized_end=77
  _DRAWREQUEST._serialized_start=79
  _DRAWREQUEST._serialized_end=121
  _DRAWREPLY._serialized_start=123
  _DRAWREPLY._serialized_end=163
  _IMAGEREQUEST._serialized_start=165
  _IMAGEREQUEST._serialized_end=208
  _IMAGEREPLY._serialized_start=210
  _IMAGEREPLY._serialized_end=236
  _VIDEOREQUEST._serialized_start=238
  _VIDEOREQUEST._serialized_end=281
  _VIDEOREPLY._serialized_start=283
  _VIDEOREPLY._serialized_end=324
  _GREETINGS._serialized_start=327
  _GREETINGS._serialized_end=515
# @@protoc_insertion_point(module_scope)
