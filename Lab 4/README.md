# Lab 4: Create a container

This project benchmarks 3 types of containers: a handmade container, LXC container and Docker container. All of the containers tested here were running on ubuntu 16.04 i386.

## Getting started

### Prerequisites

* LXD
* Docker
* Sysbench
* GCC compiler

1. Clone the repo

    ```bash
    git clone https://github.com/Sh1co/Total-Virtualization-Labs
    ```

2. Go to lab directory

    ```bash
    cd '.\Lab 4\'
    ```

### My container

1. Move to a new mount namepace

    ```bash
    sudo unshare --mount
    ```

2. Run the start script

    ```bash
    sudo sh start.sh
    ```

Option: To change the functionality of the container, you can change the start() function in process_start.c. start() is the first function that gets called in the new container.

### Docker container

1. Build Dockerfile

    ```bash
    docker build -t docker-test .
    ```

2. Use docker image in a docker container

### LXC

Make sure you have LXD setup

1. Create LXC container

    ```bash
    sudo lxc launch ubuntu/16.04 c1
    ```

2. Push benchmark script to container

    ```bash
    sudo lxc file push benchmark.sh c1/
    ```

3. Get shell access to the container

    ```bash
    sudo lxc exec c1 bash
    ```

4. Install sysbench and its dependencies

    Note: if your container is not setup to have internet access you will need to push the sysbench and its dependencies packages to the container and install them offline

5. Go to the root directory

    ```bash
    cd ..
    ```

6. Run the benchmark

    ```bash
    sh benchmark
    ```

## Benchmarks

### Tests

1. CPU test
2. File IO test
3. Memory test
4. Threads test

### Results

All benchmark results are stored in the Results folder.

You can check the benchmark.sh file for more details
