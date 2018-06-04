export HFUZZ_CC_ASAN=1

all: requirements download compile

requirements:
	mkdir -p bin crashes corpus temp verified
	apt install dos2unix

download:
	git clone https://github.com/inspircd/inspircd.git
	cd inspircd; git checkout v2.0.26
	# wow, cool that git/patch is able to handle \r\n... not!
	dos2unix inspircd/src/inspircd.cpp
	patch -p0 < inspircd.patch
	unix2dos inspircd/src/inspircd.cpp

compile:
	cd inspircd; ./configure --disable-interactive --prefix=/ffw-examples/inspircd/bin/ --config-dir=/ffw-examples/inspircd/bin/ --module-dir=/ffw-examples/inspircd/bin/ --uid=daemon --with-cc=/Development/honggfuzz/hfuzz_cc/hfuzz-clang++
	cd inspircd; make
	cd inspircd; make install

fuzz:
	rm -f corpus/*
	cp corpus.init/* corpus/
	python /ffw/ffw.py --config config.py --basedir /ffw --honggmode

test:
	rm -f corpus/*
	cp corpus.init/* corpus/
	python /ffw/ffw.py --config config.py --basedir /ffw --test
