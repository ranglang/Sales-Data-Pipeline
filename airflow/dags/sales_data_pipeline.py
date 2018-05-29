from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import sys
import os

# Calculate the start date
current_date = datetime.utcnow() - timedelta(days=5)
# Set Spark path
sparkSubmit = os.getcwd() + '/bin/spark-submit'

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


script_path = os.path.join(os.path.dirname(__file__), '../src/setup_java.sh')
setup_java = """
. {{params.script_path}}
"""

task_setup_java = BashOperator(task_id='task_dummy',
                               bash_command=setup_java,
                               params={'script_path': script_path},
                               dag=sales_data_pipeline)

task_spark_test = BashOperator(task_id='spark_test',
                               bash_command=sparkSubmit + ' ' + '--master spark://master:7077 ../src/test.py',
                               dag=sales_data_pipeline)


# Set dependencies
task_spark_test.set_upstream(task_setup_java)
