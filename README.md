dockerfiles
===========

This repository contains NFs implemented by the authors of the GLANF framework.

loadsim
========

This NF behaves as `glanf/wire` does, but with additional delay added and load
performed for each packet which passes through the device. This is meant to
simulate devices which have inherent baseline latency which they add and which
perform processing per packet.

The amount of "processing" performed per packet scales exponentially according
to a load factor, which can be tweaked by configuring the `LOAD_FACTOR`
environment variable (which can be a floating point value). The amount of
processing performed is equal to `LOAD_FACTOR * ( 2 ** LOAD_FACTOR)` which has
the nice property that it scales from 0 to a large number very quickly.

The delay is added to outgoing packets on both interfaces.

An example invocation is as follows:

```
docker run -itd --cap-add=NET_ADMIN --env="LOAD_FACTOR=8.0" --env="DELAY=2ms" glanf/loadsim
```
