#ifndef BUFFER_H
#define BUFFER_H

using namespace std;

// TODO: consider different naming
class ReaderWriter {
  public:
    int write_offset = 0;
    int read_offset  = 0;
    int header_size  = 4;

    void write(void *src, int len, bool raw=false) {      
      raw ? void() : write_header(len);
      write_data(src, len);
    }

    void write_header(int len) {
      _write(&len, header_size, write_offset);
      write_offset += header_size;
    }

    void write_data(void *src, int len) {
      _write(src, len, write_offset);
      write_offset += len;
    }

    void read(void *dst) {
      int data_size = read_header();
      read_data(dst, data_size);
    }

    int read_header() {
      int16_t len;
      _read(&len, header_size, read_offset);
      read_offset += header_size;
      return len;
    }

    void read_data(void *src, int len) {
      _read(src, len, read_offset);
      read_offset += len;
    }

    virtual void _write(void *src, int len, int offset) {}
    virtual void _read(void  *dst, int len, int offset) {}

    virtual ~ReaderWriter() {}
};

class buffer : public ReaderWriter  {
  public:
    std::vector<unsigned char> buf;

    int number_of_elems = 0;
    int current_size    = 0;

    buffer();   
    ~buffer() override;
    int size();

    unsigned char operator[](int index);
    unsigned char* data();

    void _write(void *data_src, int size, int offset) override;
    void _read(void *dst, int len, int offset) override;
};

#endif
