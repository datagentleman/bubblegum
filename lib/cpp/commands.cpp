#include "conn.cpp"
#include "buffer.cpp"

void tensor_put(int fd) {
  conn con = conn(fd);

  std::string msg = "response from cpp";
  con.write(&msg);
  
  std:string tensor_name;
  con.read(&tensor_name);

  buffer buf = buffer();
  con.read(buf.vec());
}