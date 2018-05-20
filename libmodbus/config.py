{
    # name of the software we fuzz
    "name": "libmodbus",

    # which version of the software are we fuzzing (optional)
    "version": "3.0.6",

    # additional comment about this project (optional)
    "comment": "http://libmodbus.org/download/",

    # Path to target
    "target_bin": "bin/unit-test-server",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "",

    # if you cant specify the port on the command line,
    # hardcode it here. Note that it will work only with one fuzzing instance.
    "target_port": 1502,

    # how many fuzzing instances should we start
    "processes": 1,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",

    "mutator": [ 'Radamsa' ],
    "use_netnamespace": True,
    "honggpath": "/Development/honggfuzz/honggfuzz",
}
