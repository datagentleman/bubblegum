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
};