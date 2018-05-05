
all: requirements download patch compile

requirements:
	apt-get -y install autoconf automake pkg-config libtool
	mkdir bin crashes corpus temp verified

download:
	git clone https://github.com/obgm/libcoap.git

	# go to tested version
	cd libcoap; git checkout 4cf5ff0c63c986611b85badafcdc8c8a88cdfe9a

patch:
	echo "patch"

compile:
	export HFUZZ_CC_ASAN="true"
	export CC="/Development/honggfuzz/hfuzz_cc/hfuzz-gcc"

	cd libcoap; ./configure --disable-dtls --disable-documentation
	cd libcoap; make

	# required to put the damn libcoap library into correct location
	cd libcoap; make install
	ldconfig

	# why is everyone hiding their damn executables?
	cp libcoap/examples/.libs/coap-server bin/

fuzz:
	python /ffw/ffw.py --config config.py --basedir /ffw --honggmode

clean:
	rm -f bin/coap-server
	cd libcoap; make clean
