# Wire Functionality

FROM glanf/base
MAINTAINER Kyle White

ENTRYPOINT ifinit && brctl addbr br0 && brctl addif br0 if1 && brctl addif br0 if2 && ifconfig dev br0 up && /bin/bash

