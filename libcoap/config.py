{
    # name of the software we fuzz
    "name": "libcoap",

    # which version of the software are we fuzzing (optional)
    "version": "ff848928173c80516713b4de8c0ffe64c25198ec",

    # additional comment about this project (optional)
    "comment": "https://github.com/obgm/libcoap",

    # Path to target
    "target_bin": "bin/coap-server",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "-A 127.0.0.1 -p %(port)i",

    # if you cant specify the port on the command line,
    # hardcode it here. Note that it will work only with one fuzzing instance.
    "target_port": 1883,

    # how many fuzzing instances should we start
    "processes": 1,

    # "tcp" or "udp" protocol?
    "ipproto": "udp",

    "honggpath": '/Development/honggfuzz/honggfuzz'
}
