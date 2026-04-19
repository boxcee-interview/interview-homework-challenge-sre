## Challenge 2: System information scripting

Well, I did this challenge last and it was the one which took me the longest. I went with a Python lib to get all the info I require, `psutil`.
This means the script has dependencies. And I went with `uv` as package manger.

## Dependencies
```shell
brew install uv
# Rest should work without additional setup as uv will pull missing modules on run
```

## Run
```shell
# No flags will exit non-zero and show help
./system_stats.py
```

## Run all
```shell
./system_stats.py -dcpro
# Separate (single) flag use will also work
```