
all: requirements download compile

download:
	mkdir bin corpus crashes temp verified
	git clone https://github.com/ngircd/ngircd.git
	cd ngircd; git checkout e17d4bdec7857e7af9deb02681585fad15eb1ebd
	apt-get -y install autoconf automake


compile:
	cd ngircd; CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc ./autogen.sh
	cd ngircd; CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc ./configure
	cd ngircd; CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc  HFUZZ_CC_ASAN="true"  make
	cp ngircd/src/ngircd/ngircd bin/
	cp ffw-ngircd.conf bin/
	
fuzz1:
	python /ffw/ffw.py --config config1.py --basedir /ffw --honggmode

fuzz2:
	python /ffw/ffw.py --config config2.py --basedir /ffw --honggmode

fuzz3:
	python /ffw/ffw.py --config config3.py --basedir /ffw --honggmode

fuzz4:
	python /ffw/ffw.py --config config4.py --basedir /ffw --honggmode

fuzz5:
	python /ffw/ffw.py --config config5.py --basedir /ffw --honggmode


clean:
	rm -f bin/mqtt_broker
	rm -f mqtt_client
	cd mongoose/examples/mqtt_broker; make clean
