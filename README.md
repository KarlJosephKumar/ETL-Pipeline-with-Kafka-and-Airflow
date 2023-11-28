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

### Creating Streaming Data Pipelines using Kafka

1. Created a MySQL database with a table to store data in MySQL database.

![db_creation](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/c72b23fd-e6f3-42cf-acea-da9fb013db3e)


2.
Downloaded Kafka from https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

Extracted and started Zookeeper for brokers by running 'bin/zookeeper-server-start.sh config/zookeeper.properties' command

Started Kafka broker service by running 'bin/kafka-server-start.sh config/server.properties' command

Created a topic called 'toll' by running 'bin/kafka-topics.sh --create --topic toll --bootstrap-server localhost:9092'

Ran the toll_traffic_generator which simulated a random stream of data.

Output:

![sim_output](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/3945e6a8-3d17-43b1-9030-6f5aa581cd82)


Then ran streaming_data_reader to read that data and insert it into the table created in MySQL database.

Output:

![data_reader_output](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/9ea88004-7005-47c0-b9c0-605e24219028)

Here's top 10 lines from the database:

![output_rows](https://github.com/KarlJosephKumar/ETL-Pipeline-with-Kafka-and-Airflow/assets/41339304/3c475f30-0e23-43aa-acc4-f5ece0b81630)

