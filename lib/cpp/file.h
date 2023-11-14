#ifndef FILE_H
#define FILE_H

#include <atomic>
#include <iostream>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <vector>
#include <numeric>

// this will allow us to use pwrite() in concurrent manner.
// Each thread will get different offset for it's data and
// we shouldn't have any conflicts ;)
static std::atomic<int> write_offset = 0;

class File {
  public:
    // main file descriptor for our tensor
    int fd;

    File();
    File(std::string file_path);

    int write(unsigned char* src, int len, int offset);
    int read(void* dst, int len, int offset);
};

#endif
