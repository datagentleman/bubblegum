#ifndef CONN
#define CONN 

#include <iostream>
#include <string>
#include <fcntl.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include "buffer.cpp"
#include "utils.cpp"
#include "reader_writer.cpp"

using namespace std;

// class for handling sockets and user connections
// TODO: rename this class (make all cpp classes consistent)
class conn : public ReaderWriter {
  public:
    int sock;

    conn() {}

    // It's possible to create sockets from already existing fd (file descriptors).
    // In most cases existing_fd will be client socket that is already connected to our node.
    conn(int existing_fd) {
      create_socket(existing_fd);
    }

    template <typename... Items>
    void write_all(Items... items) {
      buffer buf = buffer();
      (buf.write(items), ...);

      _write(buf.data(), container_size(buf.vec()), 0);
    }

    void _write(void *data_src, int size, int offset) {
      auto bytes_send = send(sock, data_src, size, MSG_WAITALL);
    }

    int _read(void *dst, int size, int offset) {
      // TODO: MSG_WAITALL could potentially block forever if message is too large ? 
      return recv(sock, dst, size, MSG_WAITALL);
    }

    void blocking_mode() {
      int flags = fcntl(sock, F_GETFL, 0);
      flags &= ~O_NONBLOCK;
      fcntl(sock, F_SETFL, flags);
    }

  private:
    void create_socket(int existing_fd) {
      sock = socket(AF_INET, SOCK_STREAM, 0);

      // after that we can recv/send on our socket
      dup2(existing_fd, sock);
    }
};

#endif