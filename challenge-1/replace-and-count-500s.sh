#!/usr/bin/env bash

sed 's/ 503 / 500 /' "$1" | grep -c " 500 "