from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Ziad',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="sales_data_pipeline_with_analysis",
    default_args=default_args,
    description="ETL pipeline with data analysis in PostgreSQL",
    start_date=datetime(2024, 12, 15),
    schedule_interval="@daily",
    catchup=False
) as dag:

    create_tables = PostgresOperator(
        task_id="create_tables",
        postgres_conn_id="postgres_conn",
        sql='/sql/create_tables.sql'
    )

    insert_customers = PostgresOperator(
        task_id="insert_customers",
        postgres_conn_id="postgres_conn",
        sql='/sql/insert_customers.sql'
    )
    insert_sales = PostgresOperator(
        task_id="insert_sales",
        postgres_conn_id="postgres_conn",
        sql='/sql/insert_sales.sql'
    )


    analyze_sales_per_customer = PostgresOperator(
        task_id="analyze_sales_per_customer",
        postgres_conn_id="postgres_conn",
        sql='/sql/total_sales_per_customer.sql'
    )

    analyze_sales_by_product = PostgresOperator(
        task_id="analyze_sales_by_product",
        postgres_conn_id="postgres_conn",
        sql='/sql/total_sales_by_product.sql'
    )

    analyze_avg_sales_per_customer = PostgresOperator(
        task_id="analyze_avg_sales_per_customer",
        postgres_conn_id="postgres_conn",
        sql='/sql/average_sales_per_customer.sql'
    )

    create_tables >> insert_customers>>insert_sales >> [analyze_sales_per_customer, analyze_sales_by_product, analyze_avg_sales_per_customer]
