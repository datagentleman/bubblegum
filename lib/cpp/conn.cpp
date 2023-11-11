#ifndef CONN
#define CONN 

#include <iostream>
#include <string>
#include <sys/socket.h>

#include "buffer.cpp"

using namespace std;

void test(buffer buf, int sock) {
  send(sock, buf.data(), buf.len(), 0);
}

// class for handling sockets and user connections
class conn {
  public:
    int sock;

    conn() {}

    // It's possible to create sockets from already existing fd (file descriptors).
    // In most cases existing_fd will be client socket that is already connected to our node.
    conn(int existing_fd) {
      create_socket(existing_fd);
    }

    // msg can be anything compatible with std::memcpy
    void write(void* msg, int len) {
      buffer buf = buffer();
      buf.write(msg, len);
    }

  private:
    void create_socket(int existing_fd) {
      sock = socket(AF_INET, SOCK_STREAM, 0);

      // after that we can recv/send on our sock
      dup2(existing_fd, sock);
    }
};

#endif