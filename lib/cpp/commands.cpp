#include <chrono>
#include <thread>
#include "conn.cpp"
#include "buffer.cpp"
#include "bucket.cpp"
#include "timer.cpp"
#include "tensor.cpp"

void f(int fd) {
  conn   con  = conn(fd);
  buffer buf  = buffer();
  buffer data = buffer();

  // Set socket to blocking mode 
  // TODO: extract this
  int flags = fcntl(con.sock, F_GETFL, 0);
  flags &= ~O_NONBLOCK;
  fcntl(con.sock, F_SETFL, flags);

  TIMER_BEGIN(socket_read);
  con.read_all(buf.vec());
  TIMER_END(socket_read);

  // if(len > 0) {
  std::string tensor_name = "";
  buf.read(&tensor_name);

  CTensor tensor = CTensor(tensor_name);
  TIMER_BEGIN(tput);

  TIMER_BEGIN(buf_read);
  buf.read(data.vec());
  TIMER_END(buf_read);

  TIMER_BEGIN(disk_write);
  tensor.put(&data);
  TIMER_END(disk_write);

  int res = 1;
  con.write_all(&res);
  TIMER_END(tput);
  // }
}

void tput(int fd) {
  std::thread t(f, fd);
  t.detach();
}

void tget(int fd) {
  conn   con  = conn(fd);
  buffer cmd  = buffer();
  buffer data = buffer();

  con.read_all(cmd.vec());

  std::string tensor_name = "";
  cmd.read(&tensor_name);


  int num = 0;
  cmd.read(&num);

  CBucket bucket = CBucket(tensor_name);
  bucket.shape = {2, 2, 2};
  bucket.read(&data, num);

  int res = 1;
  con.write(&res);
}
