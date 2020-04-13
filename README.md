# petisco-flask-service-sample :cookie:  [![version](https://img.shields.io/github/release/alice-biometrics/petisco/all.svg)](https://github.com/alice-biometrics/petisco/releases) [![ci](https://github.com/alice-biometrics/petisco/workflows/ci/badge.svg)](https://github.com/alice-biometrics/petisco/actions) [![pypi](https://img.shields.io/pypi/dm/petisco)](https://pypi.org/project/petisco/)

<img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/alice_header.png" width=auto>

This repo illustrate how to integrate petisco on a flask sample. 

The Application is a very simple **Task Manager** with the following entry points:

- `POST /task`: Create a task, return a `task_id`
- `GET /task`: Get a task from its `task_id`
- `GET /task`: Get all tasks
- `PUT /task/priority`: Change task priority


