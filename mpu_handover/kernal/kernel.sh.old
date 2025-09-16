#!/bin/bash

# Get the current kernel version
KERNEL_VERSION=$(uname -r)

# Define the modules directory path
MODULES_DIR="/lib/modules"

# Rename the module directory to match the kernel version
echo "Renaming module directory to match the kernel version..."
mv "$MODULES_DIR"/* "$MODULES_DIR/$KERNEL_VERSION"

# Update module dependencies
echo "Updating module dependencies..."
depmod "$KERNEL_VERSION"

echo "Module directory renamed and dependencies updated successfully."
