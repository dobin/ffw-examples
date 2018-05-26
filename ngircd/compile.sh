#!/bin/bash

mkdir crashes verified temp

git clone https://github.com/ngircd/ngircd.git
cd ngircd
git checkout e17d4bdec7857e7af9deb02681585fad15eb1ebd

export HFUZZ_CC_ASAN=1
export CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc
patch -p0 < ngircd.patch
apt-get -y install autoconf automake
./autogen.sh
./configure
make

cp src/ngircd/ngircd ../bin/
cd ..
cp ffw-ngircd.conf bin/
