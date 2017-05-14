#!/usr/bin/env bash
####################################################
## Git pull latest Puppet modules
####################################################


# get input
while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -p|--path)
    PUPPET_PATH="$2"
    shift # past argument
    ;;
    *)
    echo "get_latest.sh actually takes one argument -p"
    ;;
esac
shift
done
echo Puppet Path  = "${PUPPET_PATH}"

# check if puppet path exists
if [ ! -d ${PUPPET_PATH} ]; then
    echo "${PUPPET_PATH} does not exists, please retry."
    exit 1
fi

# git pull latest latest puppet codes
cd ${PUPPET_PATH}
git pull
make
if [[ $? -eq 1 ]] ; then
    echo "Error when git pull"
    exit 1
fi

exit 0