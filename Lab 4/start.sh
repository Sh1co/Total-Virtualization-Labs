#! /bin/bash

# exit when any command fails
set -e

# Create new file system
sudo sh create_fs.sh
echo "New filesystem created!"

# Copy files into container
cp process_start.c fs
cp benchmark.sh fs

#Run main process
cd fs
gcc process_start.c -o process_start
./process_start


