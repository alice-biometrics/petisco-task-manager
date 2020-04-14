# petisco-task-manager :cookie:  [![ci](https://github.com/alice-biometrics/petisco-task-manager/workflows/ci/badge.svg)](https://github.com/alice-biometrics/petisco-task-manager/actions)

<img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/alice_header.png" width=auto>

This repo illustrate how to integrate petisco on a flask sample. 

The Application is a very simple **Task Manager** with the following entry points:

- `POST /task`: Create a task, return a `task_id` :white_check_mark:
- `GET /task`: Get a task from its `task_id` :white_check_mark:
- `GET /task`: Get all tasks (TODO :recycle:)
- `PUT /task/priority`: Change task priority (TODO :recycle:)


TODO

- [ ] Configure docker compose
- [ ] Add Event Manager with RabbitMQ
- [ ] Add new entry point to show more petisco features
