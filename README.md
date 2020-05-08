# petisco-task-manager :cookie:  [![ci](https://github.com/alice-biometrics/petisco-task-manager/workflows/ci/badge.svg)](https://github.com/alice-biometrics/petisco-task-manager/actions) ![ci-end2end](https://github.com/alice-biometrics/petisco-task-manager/workflows/ci-end2end/badge.svg)

<img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/alice_header.png" width=auto>

Flask Petisco Application Example. Use [petisco :cookie:](https://github.com/alice-biometrics/petisco) to help you developing clean applications.

## Table of Contents
- [Use this template :v:](#use-this-template-v)
- [Application :rocket:](#application-rocket)
- [Installation :computer:](#installation-computer)
- [Testing :white_check_mark:](#testing-white_check_mark)
- [Configuration :gear:](#configuration-gear)
- [Local Deploy :zap:](#local-deploy-zap)
- [Contact :mailbox_with_mail:](#contact-mailbox_with_mail)


## Use this template :v:

1. Click `Use this template` in Github Web :octocat:

2. Once in the root package, install requirements:

```console
>> conda create -n myenv python=3.6
>> conda activate myenv
(myenv) >> pip install lume
(myenv) >> lume -install
```
3. Then, you can change project name with `petisco` :cookie:

```console
(myenv) >> petisco --rename-template myservice
```
If you want to change another time the name, just type:

```console
(myenv) >> petisco --rename-template brandnewname --original-template-name myservice 
```

## Application :rocket:

The Application is a very simple **Task Manager** with the following entry points:

- `POST /task`: Create a task, return a `task_id` :white_check_mark:
- `GET /task`: Get a task from its `task_id` :white_check_mark:
- `GET /events`: Get all events :white_check_mark:
- `GET /tasks`: Get all tasks (TODO :recycle:)
- `PUT /task/priority`: Change task priority (TODO :recycle:)

## Installation :computer:

Use [lume :fire:](https://github.com/alice-biometrics/lume) to install dependencies:

Example:

```console
>> conda create -n myenv python=3.6
>> conda activate myenv
(myenv) >> pip install lume
(myenv) >> lume -install
```

## Testing :white_check_mark:

### Unit, Integration and Acceptance

```console
(myenv) >> lume -test
```

### End-to-end [python]

```console
(myenv) >> lume -test-e2e-local-python
```

### End-to-end [docker-compose]

```console
(myenv) >> lume -test-e2e-local
```

## Configuration :gear:

Application can be configured by *environment variables*.

* Petisco :cookie:
  * `PETISCO_PORT: "8080"`
* Persistence 💾:
  * inmemory:
    - `TASK_REPOSITORY_TYPE: inmemory`
    - `EVENT_REPOSITORY_TYPE: inmemory`
  * sqlite:
    - `TASK_REPOSITORY_TYPE: sqlite`
    - `EVENT_REPOSITORY_TYPE: sqlite`
    - `SQL_SERVER: sqlite`
    - `SQL_DATABASE: taskmanager_test.db`
  * mysql:
    - `TASK_REPOSITORY_TYPE: mysql`
    - `EVENT_REPOSITORY_TYPE: mysql`
    - `SQL_SERVER: mysql`
    - `SQL_DATABASE: taskmanager`
    - `MYSQL_DATABASE: taskmanager`
    - `MYSQL_USER: root`
    - `MYSQL_PASSWORD: root`
    - `MYSQL_HOST: mysql`
    - `MYSQL_PORT: 3306`
* Event Manager <img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/rabbitmq.png" width="16">
:
  * `EVENT_PUBLISHER_TYPE: "rabbitmq"` (By default it uses a not implemented event manager)
  * `EVENT_SUBSCRIBER_TYPE: "rabbitmq"` (By default it uses a not implemented event manager)
  * `RABBITMQ_USER: "guest"`
  * `RABBITMQ_HOST: "localhost"`
  * `RABBITMQ_PORT: "5672"`
  
## Local Deploy :zap:

You can run all the stack using docker-compose and lume.

```
lume -run-local
```

You can access both the message broker and the database with the following applications:

* RabbitMQ <img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/rabbitmq.png" width="16">: [http://localhost:15672/](http://localhost:15672/)
    * Username: guest 
    * Password: guest
* Adminer (MySQL): [http://localhost:8090/?server=mysql&username=root&db=eventmanager](http://localhost:8090/?server=mysql&username=root&db=taskmanager)
    * System: MySQL
    * Server: mysql
    * Username: root 
    * Password: root
    * Database: taskmanager

These default values might change if you modify environment variables.

## Contact :mailbox_with_mail:

support@alicebiometrics.com

