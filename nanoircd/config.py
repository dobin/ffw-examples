{
    # name of the software we fuzz
    "name": "nanoircd",

    # which version of the software are we fuzzing (optional)
    "version": "8cd2dfb82172eccdfb9c767fcdece2fae91a96b9",

    # additional comment about this project (optional)
    "comment": "https://github.com/joric/nanoircd",

    # Path to target
    "target_bin": "bin/nanoircd",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "",

    # if you cant specify the port on the command line,
    # hardcode it here. Note that it will work only with one fuzzing instance.
    "target_port": 6667,

    # how many fuzzing instances should we start
    "processes": 4,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",

    "use_netnamespace": True,
    "honggpath": "/Development/honggfuzz/honggfuzz",
}
