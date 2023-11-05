#include <sys/socket.h>

// class for handling sockets and user connections
class Conn {
public:
  int sock;

  // It's possible to create sockets from already existing fd (file descriptors).
  // In most cases existing_fd will be client socket that is already connected to node.
  Conn(int existing_fd) {
    create_socket(existing_fd);
  }

private:
  void create_socket(int existing_fd) {
    sock = socket(AF_INET, SOCK_STREAM, 0);

    // now we can use recv/send on our sock
    dup2(existing_fd, sock);
  }
};
