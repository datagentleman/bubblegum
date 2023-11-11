from data_stream import DataStream  

def perform(input: DataStream):
  print(f"Got data from node 1 :{input.next()}")
  print(f"Got data from node 2: {input.next()}")
  input.end()