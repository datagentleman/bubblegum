#ifndef BUFFER
#define BUFFER 

#include <vector>
#include "buffer.h"
#include "utils.cpp"

buffer:: buffer() {}
 
buffer::buffer(unsigned char* b, int len) {
  buf.resize(len);
  memcpy(buf.data(), b, len);
}

// read next packet
int buffer::read(unsigned char *dst, int len) {  
  // read data length 
  int16_t size;
  _read(&size, 0, header_size);

  // read data
  _read(dst, 0, size);
  return size;
}

template <typename T> 
void buffer::write(T data, int len) {
  buf.resize(header_size + len);

  _write(&len, header_size);
  _write(data, len);
}

unsigned char buffer::operator[](int index) {
  return buf[index];
} 

int buffer::size() {
  return buf.size();
}

unsigned char* buffer::data() {
  return buf.data();
}

void buffer::_write (void *data_src, int size) {
  auto dst = buf.data() + write_offset; 

  memcpy(dst, data_src, size);
  write_offset += size;
}

// TODO: check boundaries. Add read_offset !!!
void buffer::_read(void *dst, int offset, int len) {
  memcpy(dst, buf.data() + offset, len);

  // we must remove bytes that we just read
  auto start = buf.begin() + offset;
  auto end   = start + len;

  buf.erase(start, end);
}

#endif