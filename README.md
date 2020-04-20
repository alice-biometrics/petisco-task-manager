# petisco-task-manager :cookie:  [![ci](https://github.com/alice-biometrics/petisco-task-manager/workflows/ci/badge.svg)](https://github.com/alice-biometrics/petisco-task-manager/actions)

<img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/alice_header.png" width=auto>

Flask Petisco Application Example. Use [petisco :cookie:](https://github.com/alice-biometrics/petisco) to help you developing clean applications.

## Table of Contents
- [Application :rocket:](#application-rocket)
- [Installation :computer:](#installation-computer)
- [Testing :white_check_mark:](#testing-white_check_mark)
- [Contact :mailbox_with_mail:](#contact-mailbox_with_mail)


## Application :rocket:

The Application is a very simple **Task Manager** with the following entry points:

- `POST /task`: Create a task, return a `task_id` :white_check_mark:
- `GET /task`: Get a task from its `task_id` :white_check_mark:
- `GET /task`: Get all tasks (TODO :recycle:)
- `PUT /task/priority`: Change task priority (TODO :recycle:)

## Installation :computer:

Use [lume :fire:](https://github.com/alice-biometrics/lume) to install dependencies:

Example:

```console
>> conda create -n myenv python=3.6
>> conda activate myenv
(myenv) >> lume -install # pip install lume if needed
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

## Contact :mailbox_with_mail:

support@alicebiometrics.com

