
all: requirements download compile

requirements:
	mkdir -p bin corpus crashes temp verified
	mkdir -p fuzz1 fuzz2 fuzz3 fuzz4 fuzz5
	cp ffw-ngircd.conf bin/

download:
	git clone https://github.com/ngircd/ngircd.git
	cd ngircd; git checkout e17d4bdec7857e7af9deb02681585fad15eb1ebd
	apt-get -y install autoconf automake

compile:
	cd ngircd; CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc ./autogen.sh
	cd ngircd; CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc ./configure
	cd ngircd; CC=/Development/honggfuzz/hfuzz_cc/hfuzz-gcc  HFUZZ_CC_ASAN="true"  make
	cp ngircd/src/ngircd/ngircd bin/


fuzz:
	# fuzz1
	rm -f corpus/*
	cp corpus.init/* corpus/
	timeout --foreground --preserve-status 10s python /ffw/ffw.py --config config1.py --basedir /ffw --honggmode; echo "Fuzz1"
	mv fuzzer_stats plot_data fuzz1/
	sleep 60
	# fuzz2
	rm -f corpus/*
	cp corpus.init/* corpus/
	timeout --foreground --preserve-status 1h python /ffw/ffw.py --config config2.py --basedir /ffw --honggmode; echo "Fuzz2"
	mv fuzzer_stats plot_data fuzz2/
	sleep 60
	# fuzz3
	rm -f corpus/*
	cp corpus.init/* corpus/
	timeout --foreground --preserve-status 1h python /ffw/ffw.py --config config3.py --basedir /ffw --honggmode; echo "Fuzz3"
	mv fuzzer_stats plot_data fuzz3/
	sleep 60
	# fuzz4
	rm -f corpus/*
	cp corpus.init/* corpus/
	timeout --foreground --preserve-status 1h python /ffw/ffw.py --config config4.py --basedir /ffw --honggmode; echo "Fuzz4"
	mv fuzzer_stats plot_data fuzz4/
	sleep 60
	# fuzz5
	rm -f corpus/*
	cp corpus.init/* corpus/
	timeout --foreground --preserve-status 1h python /ffw/ffw.py --config config5.py --basedir /ffw --honggmode; echo "Fuzz5"
	mv fuzzer_stats plot_data fuzz5/

clean:
	rm -f bin/mqtt_broker
	rm -f mqtt_client
	cd mongoose/examples/mqtt_broker; make clean
