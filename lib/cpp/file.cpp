#ifndef FILE
#define FILE

#include "file.h"
#include "buffer.cpp"

// Main class for writing/reading tensors (and other types in the future).
// Cncurrent writes and reads will be supported.
File::File() {}
File::~File() {
  close(fd);
}

File::File(std::string file_path, int offset=-1) {
  fd = ::open(file_path.c_str(), O_RDWR | O_CREAT, 0666);
  
  // TODO: extract this to separate function
  file_offsets.insert({file_path, new std::atomic<int>(0)});
  file_offset = file_offsets[file_path];

  if(offset == -1) {
    int eof_offset = lseek(fd, 0, SEEK_END);
    file_offset->fetch_add(eof_offset, std::memory_order_relaxed);
  }
}

void File::_write(void *src, int len, int offset) {
  pwrite(fd, src, len, file_offset->load());
  file_offset->fetch_add(offset, std::memory_order_relaxed);
}

void File::_write_at(void *src, int len, int offset) {
  pwrite(fd, src, len, offset);
}

int File::_read(void* dst, int len, int offset) {
  return pread(fd, dst, len, offset);
}

#endif