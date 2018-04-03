# Mongoose 6.9 MQTT

Example Mongoose 6.9 MQTT project.
* Server patched so it supports ports
* Feedback driven fuzzing with software
* Example network data included

## Install

```
make requirements
make download
make patch
make compile
```

## Network data

A sample network traffic capture is stored as `data_0.pickle`.
Just copy/move it to the `in/` directory to start fuzzing.
Alternatively, you can intercept it by yourself.


## Fuzzing

```
python /ffw/ffw.py --config config.py --basedir /ffw --honggmode
```
