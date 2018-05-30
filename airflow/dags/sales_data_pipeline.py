from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import sys
import os

# Calculate the start date
current_date = datetime.utcnow() - timedelta(days=5)
# Set Spark path
sparkSubmit = '~/spark-2.3.0-bin-hadoop2.7/bin/spark-submit'

default_args = {
                'owner': 'airflow',
                'depends_on_past': False,
                'start_date': datetime(int(current_date.year), \
                                       int(current_date.month), \
                                       int(current_date.day), \
                                       int(current_date.hour), \
                                       int(current_date.minute)),
                'email': ['airflow@example.com'],
                'email_on_failure': False,
                'email_on_retry': False,
                'retries': 1,
                'retry_delay': timedelta(minutes=5)
                }

# schedule_interval="@hourly"
sales_data_pipeline = DAG('sales-data-pipeline', schedule_interval=timedelta(minutes=5), catchup=False, default_args=default_args)


script_path = '~/src/setup_env.sh'
setup_env = """
. {{params.script_path}}
"""

task_setup_env = BashOperator(task_id='setup_env',
                               bash_command=setup_env,
                               params={'script_path': script_path},
                               dag=sales_data_pipeline)


task_get_hourly_income = BashOperator(task_id='get_hourly_income',
                                     bash_command=sparkSubmit + ' ' + '--master spark://master:7077 ' + \
                                                                      '--jars ~/jars/mysql-connector-java-8.0.11.jar ' + \
                                                                      '~/src/get_hourly_income.py',
                                     dag=sales_data_pipeline)

# Set dependencies
task_get_hourly_income.set_upstream(task_setup_env)
