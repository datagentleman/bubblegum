// taking 2 bytes from bytes and converting them to uint16.
uint16_t to_uint16(char* bytes, bool big_endian=true) {
  if (big_endian) {
    return (bytes[0] << 8) | bytes[1];
  }
}

