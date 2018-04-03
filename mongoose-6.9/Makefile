
all: requirements download patch compile

requirements:
	mkdir bin in out temp verified

download:
	git clone https://github.com/cesanta/mongoose.git

	# go to version 6.9
	cd mongoose; git checkout 6.9

patch:
	echo "patch"

compile:
	# enable address sanitizer
	#export HFUZZ_CC_ASAN="true"

	# compile with honggfuzz compiler
	#cd mongoose/examples/mqtt_broker; make CC="~/Development/honggfuzz/hfuzz_cc/hfuzz-gcc"
	cd mongoose/examples/mqtt_broker; make CFLAGS_EXTRA="-fsanitize=address"
	cp mongoose/examples/mqtt_broker/mqtt_broker bin/

clean:
	rm -f bin/mqtt_broker
	rm -f mqtt_client
	cd mongoose/examples/mqtt_broker; make clean
