#!/usr/bin/env bash
####################################################
## Start up Groot Web Server
####################################################


if [ ! -d "../log" ]; then
  mkdir ../log
fi

pid=$(ps -ef | grep 8888 | grep "Main" | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    kill ${pid}
fi

nohup python ../src/Main.py 8888 >> ../log/console.log &