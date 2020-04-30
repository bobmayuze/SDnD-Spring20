# SDnD-Spring20

![LOGO](logo.png)

This is Team linked list for SDnD @ RPI for spring 20

Installation Guidance
System Requirement:
Operating System: Ubuntu 16.04 or above 
CPU: 2.3 GHz * 2
Memory: 4 GB or above  
Storage: 40GB or above

For more detailed requirements, please view docker’s official [website](https://docs.docker.com/engine/install/ubuntu/#prerequisites) for more instruction.

## Step 1:  Install Docker, docker-compose, node, and npm

Open up the terminal, and run the following command. More detailed instruction could be found [here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script).

```bash
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```
Docker-compose is also required for this software to be installed properly. Please follow the command below to install docker-compose. The more detailed installation guidance could be found [here](https://docs.docker.com/compose/install/). 

```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose
```

The following command will install node and npm. For more detailed installation of node and npm, please read this node js install [documentation](https://nodejs.org/en/download/).

Enable the NodeSource repository by running the following curl as a user with sudo privileges:
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
```
Once the NodeSource repository is enabled, install Node.js and npm by typing:
```bash
$ sudo apt install nodejs
```
Verify that the Node.js and npm were successfully installed by printing their versions:
```bash
$ node --version
v10.16.3
$ npm --version
6.9.0
```

## Step 2:  Clone the repository

Open a terminal and clone the repository from the github. Make sure git is installed on the machine.

$ git clone https://github.com/bobmayuze/SDnD-Spring20.git



## Step 3:  Build and run the backend and regional server(worker)

```bash
$ cd SDnD-Spring20/
$ ./scripts/init.sh
```

Once the mongo_result_backend instance says:

mongo_result_backend    | MongoDB configured successfully. You may now connect to the DB.


Press Ctrl+C to stop the current docker-compose process. Once all containers are stopped, run the command:
```bash
$ ./scripts/init.sh
```
Once the web_backend container says:

web_backend             |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

That means the backend, database, and regional worker has been successfully created. 
Next, it is required to start a regional server as a worker to execute the jobs. Open a new terminal window and run:
```bash
$ docker exec -it sample_region celery -A task worker -l INFO -n s1 -Q sample_region_1
```
Once the worker prints:

[2020-04-25 22:48:55,366: INFO/MainProcess] Connected to amqp://rabbitmq_username:**@rabbit_mq:5672//
[2020-04-25 22:48:55,376: INFO/MainProcess] mingle: searching for neighbors
[2020-04-25 22:48:56,398: INFO/MainProcess] mingle: all alone
[2020-04-25 22:48:56,440: INFO/MainProcess] celery@s1 ready.
 
That means the worker has been successfully created.


## Step 4: Build and run frontend

Open up a new terminal and change the directory to the frontend code by the following command.

```bash
$ cd ./SDnD-Spring20/frontend/sample/
$ npm install && npm run serve
```

Once the terminal says the following content, that means the project is available at localhost:8080 via Chrome. For the installation of Chrome, please view this [website](https://www.google.com/chrome).


  App running at:
  - Local:   http://localhost:8080/
  - Network: http://172.31.29.36:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
