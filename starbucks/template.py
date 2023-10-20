class WorkerTemplate:
  def __init__(self, name, code):
    self.name = name
    self.code = code


  def template(self):
    return f"""
    from starbucks.client import Client

    HOST = '127.0.0.1'
    PORT = 1337

    {self.code}

    if __name__ == '__main__':
      stream = Client(HOST, PORT)
      stream.send("STREAM", "iris/iris.csv")

      {self.name}(stream.read())
    """