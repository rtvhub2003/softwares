#!/bin/bash

user=$(whoami)
pass=""

cd /home/root/papis/update/
lsfw=$(ls /home/root/papis/update/ | grep .upd)
echo "File: $lsfw is available"

chmod 777 $PWD/$lsfw
unzip -o $lsfw

cp -R $PWD/mpu_final /opt/mpu_final/bin/
chmod a+x /opt/mpu_final/bin/mpu_final
rm -r /home/root/papis/update/*


# start mpu
/opt/mpu_final/bin/mpu_final &

# monitor application

check_process() {
  echo "$ts: checking $1"
  [ "$1" = "" ]  && return 0
  [ `pgrep -n $1` ] && return 1 || return 0
}

while [ 1 ]; do 
   #timestamp
  ts=`date +%T`

  echo "$ts: begin checking..."
  check_process "mpu_final"
 [ $? -eq 0 ] && echo "$ts: not running, restarting..." && `/opt/mpu_final/bin/mpu_final &`
  sleep 5
done

