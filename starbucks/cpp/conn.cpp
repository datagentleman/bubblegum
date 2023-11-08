#include <iostream>
#include <string>
#include <sys/socket.h>

#include "buffer.cpp"

using namespace std;

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

    void write(string msg) {
      buffer buf = buffer();
      buf.write(&msg, msg.length());

      send(sock, buf.data(), buf.len(), 0);
    }

  private:
    void create_socket(int existing_fd) {
      sock = socket(AF_INET, SOCK_STREAM, 0);

      // now we can use recv/send on our sock
      dup2(existing_fd, sock);
    }
};

