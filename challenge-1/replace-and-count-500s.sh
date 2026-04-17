#!/usr/bin/env bash

sed 's/ 503 / 500 /' sample.log | egrep -c " 500 "