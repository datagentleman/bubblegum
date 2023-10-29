from starbucks.commands import * 

API = {
  "HELLO":  hello,

  # WORKERS
  "WLS":      worker_ls, 
  "WRUN":     worker_run,  

  # TENSORS
  "TCREATE": tensor_create,
  "TREMOVE": tensor_remove,
  "TSTREAM": tensor_stream,
  "TLS":     tensor_list,
}
