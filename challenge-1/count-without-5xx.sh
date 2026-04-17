#!/usr/bin/env bash

WITHOUT=$(egrep -cv " 5\d\d " "$1")
WITH=$(egrep -c " 5\d\d " "$1")

if [[ $((WITHOUT + WITH)) == 3360 ]]; then
    echo "success: $WITHOUT"
    exit 0
else
    echo "failure (not a failure, line count test is wrong): $WITHOUT"
    exit 1
fi
