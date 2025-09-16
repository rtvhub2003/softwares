#!/bin/bash

# Get the current kernel version
KERNEL_VERSION=$(uname -r)

# Define the modules directory path
MODULES_DIR="/lib/modules"

# Create the target directory if it doesn't exist
mkdir -p "$MODULES_DIR/$KERNEL_VERSION"

# Move all other module directories except the current one
echo "Renaming other module directories to match the kernel version..."
for dir in "$MODULES_DIR"/*; do
    if [[ "$dir" != "$MODULES_DIR/$KERNEL_VERSION" ]]; then
        mv "$dir" "$MODULES_DIR/$KERNEL_VERSION/"
    fi
done

# Update module dependencies
echo "Updating module dependencies..."
depmod "$KERNEL_VERSION"

echo "Module directories moved and dependencies updated successfully."
