#!/bin/sh
if test -z "$XDG_RUNTIME_DIR"; then
    export XDG_RUNTIME_DIR=/run/user/`id -u`
    if ! test -d "$XDG_RUNTIME_DIR"; then
        mkdir --parents $XDG_RUNTIME_DIR
        chmod 0700 $XDG_RUNTIME_DIR
    fi
fi

# wait for weston
while [ ! -e  $XDG_RUNTIME_DIR/wayland-0 ] ; do sleep 0.1; done
sleep 1
echo 0 > /sys/class/backlight/backlight/bl_power                                
echo 7 > /sys/class/backlight/backlight/brightness                              
echo 6 > /sys/class/gpio/export                                                 
echo "out" > /sys/class/gpio/gpio6/direction                                    
echo 1 > /sys/class/gpio/gpio6/value                                            
amixer set 'Headphone' 75                                                       
#echo 1 > /sys/bus/usb/devices/1-1.1.1/bConfigurationValue                       
#echo 1 > /sys/bus/usb/devices/1-1.1.2/bConfigurationValue                          


#sleep 1
#echo 1 > /sys/bus/usb/devices/1-1.1.2/bConfigurationValue
#modprobe usbserial vendor=0x1286 product=0x4e3c

#sleep 3
#pon cavli-ppp

/home/root/quectel.sh

#cd
#/opt/mpu_final/bin/mpu_prod_3 --fullscreen &
#/usr/share/cinematicexperience-1.0/Qt5_CinematicExperience --fullscreen &

