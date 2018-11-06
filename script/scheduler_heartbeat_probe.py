import os
from sys import exit
from sqlalchemy import create_engine

# get database details
postgres_user = os.environ['POSTGRES_USER']
postgres_password = os.environ['POSTGRES_PASSWORD']
postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_PORT']
postgres_db = os.environ['POSTGRES_DB']

# create connection string
sql_alchemy_conn="postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    postgres_user,
    postgres_password,
    postgres_host,
    postgres_port,
    postgres_db
        )

# set the airflow Database copnnection string before importing
os.environ['AIRFLOW__CORE__SQL_ALCHEMY_CONN'] = sql_alchemy_conn

from airflow import configuration
from airflow.utils import timezone

# Check that the heartbeat it recent
heartbeat_interval = configuration.getint('scheduler', 'SCHEDULER_HEARTBEAT_SEC')
eng = create_engine(sql_alchemy_conn)

with eng.connect() as con:
    if (timezone.utcnow() - con.execute("""SELECT MAX(latest_heartbeat) FROM job WHERE job_type = 'SchedulerJob'""")
            .fetchone()[0]).seconds > heartbeat_interval+5:
        exit(1)
    else:
        exit(0)
