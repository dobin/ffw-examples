
all: requirements download compile

requirements:
	mkdir -p bin corpus crashes temp verified
	apt install -y libssl-dev

download:
	git clone https://github.com/cesanta/mongoose.git
	# go to version 6.9
	cd mongoose; git checkout 6.9

compile:
	# compile with honggfuzz compiler, and enabled asan
	cd mongoose/examples/mqtt_broker; make HFUZZ_CC_ASAN="true" CC="/Development/honggfuzz/hfuzz_cc/hfuzz-gcc"
	cp mongoose/examples/mqtt_broker/mqtt_broker bin/


fuzz:
	python /ffw/ffw.py --config config.py --basedir /ffw --honggmode

clean:
	rm -f bin/mqtt_broker
	rm -f mqtt_client
	cd mongoose/examples/mqtt_broker && make clean
	rm -f corpus/* verified/* crashes/*
