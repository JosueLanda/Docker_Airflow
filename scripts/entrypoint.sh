#!/usr/bin/env bash

airflow users create \
    --role Admin \
    --username admin \
    --firstname FIRST_NAME \
    --lastname LAST_NAME \
    --email EMAIL@example.org \
    -p admin
airflow db init
airflow webserver
