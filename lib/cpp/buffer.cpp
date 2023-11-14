#ifndef BUFFER
#define BUFFER 

#include <vector>
#include "buffer.h"
#include "utils.cpp"

buffer:: buffer() {}
 
// read next packet
int buffer::read(unsigned char *dst, int len) {  
  // read data length 
  int16_t size;
  _read(&size, 0, header_size);

  // read data
  _read(dst, 0, size);
  return size;
}

// write data from src to buffer
void buffer::write(void* src, int len) {
  buf.resize(buf.size() + header_size + len);

  _write(&len, header_size);
  _write(src, len);
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

// write data from src to buffer
void buffer::_write(void* src, int size) {
  auto dst = buf.data() + write_offset;
  memcpy(dst, src, size);  

  write_offset += size;
}

// read bytes from buffe to dst. We are removing consumed bytes.
// TODO: check boundaries. Add read_offset !!!
void buffer::_read(void *dst, int offset, int num_bytes) {
  memcpy(dst, buf.data() + offset, num_bytes);

  // we must remove bytes that we just read
  auto start = buf.begin() + offset;
  auto end   = start + num_bytes;

  buf.erase(start, end);
}

#endif