#!/usr/bin/env bash
####################################################
## Start up Groot Web Server
####################################################

# get input
while [[ $# -gt 1 ]]
do
key="$1"
case $key in
    -p|--path)
    BASE_PATH="$2"
    shift # past argument
    ;;
    *)
    echo "start.sh actually takes one argument -p"
    ;;
esac
shift
done
echo Base Path  = "${BASE_PATH}"

if [ ! -d "${BASE_PATH}/log" ]; then
  mkdir ${BASE_PATH}/log
fi

pid=$(ps -ef | grep 8888 | grep -i "Main.py" | grep -v grep | awk '{print $2}')

if [ -n "$pid" ]; then
    kill ${pid}
    echo "Kill previous process."
fi

nohup python27 ${BASE_PATH}/Main.py 8888 --base-path=${BASE_PATH} >> ${BASE_PATH}/log/console.log 2>&1 &