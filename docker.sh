#!/bin/bash

docker build -t bluetti-modbus .

docker run --rm -it --entrypoint bash bluetti-modbus

# bluetti-modread -c 10.2.141.192 -p 502 -t balco260
