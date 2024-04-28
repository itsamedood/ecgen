from enum import Enum


class EOL(Enum):
  LF    = "lf"
  CR    = "cr"
  CRLF  = "crlf"
  UNSET = "unset"
