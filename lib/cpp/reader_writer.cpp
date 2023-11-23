#ifndef READER_WRITER
#define READER_WRITER

#include "utils.cpp"

// TODO: consider different naming
class ReaderWriter {
  public:
    int write_offset = 0;
    int read_offset  = 0;
    int header_size  = 4;

    virtual ~ReaderWriter() {}

    // implemented by children (File, Buffer, ...)
    virtual void _write(void *src, int len, int offset)    {}
    virtual void _write_at(void *src, int len, int offset) {}
    virtual void _read(void  *dst, int len, int offset)    {}

    // WRITER
    void write_at(void *src, int len, int offset) {
      _write_at(src, len, offset);
    }

    template <typename T>
    void write(std::vector<T> *src, bool header=true) {
      if(header) write_header(container_size(src));
      write_data(src->data(), container_size(src));
    }

    void write(int *src) {
      write_data(src, sizeof(*src));
    }

    void write(int src) {
      write_data(&src, sizeof(src));
    }

    void write(std::string *src) {
      write_header(src->size());
      write_data(src, src->size());
    }

    void write(unsigned char *src, int len, bool header=true) {      
      if(header) write_header(len);
      write_data(src, len);
    }

    void write(void *src, int len, bool header=true) {      
      if(header) write_header(len);
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

    // READER
    void read_at(void *dst, int len, int offset) {
      _read(dst, len, offset);
    }

    template <typename T>
    void read(std::vector<T> *dst) {
      int elems = read_header();
      int len   = read_header();

      dst->resize(elems);
      read_data(dst->data(), len);
    }

    void read(int *dst) {
      read_data(dst, 4);
    }

    void read(std::string *dst) {
      int len = read_header();
      dst->resize(len);
      read_data(dst, len);
    }

    void read(void *dst) {
      int len = read_header();
      read_data(dst, len);
    }

    int read_header() {
      int len = 0;
      _read(&len, header_size, read_offset);
      read_offset += header_size;
      return len;
    }

    void read_data(void *src, int len) {
      _read(src, len, read_offset);
      read_offset += len;
    }
};

#endif