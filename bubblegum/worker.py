import os
import subprocess

class WorkerStream:
  def __init__(self, conn):
    self.conn = conn    

  def next(self):
    pass


class Worker:
  PATH = "./workers"

  def __init__(self, name: str):
    self.name = name


  def run(self):
    subprocess.Popen(["python", "worker.py", self.read_code()])


  def read_code(self) -> str:
    return open(f"{Worker.PATH}/{self.name}.py", "r").read()


  @classmethod
  def ls(cls) -> list[str]:
    return [name for name in os.listdir(cls.PATH)]
