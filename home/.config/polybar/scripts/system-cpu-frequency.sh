#!/bin/sh

FIRST=$(cpupower frequency-info -fm | grep -oP '(?<=frequency: )([^ ]+ [^ ]+)')
SECOND=$(cpupower frequency-info -pm | grep -oP '(?<=governor ")([^ "]+)' | cut -c 1-3 | tr a-z A-Z)
echo "$SECOND:$FIRST"
