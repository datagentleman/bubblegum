#include <vector>

#include "utils.cpp"

class buffer {
  public:
    std::vector<unsigned char> buf;

    buffer() {}
    buffer(unsigned char* b) {
      buf.resize(20);
      std::memcpy(buf.data(), b, 20);
    };

    // read next packet
    int read(unsigned char *dst, int len) {  
      return 0;
    };

    int len() {
      return buf.size();  
    };

    unsigned char* data() {
      return buf.data();
    };

  private:
    void _read(void *dst, int offset, int len) {
      std:memcpy(dst, buf.data()+offset, len);

      // we must remove bytes that we just read
      auto first = buf.begin() + offset ;
      auto last  = buf.begin() + offset + len;
      
      buf.erase(first, last);
    }
};