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

#include "buffer.h"

// this will allow us to use pwrite() in concurrent manner.
// Each thread will get different offset for it's data and
// we shouldn't have any conflicts ;)
//
// TODO: this will be map for each tensor. We must have write_offset for each opened tensor.
static std::atomic<int> file_offset(0);

class File : public ReaderWriter {
  public:
    // main file descriptor for our tensor
    int fd;

    File();
    File(std::string file_path);

    void _write(void *data_src, int size, int offset) override;
    void _read(void *dst, int len, int offset) override;
};

#endif
