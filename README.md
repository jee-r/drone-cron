# drone-cron
This is a script that you can put in your cron table for automacly re-run the last build of your repos in drone.io

## requirements

    - python3
    - drone account
    - drone-cli
    - cron or all others task scheduler that you can pass a python script

## usage

copy the `config-sample.py` file to `config.py` edit it as your need.

add the full path of the `app.py` file in your task scheduler
