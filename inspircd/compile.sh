
mkdir bin corpus crashes verified temp

git clone https://github.com/inspircd/inspircd.git
cd inspircd

git checkout v2.0.26

export HFUZZ_CC_ASAN="true"
export CC="/Development/honggfuzz/hfuzz_cc/hfuzz-gcc"
export CPP="/Development/honggfuzz/hfuzz_cc/hfuzz-g++"

./configure --disable-interactive --prefix=/ffw-examples/inspircd/bin/ --config-dir=/ffw-examples/inspircd/bin/ --module-dir=/ffw-examples/inspircd/bin/ --uid=daemon --with-cc=/Development/honggfuzz/hfuzz_cc/hfuzz-clang++
make
make install

cd ../bin/
mkdir conf
ln -s /ffw-examples/inspircd/bin/examples/ /ffw-examples/inspircd/bin/conf/
