{
    # name of the software we fuzz
    "name": "unrealircd",

    # which version of the software are we fuzzing (optional)
    "version": "4.0.17",

    # additional comment about this project (optional)
    "comment": "",

    # Path to target
    "target_bin": "bin/unrealircd/bin/unrealircd",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "-F",

    # if you cant specify the port on the command line,
    # hardcode it here. Note that it will work only with one fuzzing instance.
    "target_port": 6661,

    # how many fuzzing instances should we start
    "processes": 1,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",

    "use_netnamespace": True,
    "honggpath": "/Development/honggfuzz/honggfuzz",
}
