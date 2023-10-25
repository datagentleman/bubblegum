from starbucks.commands import * 

API = {
  "HELLO":  hello,
  "STREAM": stream,

  # WORKERS
  "WLS":  worker_ls, 
  "WRUN": worker_run,  

  # TENSORS
  "TCREATE": tensor_create,
}
