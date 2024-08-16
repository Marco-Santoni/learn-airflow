from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt") # same URI!

with DAG(
    dag_id="consumer",
    schedule=[my_file],
    start_date=datetime(2024, 8, 16),
    catchup=False
):
    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())

    read_dataset()
