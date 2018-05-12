{
    # name of the software we fuzz
    "name": "vulnserver",

    # which version of the software are we fuzzing (optional)
    "version": "",

    # additional comment about this project (optional)
    "comment": "Intentionally vulnerable server",

    # enable namespaces (required root, and possibly nesting)
    "use_netnamespace": True,

    # Path to target
    "target_bin": "bin/vulnserver_hfuzz",

    # target arguments
    # separate arguments by space
    # keywords: "%(port)i" is the port the server will be started on
    "target_args": "",

    # the port the server uses
    "target_port": 5001,

    # how many fuzzing instances should we start
    "processes": 1,

    # "tcp" or "udp" protocol?
    "ipproto": "tcp",

    "honggpath": "/Development/honggfuzz/honggfuzz",

    "restart_server_every": 1000,
}
