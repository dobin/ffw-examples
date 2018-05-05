{
    # name of the software we fuzz
    "name": "Cesanta Mongoose",

    # which version of the software are we fuzzing (optional)
    "version": "6.9",

    # additional comment about this project (optional)
    "comment": "MQTT",

    # enable namespaces (required root, and possibly nesting)
    "use_netnamespace": True,

    # Path to target
    "target_bin": "bin/mqtt_broker",

    # target arguments
    # separate arguments by space
    # keywords: ""%(port)i" is the port the server will be started on
    "target_args": "",

    # the port the server uses
    "target_port": 1883,

    # how many fuzzing instances should we start
    "processes": 2,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",

    "honggpath": "/Development/honggfuzz/honggfuzz",

    "restart_server_every": 10,
}
