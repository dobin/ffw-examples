# Mongoose 6.8 MQTT

Example Mongoose 6.8 MQTT project.
* Server not patched (not possible to define port, therefore only one fuzzing process possible)
* Feedback driven fuzzing not tested
* Example, simple network data included (from `mqtt_client`)


## Install

```
make requirements
make download
make compile
```

## Network data

A sample network traffic capture is stored as `data_0.pickle`.
Just copy/move it to the `in/` directory to start fuzzing.
Alternatively, you can intercept it by yourself.

### Intercept

Listen on port 10'000, as server cannot change port:
```
$ python /ffw/ffw.py --config config.py --intercept --listenport 10000

Client Manager
Network Server Manager
Interceptor listen on port: 10000
Target server port: 1883
MQTT broker started on 0.0.0.0:1883
Check if we can connect to server localhost:1883
Forwarding everything to localhost:1883
Waiting for new client on port: 10000
```

Start client:
```
./mqtt_client -h localhost:10000
Subscribing to '/stuff'
Subscription acknowledged, forwarding to '/test'
```

Result:
```
Client Thread0 started
Received from client: 0: 19
target: recv data
Received from server: 0: 4
Received from client: 0: 13
target: recv data
Received from server: 0: 5
ClientTcpThread terminating
Got 4 packets
Storing into file: /ffw-examples/mongoose-6.8/in/data_0.pickle
```

## Fuzzing

```
python /ffw/ffw.py --config config.py --basedir /ffw --fuzz
```
