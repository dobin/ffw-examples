export HFUZZ_CC_ASAN=1
export CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc
# export LD_LIBRARY_PATH="/ffw-examples/libmodbus/bin/:$LD_LIBRARY_PATH"

all: requirements download compile

requirements:
	mkdir -p bin corpus temp crashes verified

download:
	wget http://libmodbus.org/releases/libmodbus-3.0.6.tar.gz
	tar xvfz libmodbus-3.0.6.tar.gz
	patch -p0 <multiclient.patch

compile:
	cd libmodbus-3.0.6; ./configure
	cd libmodbus-3.0.6; make
	cp libmodbus-3.0.6/tests/.libs/unit-test-server bin/
	# cp libmodbus-3.0.6/src/.libs/libmodbus.so.5 bin/
	# again we have to install it globally... damn
	cd libmodbus-3.0.6; make install
	ldconfig

test:
	python /ffw/ffw.py --config config.py --basedir /ffw --test

fuzz:
	python /ffw/ffw.py --config config.py --basedir /ffw --honggmode
