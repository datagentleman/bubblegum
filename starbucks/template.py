TEMPLATE = """
from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

# worker code goes here
{} 

if __name__ == '__main__':
  client = Client(HOST, PORT)
  client.send("STREAM", "iris/iris.csv")

  # execute worker function
  {}(client.read())
"""

class WorkerTemplate:
  def __init__(self, name, code):
    self.name = name
    self.code = code


  def template(self):    
    t = TEMPLATE.format(self.code, self.name)
    print(t)
    return t