
mkdir bin corpus crashes verified temp

git clone https://github.com/joric/nanoircd.git
cd nanoircd

export HFUZZ_CC_ASAN=1
/Development/honggfuzz/hfuzz_cc/hfuzz-clang nanoircd.c -o nanoircd
cp nanoircd ../bin
