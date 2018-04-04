
all: requirements download compile

requirements:
	mkdir bin in out temp verified

download:
	git clone https://github.com/cesanta/mongoose.git

	# go to version 6.8
	cd mongoose; git checkout 6.8

compile:
	cd mongoose/examples/mqtt_client; make
	cp mongoose/examples/mqtt_client/mqtt_client .

	# enable address sanitizer. Note that it is required to use CFLAGS_EXTRA,
	# not just CFLAGS, as compiling mongoose will fail
	cd mongoose/examples/mqtt_broker; make CFLAGS_EXTRA="-fsanitize=address"
	cp mongoose/examples/mqtt_broker/mqtt_broker bin/


fuzz:
	python /ffw/ffw.py --config config.py --basedir /ffw --fuzz

clean:
	rm bin/mqtt_broker
	rm mqtt_client
	cd mongoose/exmples/mqtt_broker; make clean
