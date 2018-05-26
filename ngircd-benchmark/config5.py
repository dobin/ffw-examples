{
    # name of the software we fuzz
    "name": "ngircd",

    # which version of the software are we fuzzing (optional)
    "version": "e17d4bdec7857e7af9deb02681585fad15eb1ebd",

    # additional comment about this project (optional)
    "comment": "",

    # Path to target
    "target_bin": "bin/ngircd",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "--nodaemon -f ffw-ngircd.conf",

    # if you cant specify the port on the command line,
    # hardcode it here. Note that it will work only with one fuzzing instance.
    "target_port": 6669,

    # how many fuzzing instances should we start
    "processes": 256,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",
    "recvTimeout": 0.1,

    "use_netnamespace": True,
    "honggpath": "/Development/honggfuzz/honggfuzz",
}
