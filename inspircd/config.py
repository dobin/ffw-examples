{
    # name of the software we fuzz
    "name": "inspircd",

    # which version of the software are we fuzzing (optional)
    "version": "v2.0.26",

    # additional comment about this project (optional)
    "comment": "https://github.com/inspircd/inspircd.git",

    # Path to target
    "target_bin": "inspircd/run/bin/inspircd",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "--nofork --config=/ffw-examples/inspircd/bin/inspircd.conf --runasroot",

    # if you cant specify the port on the command line,
    # hardcode it here. Note that it will work only with one fuzzing instance.
    "target_port": 6668,

    # how many fuzzing instances should we start
    "processes": 4,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",

    "use_netnamespace": True,
    "honggpath": "/Development/honggfuzz/honggfuzz",
}
