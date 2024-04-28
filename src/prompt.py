from charset import Charset
from eol import EOL
from inquirer import Confirm, List, Text, prompt
from os import getcwd
from typing import Any


class Prompt:
  def __init__(self) -> None: ...

  def get_supported_properties(self) -> dict[str, Any]:
    """
    Gets all supported properties for the editorconfig file to generate according to https://editorconfig.org/#file-format-details.
    """

    given: dict[str, Any] = {}

    # root = true | false
    root: dict[str, bool] | None = prompt([Confirm("root", default=True, message="Root?")])
    if root is not None: given["root"] = str(root["root"]).lower()
    else: raise Exception("need root!")

    # charset = latin1 | utf-8 | utf-8-bom | utf-16be | utf-16le | unset
    charset: dict[str, Charset] | None = prompt([List("charset", "Charset?", [cs.value for cs in Charset], carousel=True)])
    if charset is not None: given |= charset
    else: raise Exception("need charset!")

    # end_of_line = lf | cr | crlf | unset
    end_of_line: dict[str, EOL] | None = prompt([List("end_of_line", "End of line?", [e.value for e in EOL], carousel=True)])
    if end_of_line is not None: given |= end_of_line
    else: raise Exception("need end_of_line!")

    # indent_style = tab | space | unset
    indent_style: dict[str, str] | None = prompt([List("indent_style", "Indent style?", ["tab", "space", "unset"], carousel=True)])
    if indent_style is not None: given |= indent_style
    else: raise Exception("need indent_style!")

    if given["indent_style"] == "space":
      # indent_size = <int> | unset (if `0`)
      indent_size: dict[str, str] | None = prompt([Text("indent_size", "Indent size? (0 = unset)", '4')])

      if indent_size is not None:
        if indent_size["indent_size"].isdigit(): given["indent_size"] = int(indent_size["indent_size"])
        else: raise Exception("indent_size should be an integer!")
      else: raise Exception("need indent_size!")

    elif given["indent_style"] == "tab":
      # tab_width = <int> | unset (if `0`)
      tab_width: dict[str, str] | None = prompt([Text("tab_width", "Tab width? (0 = unset)", '4')])
      if tab_width is not None:
        if tab_width["tab_width"].isdigit(): given["tab_width"] = int(tab_width["tab_width"])
        else: raise Exception("tab_width should be an integer!")
      else: raise Exception("need tab_width!")

    # trim_trailing_whitespace = true | false
    ttw: dict[str, bool] | None = prompt([Confirm("ttw", default=True, message="Trim trailing whitespace?")])
    if ttw is not None: given["trim_trailing_whitespace"] = str(ttw["ttw"]).lower()
    else: raise Exception("need ttw!")

    # insert_final_newline = true | false
    ifn: dict[str, bool] | None = prompt([Confirm("ifn", default=True, message="Insert final newline?")])
    if ifn is not None: given["insert_final_newline"] = str(ifn["ifn"]).lower()
    else: raise Exception("need ifn!")

    return given

  def get_path(self) -> str:
    # Path to generated `.editorconfig`.
    path: dict[str, str] | None = prompt([Text("path", "Path to generate", "%s/.editorconfig" %getcwd())])
    if path is not None: return path["path"]
    else: raise Exception("need path!")
