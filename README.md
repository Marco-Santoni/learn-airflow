to launch al containers

```bash
docker-compose up -d
```

Test your airflow tasks by running the following command:

```bash
# to list processes
docker-compose ps
# to move inside the container that hosts the scheduler
docker exec -it materials-airflow-scheduler-1 /bin/bash
# now you are inside
airflow@fd4f0d45bc7f:/opt/airflow$
# you can here use Airflow CLI, example
airflow@fd4f0d45bc7f:/opt/airflow$ airflow tasks test marco_processing create_table

# or you can connect to Postgres container
docker exec -it materials-postgres-1 /bin/bash
# thenn connect to db
psql -U airflow
```
