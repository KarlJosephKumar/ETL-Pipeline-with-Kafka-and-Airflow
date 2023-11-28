from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Karl',
    'start_date': days_ago(0),
    'email': ['dummy@email.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id = 'ETL_toll_data',
    schedule_interval = timedelta(days=1),
    default_args = default_args,
    description='Apache Airflow Final Assignment',
)

unzip_data=BashOperator(
    task_id='unzip_data',
    bash_command="""mkdir -p /home/project/airflow/dags/finalassignment/destination && \
                  cd /home/project/airflow/dags/finalassignment/destination && \
                  tar -xf /home/project/airflow/dags/finalassignment/tolldata.tgz""",
    dag=dag,
)

extract_data_from_csv=BashOperator(
    task_id='extract_data_from_csv',
    bash_command="""cd /home/project/airflow/dags/finalassignment/destination/ \
    &&cut -d"," -f1-4 vehicle-data.csv > csv_data.csv""",
    dag=dag,
)

extract_data_from_tsv=BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="""cd /home/project/airflow/dags/finalassignment/destination/ \
    && tr "\t" "," < tollplaza-data.tsv | cut -d"," -f5-7 |  tr -d '\r' > tsv_data.csv""",
    dag=dag,
)

extract_data_from_fixed_width=BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="""cd /home/project/airflow/dags/finalassignment/destination/ \
    && awk -F' ' '{print $(NF-1)","$NF}' payment-data.txt > fixed_width_data.csv""",
    dag=dag,
)

consolidate_data=BashOperator(
    task_id='consolidate_data',
    bash_command="""cd /home/project/airflow/dags/finalassignment/destination/ \
        && paste -d',' csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv""",
    dag=dag,
)

transform_data=BashOperator(
    task_id='transform_data',
    bash_command = """cd /home/project/airflow/dags/finalassignment/destination/ \
    && sed 's/[^,]*/\\\\U&/4' /home/project/airflow/dags/finalassignment/destination/extracted_data.csv \
    > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv""",
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
