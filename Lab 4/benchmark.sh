#! /bin/bash

# exit when any command fails
set -e

# CPU Test
echo "Starting cpu test!"
sysbench --test=cpu --cpu-max-prime=20000 run
echo "CPU test complete!"

# File IO Read/Write
echo "Starting file IO tests!"
sysbench --test=fileio --file-total-size=50M prepare
sysbench --test=fileio --file-total-size=50M --file-test-mode=rndrw --max-time=300 --max-requests=0 run 
sysbench --test=fileio --file-total-size=50M cleanup 
echo "File IO tests complete!"

# Memory access
echo "Starting memory test!"
sysbench --test=memory --num-threads=4 run
echo "Starting memory test complete!"

# Threads
echo "Starting threads test!"
sysbench --test=threads --thread-locks=1 --max-time=20 run
echo "Threads test complete!"
