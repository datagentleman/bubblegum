import os
import subprocess

from starbucks.template import WorkerTemplate

class Worker:
  PATH = "./workers"

  def __init__(self, name):
    self.name = name
    self.template = WorkerTemplate(self.name, self.read_code())


  def run(self):
    subprocess.run(["python", "-c", self.template.template()])


  def read_code(self) -> str:
    return open(f"{Worker.PATH}/{self.name}.py", "r").read()


  @classmethod
  def ls(cls) -> list[str]:
    return [name for name in os.listdir(cls.PATH)]
