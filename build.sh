#! /bin/sh

cd starbucks/cython/

# removing /build directory would reload all libraries, including c++ ones
rm -r ./build

python3 setup.py build_ext --inplace
