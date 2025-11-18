from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd

from etl.extract import extract_from_csv
from etl.transform import transform_sales
from etl.load import load_to_postgres

def extract_task(**_):
    df = extract_from_csv("/opt/airflow/data/sample_input.csv")
    df.to_pickle("/opt/airflow/data/extracted.pkl")

def transform_task(**_):
    df = pd.read_pickle("/opt/airflow/data/extracted.pkl")
    df = transform_sales(df)
    df.to_pickle("/opt/airflow/data/transformed.pkl")

def load_task(**_):
    df = pd.read_pickle("/opt/airflow/data/transformed.pkl")
    load_to_postgres(df)

with DAG(
    "example_etl_dag",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract_task)
    t2 = PythonOperator(task_id="transform", python_callable=transform_task)
    t3 = PythonOperator(task_id="load", python_callable=load_task)

    t1 >> t2 >> t3
