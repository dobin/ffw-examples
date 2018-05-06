mkdir bin corpus crashes verified temp

wget https://www.unrealircd.org/unrealircd4/unrealircd-4.0.17.tar.gz
tar xvfz unrealircd-4.0.17.tar.gz

cp config.settings unrealircd-4.0.17/

export HFUZZ_CC_ASAN=1
export CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc

cd unrealircd-4.0.17
apt-get install -y libssl-dev

export LIBS="-ldl"
export CC=/Development/honggfuzz/hfuzz_cc/hfuzz-clang
export HFUZZ_CC_ASAN=1

./Config
make
make install
cd ..

cp unrealircd.conf bin/unrealircd/conf

