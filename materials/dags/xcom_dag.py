from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import BranchPythonOperator

from datetime import datetime

def _t1(task_instance):
    task_instance.xcom_push(key="my_key", value=42)

def _t2(task_instance):
    print(task_instance.xcom_pull(task_ids='t1', key='my_key'))

def _branch(task_instance):
    value = task_instance.xcom_pull(task_ids='t1', key='my_key')
    if value == 42:
        return 't3'
    else:
        return 't2'

with DAG("xcom_dag", start_date=datetime(2022, 1, 1),
    schedule_interval='@daily', catchup=False) as dag:

    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )

    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )

    t3 = BashOperator(
        task_id='t3',
        bash_command="echo ''"
    )

    t4 = BashOperator(
        task_id='t4',
        bash_command="echo ''",
        trigger_rule='one_success'
    )

    t1 >> branch >> [t2, t3] >> t4
