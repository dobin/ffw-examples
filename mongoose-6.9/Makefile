
all: requirements download patch compile

requirements:
	mkdir bin corpus crashes temp verified

download:
	git clone https://github.com/cesanta/mongoose.git

	# go to version 6.9
	cd mongoose; git checkout 6.9

patch:
	echo "patch"

compile:
	# compile with honggfuzz compiler, and enabled asan
	cd mongoose/examples/mqtt_broker; make HFUZZ_CC_ASAN="true" CC="/Development/honggfuzz/hfuzz_cc/hfuzz-gcc"
	cp mongoose/examples/mqtt_broker/mqtt_broker bin/


fuzz:
	python /ffw/ffw.py --config config.py --basedir /ffw --honggmode

clean:
	rm -f bin/mqtt_broker
	rm -f mqtt_client
	cd mongoose/examples/mqtt_broker; make clean
