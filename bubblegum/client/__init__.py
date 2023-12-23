from .client import Client

def connect(host: str, port: str) -> Client:
  return Client().connect(host, port)
