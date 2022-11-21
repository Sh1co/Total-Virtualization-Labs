#! /bin/bash

# exit when any command fails
set -e

echo "Checking for filesystem image!"
if ! test -f fs.img; then
	echo "Filesystem image not found! Creating a new one..."
	# Create a zeroed 100mb image using dd
	dd if=/dev/zero of=fs.img bs=1 count=0 seek=100M
	echo "100mb image created!"

	# Setup file system
	mkfs.ext4 fs.img
	echo "Filesystem created!"
fi

# Mount image to a folder fs
sudo mkdir -p fs
sudo mount -o loop fs.img fs
echo "Image mounted!"


