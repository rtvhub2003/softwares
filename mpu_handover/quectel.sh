#!/bin/bash

# Define paths
OVERLAY_DIR="/home/root/papis/downloads"
EXTRACT_PATH="/tmp/rootfs_overlay"
OVERLAY_FILE=""

# Find the latest valid .upd file based on the format YYYYMMDD_mpu_update_<something>.upd
for file in "$OVERLAY_DIR"/*.upd; do
    if [[ -f "$file" && "$file" =~ ^${OVERLAY_DIR}/[0-9]{8}_mpu_update_.*\.upd$ ]]; then
        # Extract the date portion and check if it's the latest
        FILE_DATE=$(basename "$file" | cut -d '_' -f1)
        if [[ -z "$OVERLAY_FILE" || "$FILE_DATE" -gt "$(basename "$OVERLAY_FILE" | cut -d '_' -f1)" ]]; then
            OVERLAY_FILE="$file"
        fi
    fi
done

# Apply overlay if a matching .upd file was found
if [ -n "$OVERLAY_FILE" ]; then
    echo "Applying root filesystem overlay update from $OVERLAY_FILE."

    # Create extraction directory and extract overlay
    mkdir -p "$EXTRACT_PATH"
    tar -xJf "$OVERLAY_FILE" -C "$EXTRACT_PATH" || { echo "Failed to extract overlay"; exit 1; }

    # Apply overlay to root filesystem, only overwriting existing files
    rsync -a "$EXTRACT_PATH"/ / || { echo "Failed to apply overlay"; exit 1; }
    
    echo "Overlay applied successfully."

    # Clean up extracted files and the overlay file
    rm -rf "$EXTRACT_PATH" "$OVERLAY_FILE"
    echo "Overlay and temporary files removed."
else
    echo "No valid .upd file found in $OVERLAY_DIR matching the format YYYYMMDD_mpu_update_<something>.upd."
fi

# Network setup
ifconfig eth0 up 
ifconfig eth0 192.168.1.100

sleep 3

echo "nameserver 8.8.8.8" > /etc/resolv.conf

sleep 2                                                               
                                                                     
echo 1 > /sys/bus/usb/devices/1-1.1.2/bConfigurationValue
                                  
# Start the LTE connection                                      
cd ~/quectel/quectel-CM/out || exit
chmod +x quectel-CM #User given permission
./quectel-CM -4 -6 -s AIRTELIOT.COM &     
                                  
sleep 10                           
                                                                
ifconfig eth0 up
ifconfig eth0 192.168.1.100                                                      
                                                                
#!/bin/bash

sleep 1                                                        
                                                                
# Start the MPU application
cd /opt/mpu_final/bin || { echo "Directory not found"; exit 1; }

# Ensure mpu_iot is executable
chmod +x ./mpu_prod_3_iot

# Run MPU application in background
./mpu_prod_3_iot --fullscreen &   

# Keep script running indefinitely
#wait


