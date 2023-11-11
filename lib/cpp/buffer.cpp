#ifndef BUFFER
#define BUFFER 

#include <vector>

#include "utils.cpp"

using namespace std;

class buffer {
  public:
    std::vector<unsigned char> buf;
    
    // Since we are using std::memcpy we must track current offset while writing
    // data to our vector.
    //
    // If that will become problematic, I will replace it with something else, 
    // probably push_back() 
    int write_offset = 0;

    buffer() {}
    buffer(unsigned char* b, int len) {
      buf.resize(len);
      memcpy(buf.data(), b, len);
    };

    // read next packet
    int read(unsigned char *dst, int len) {  
      // read data length 
      int16_t size;
      _read(&size, 0, 2);

      // read data
      _read(dst, 0, size);
      return size;
    }

    void write(void* data, int len) {
      int16_t total_len = 6;
      int16_t data_len  = len;

      buf.resize(len + sizeof(total_len) + sizeof(data_len));
      
      _write(&total_len, 2);
      _write(&data_len, 2);
      _write(data, len);
    }

    int len() {
      return buf.size();  
    }

    unsigned char* data() {
      return buf.data();
    }

  private:
    void _write(void *data, int size) {
      auto data_ptr = buf.data() + write_offset; 
      
      std::memcpy(data_ptr, data, size);
      write_offset += size;
    }

    // TODO: check boundaries 
    void _read(void *dst, int offset, int len) {
      memcpy(dst, buf.data() + offset, len);

      // we must remove bytes that we just read
      auto start = buf.begin() + offset;
      auto end   = start + len;

      buf.erase(start, end);
    }
};

#endif