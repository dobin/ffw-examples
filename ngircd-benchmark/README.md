# NGIRCD - Benchmark

## Issues

### Nickname

If we always use the same nickname, NGIRCD will deny us
(nick already used). The code in `protocol.py` will change
the used nickname `dobin` to a random value.

### Timeouts

We need to specify this in the config:
```
DefaultUserModes = i
```
So that we dont have a timeout here.

And, or, remove penalty calculation in the source code.
See `ngircd.patch`.

We'll also increase the default timeout from 0.03 to 0.1.
