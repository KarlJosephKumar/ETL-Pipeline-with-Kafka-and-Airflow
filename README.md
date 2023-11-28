# ETL-Pipeline-with-Kafka-and-Airflow

Small final project for 'ETL and Data Pipelines with Shell, Airflow and Kafka' by IBM certificate, part of the IBM Data Engineering Professional Certificate.

Projet is made in IBM docker environment.

## Key learnings:
- Extracting data from different files
- Transforming and combining data
- Loading to database
- Data pipeline
- Workflow management with Airflow
- Creating DAGs
- Data streaming and reading
- Storing streamed data
- Monitoring DAGs and streams

## Technologies used:
- Apache Airflow
- Apache Kafka
- Apache Zookeeper
- Python
- MySQL

## Preview:

### Creating a DAG:

1. I imported relevant libraries and then defined DAG arguments:

![dag_args](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/a90ae197-3937-4e7c-b7f8-3dc2a90623a8)

2. Defined a DAG with DAG id, schedule, default arguments and gave description:

![dag_definition](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/28415107-1599-4c67-b11e-f5412cc54c27)

3. Creating tasks.

Unzipped a given file that contains data of toll plaza in CSV, TSV and Fixed Width text file.

Extracted necessary information and created CSV files out of them.

![data_extraction](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/f401e025-02ad-4d98-9930-e3a6743a8f82)


Combined all created CSV files into one.  


![combination_of_data](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/c516a78f-fa5e-4900-bcd8-91ad7d1c07d3)


Transformed the vehicle types in the combined file into uppercase.

![transformedDAta](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/828dd5e9-2e3e-4a11-934f-7fda4a33c43c)

Finally combined the pipeline of all of the tasks.

![pipeline](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/ca26dc6d-a9db-4158-9833-2ea66f34cf82)


4. Submit and monitor DAG

Submitted the dag, unpaused and ran it.

![dag_runs](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/d16532b3-1ea4-46d2-95d7-cdb427565f7d)


