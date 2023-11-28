import dataclasses

@dataclasses
class Tensor:
  name:  str = ""
  dtype: str = "float16"
  shape: list(int) = ()
  size:  int = 0
