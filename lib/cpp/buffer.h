#ifndef BUFFER_H
#define BUFFER_H

using namespace std;

class buffer {
  public:
    std::vector<unsigned char> buf;

    int header_size = 2;
    int packet_size = 2;
    
    // Since we are using std::memcpy we must track current offset while writing
    // data to our vector.
    //
    // If that will become problematic, I will replace it with something else, 
    // probably push_back() 
    int write_offset = 0;

    buffer();   
    buffer(unsigned char* b, int len);
    int read(unsigned char *dst, int len); 

    template <typename T> void write(T data, int len);

    unsigned char operator[](int index);
    int size();

    unsigned char* data();

  private:
    void _write(void *data_src, int size);
    void _read(void *dst, int offset, int len);
};

#endif
