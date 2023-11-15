#ifndef BUFFER
#define BUFFER 

#include <vector>
#include "buffer.h"
#include "utils.cpp"

buffer::buffer()  {}
buffer::~buffer() {};

unsigned char buffer::operator[](int index) {
  return buf[index];
} 

int buffer::size() {
  return buf.size();
}

unsigned char* buffer::data() {
  return buf.data();
}

// write data from src to buffer
void buffer::_write(void* src, int len, int offset) {
  buf.resize(buf.size() + len);

  auto dst = buf.data() + offset;
  memcpy(dst, src, len);  
}

// read bytes from buffe to dst. We are removing consumed bytes.
void buffer::_read(void *dst, int num_bytes, int offset) {
  memcpy(dst, buf.data(), num_bytes);

  // we must remove bytes that we just read
  auto start = buf.begin();
  auto end   = start + num_bytes;

  buf.erase(start, end);
}

#endif