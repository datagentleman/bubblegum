#! /bin/sh

cd lib/

rm -r ./build
rm -r ./*.so

python3 setup.py build_ext
cp build/lib.macosx-13-arm64-cpython-311/starbucks/lib/* ./
