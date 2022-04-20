#!/bin/bash

# set -x

echo "-->HOST: $HOST"

# wait for selenium to be ready
sleep 20

i=1
while true; do
    python load.py "$HOST" "round-$i"
    ((i++))
    sleep 5
done
