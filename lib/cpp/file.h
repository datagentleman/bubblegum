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
static std::map<std::string, std::atomic<int> *> file_offsets;

class File : public ReaderWriter {
  public:
    int fd;
    std::atomic<int> *file_offset;

    File();
    File(std::string file_path, int offset);

    void _write(void *data_src, int size, int offset)    override;
    void _write_at(void *data_src, int size, int offset) override;
    void _read(void *dst, int len, int offset)           override;
};

#endif
