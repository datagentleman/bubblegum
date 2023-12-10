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

    void _write(void *data_src, int size, int offset) {
      send(sock, data_src, size, 0);      
    }

    int _read(void *dst, int size, int offset) { 
      return recv(sock, dst, size, MSG_WAITALL);
    }

  private:
    void create_socket(int existing_fd) {
      sock = socket(AF_INET, SOCK_STREAM, 0);

      // after that we can recv/send on our sock
      dup2(existing_fd, sock);
    }
};

#endif