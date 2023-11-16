// TODO: consider different naming
class ReaderWriter {
  public:
    int write_offset = 0;
    int read_offset  = 0;
    int header_size  = 4;

    void write(void *src, int len, bool with_header=true) {      
      if(with_header) write_header(len);
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
      int len = 0;
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
