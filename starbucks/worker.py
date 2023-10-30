import os
import subprocess

class Worker:
  PATH = "./workers"

  def __init__(self, name: str):
    self.name = name


  def run(self):
    # TODO: Add argument - user defined function
    subprocess.Popen(["python", "worker.py", self.read_code()])


  def read_code(self) -> str:
    return open(f"{Worker.PATH}/{self.name}.py", "r").read()


  @classmethod
  def ls(cls) -> list[str]:
    return [name for name in os.listdir(cls.PATH)]
