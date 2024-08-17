from airflow import DAG
from airflow.operators.bash import BashOperator

def subdag_downloads(parent_dag_id, child_dag_id, args):
    with DAG(
        dag_id=f"{parent_dag_id}.{child_dag_id}",
        description="Subdag to download files",
        schedule_interval=args["schedule_interval"],
        catchup=args["catchup"],
        start_date=args["start_date"]
    ) as dag:

        download_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 10'
        )

        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 10'
        )

        download_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 10'
        )

        return dag
