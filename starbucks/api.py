from starbucks.commands import *
from starbucks.cython.commands import ping

CYTHON_API = {
  "PING": ping,
}

PYTHON_API ={
  "HELLO":  hello,

  # WORKERS
  "WLS":  worker_ls, 
  "WRUN": worker_run,  

  # TENSORS
  "TCREATE": tensor_create,
  "TREMOVE": tensor_remove,
  "TSTREAM": tensor_stream,
  "TLS":     tensor_list,  
}
