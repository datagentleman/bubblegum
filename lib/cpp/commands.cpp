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

  TIMER_BEGIN(tput);

  // TODO: use Tensor.put() here
  CBucket bucket = CBucket(tensor_name);

  TIMER_BEGIN(buf_read);
  buf.read(data.vec());
  TIMER_END(buf_read);

  TIMER_BEGIN(disk_write);
  bucket.write(&data);
  TIMER_END(disk_write);

  // TODO: only temporary. Status OK. 
  int res = 1;
  buffer b = buffer();
  b.write(&res);
  b.write(b.vec());

  con.write(b.vec());
  TIMER_END(tput);
  // }
}

void tput(int fd) {
  std::thread t(f, fd);
  t.detach();
}

void tget(int fd) {
  conn   con  = conn(fd);
  buffer buf  = buffer();
  buffer data = buffer();

  con.read_all(buf.vec());

  std::string tensor_name = "";
  buf.read(&tensor_name);

  int num = 0;
  buf.read(&num);

  // TODO: shape will be taken from tensor
  CBucket bucket = CBucket(tensor_name);
  bucket.shape = {2, 2, 2};
  bucket.read(&data, num);

  con.write(data.vec());
}
