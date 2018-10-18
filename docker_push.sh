#!/bin/bash
AIRFLOW_VERSION=1.10.0
# tag
docker tag transformersreg11.azurecr.io/airflow:${AIRFLOW_VERSION} transformersreg11.azurecr.io/airflow:${AIRFLOW_VERSION}
docker push transformersreg11.azurecr.io/airflow:${AIRFLOW_VERSION}
