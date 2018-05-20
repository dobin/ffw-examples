mkdir bin corpus temp crashes verified

wget http://libmodbus.org/releases/libmodbus-3.0.6.tar.gz
	tar xvfz libmodbus-3.0.6.tar.gz
	patch < multiclient.patch
	cd libmodbus-3.0.6

export CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc
export HFUZZ_CC_ASAN=1

./configure
make
cd ..

cp libmodbus-3.0.6/tests/.libs/unit-test-server bin/
cp libmodbus-3.0.6/src/.libs/libmodbus.so.5 bin/

export LD_LIBRARY_PATH="/ffw-examples/libmodbus/bin/:$LD_LIBRARY_PATH"

