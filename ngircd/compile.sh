#!/bin/bash

mkdir bin corpus crashes verified temp

git clone https://github.com/ngircd/ngircd.git
cd ngircd
git checkout fb760d94736897aea32bf81a864d87a150015276

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
cp corpus.init/* corpus/
