# sales-data-pipeline

This repository contains an Airflow DAG that implements a Sales Data Pipeline with ETL (Extract, Transform, Load) operations and data analysis in a PostgreSQL database. The pipeline processes sales data by creating necessary tables, inserting customer and sales data, and performing various analyses on the data, including:
- Total sales per customer
- Total sales by product
- Average sales per customer

## Prerequisites
1. Apache Airflow
2. PostgreSQL
3. Python Packages: 
- apache-airflow
- airflow.providers.postgres
- psycopg2 (for PostgreSQL interaction)
- PostgreSQL Connection in Airflow: Set up a PostgreSQL connection in Airflow, referenced as postgres_conn.




## Workflow
- The DAG runs daily (@daily).
- It begins by creating tables in the PostgreSQL database.
- Next, customer and sales data are inserted into the corresponding tables.
- Finally, the DAG performs three types of analyses on the sales data:
- Total sales per customer
- Total sales by product
- Average sales per customer
- These analyses are written as SQL queries executed via PostgreSQL operators.

