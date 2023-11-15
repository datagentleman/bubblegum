#ifndef FILE
#define FILE

#include "file.h"
#include "buffer.cpp"

// Main class for writing/reading tensors (and other types in the future).
// Cncurrent writes and reads will be supported.
File::File() {}

File::File(std::string file_path) {
  fd = ::open(file_path.c_str(), O_CREAT| O_RDWR, 0666);
  
  int eof_offset = lseek(fd, 0, SEEK_END);
  file_offset.fetch_add(eof_offset, std::memory_order_relaxed);
}

void File::_write(void *src, int len, int offset) {
  pwrite(fd, src, len, file_offset.load());
  file_offset.fetch_add(len, std::memory_order_relaxed);
}

void File::_read(void* dst, int len, int offset) {
  pread(fd, dst, len, offset);
}

#endif