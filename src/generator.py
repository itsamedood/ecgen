from os.path import exists
from typing import Any


class Generator:
  def __init__(self) -> None: ...

  def generate(self, _path: str, _properties: dict[str, Any]):
    try:
      with open(_path, 'x' if not exists(_path) else 'w') as dotec:
        dotec.write(f"""root = {_properties["root"]}

[*]
{'\n'.join([f"{p} = {_properties[p]}" for p in _properties if not p == "root"])}
""")
    except: print("Failed to write code to `%s`!" %_path)
