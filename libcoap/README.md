# libcoap 

Example libcoap project.
* Feedback driven fuzzing with software
* Example network data included

## Install

```
make requirements
make download
make compile
```

## Example data 

Input data, corpus and crashes are available in:
* in.orig/
* out.orig/

## Fuzzing

```
python /ffw/ffw.py --config config.py --basedir /ffw --honggmode
```

