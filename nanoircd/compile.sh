
mkdir bin corpus crashes verified temp

git clone https://github.com/joric/nanoircd.git
cd nanoircd

export HFUZZ_CC_ASAN="true"
/Development/honggfuzz/hfuzz_cc/hfuzz-gcc nanoircd.c -o nanoircd
cp nanoircd ../bin
