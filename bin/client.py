import numpy as np
from starbucks.client import Client

HOST = '127.0.0.1'
PORT = 1337

if __name__ == '__main__':
  client = Client(HOST, PORT).connect()

  # iter = client.tstream('iris')

  # print('iteration ...........')
  # print(iter.next())
  # print(iter.next())
  # print(iter.end())

  # res = client.ping()
  # print(res.data())

  client.tinsert()

  # print("xxxxxxxxxxx")
  # res = client.wls()
  # print(res.read())
  # print(res.read())

  # res = client.wrun('give_me_all_the_data')
  # print(res.data())