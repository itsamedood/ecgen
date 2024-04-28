from enum import Enum


class Charset(Enum):
  LATIN1  = "latin1"
  UTF8    = "utf-8"
  UTF8BOM = "utf-8-bom"
  UTF16BE = "utf-16be"
  UTF16LE = "utf-16le"
  UNSET   = "unset"
