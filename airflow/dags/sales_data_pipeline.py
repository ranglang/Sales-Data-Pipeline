from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from src.get_customer_geo_dist import get_customer_geo_dist

import sys
import os

# Calculate the start date
current_date = datetime.utcnow() - timedelta(days=5)
# Set Spark path
sparkSubmit = '/home/wenyixu/spark-2.3.0-bin-hadoop2.7/bin/spark-submit'
srcDir = os.getcwd() + '/../src/'

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
sale_data_pipeline = DAG('weebly-v0', schedule_interval=timedelta(minutes=5), catchup=False, default_args=default_args)

task_dummy = BashOperator(task_id='task_dummy',
                          bash_command='touch os.path.dirname(__file__)/../../data/out/test.txt',
                          dag=sale_data_pipeline)

task_spark_test = BashOperator(task_id='spark_test',
                               bash_command=sparkSubmit + ' ' + srcDir + 'test.py',
                               dag=sale_data_pipeline)

# task_dummy = PythonOperator(task_id='get_customer_geo_dist',
#                             python_callable=get_customer_geo_dist,
#                             op_args=[customer_file, customer_geo_dist_file],
#                             provide_context=False,
#                             dag=sale_data_pipeline)
