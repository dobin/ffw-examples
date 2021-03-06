{
    # name of the software we fuzz
    "name": "Cesanta Mongoose",

    # which version of the software are we fuzzing (optional)
    "version": "6.8",

    "use_netnamespace": True,

    # additional comment about this project (optional)
    "comment": "MQTT",

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

    "restart_server_every": 32,
}
