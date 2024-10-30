from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Import functions from scripts folder
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'crypto_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for cryptocurrency data',
    schedule_interval='@daily',  # Runs once per day
)

def run_extract(**kwargs):
    return extract_data()

def run_transform(**kwargs):
    ti = kwargs['ti']
    extracted_data = ti.xcom_pull(task_ids='extract')
    return transform_data(extracted_data)

def run_load(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform')
    load_data(transformed_data)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=run_extract,
    provide_context=True,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=run_transform,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=run_load,
    provide_context=True,
    dag=dag,
)

extract_task >> transform_task >> load_task
