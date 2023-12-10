#ifndef BUFFER_H
#define BUFFER_H

#include "reader_writer.cpp"

using namespace std;

class buffer : public ReaderWriter {
  public:
    std::vector<unsigned char> buf;

    int number_of_elems = 0;
    int current_size    = 0;

    buffer();
    ~buffer() override;
    int size();

    unsigned char operator[](int index);
    unsigned char* data();
    std::vector<unsigned char>* vec();

    void _write(void *data_src, int size, int offset) override;
    int _read(void *dst, int len, int offset) override;
};

#endif
