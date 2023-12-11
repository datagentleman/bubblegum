#include <chrono>
#include <thread>
#include "conn.cpp"
#include "buffer.cpp"
#include "bucket.cpp"
#include "timer.cpp"


void f(int fd) {
  std::thread::id threadId = std::this_thread::get_id();

  conn   con  = conn(fd);
  buffer buf  = buffer();
  buffer data = buffer();

  TIMER_BEGIN(socket_read);
  int l = con.read_all(buf.vec());
  TIMER_END(socket_read);

  // TODO: we should just return 0 here
  // if(len > 0) {
  
  std::string tensor_name = "";
  buf.read(&tensor_name);

  TIMER_BEGIN(tput);
  
  // Set socket to blocking mode 
  // TODO: extract this
  int flags = fcntl(con.sock, F_GETFL, 0);
  flags &= ~O_NONBLOCK;
  fcntl(con.sock, F_SETFL, flags);
  
  // TODO: use Tensor.put() here
  CBucket bucket = CBucket(tensor_name);
  
  buf.read(data.vec());
  bucket.write(&data); 

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

  std::thread::id threadId = std::this_thread::get_id();
}