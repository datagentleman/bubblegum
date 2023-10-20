import subprocess
from starbucks.template import WorkerTemplate

class Worker:
  PATH = "./workers"
  
  def run(self):
    code = open(f"{Worker.PATH}/give_me_all_the_data.py", "r").read()
    template = WorkerTemplate("give_me_all_the_data", code)
    
    result = subprocess.run(["python", "-c", template.template()])
