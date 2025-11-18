# Architecture Overview

This project implements a modern end-to-end ETL data pipeline with automation and dashboard visualization.

## 1. Data Flow
1. **Source Layer**
   - CSV file or external API
   - Stored in `data/`

2. **Extraction Layer**
   - Python script (`etl/extract.py`)
   - Reads raw data and prepares it for transformation
   - Airflow extracts and saves staging data as pickle files

3. **Transformation Layer**
   - Python script (`etl/transform.py`)
   - Cleans, converts, adds computed columns (e.g., revenue)
   - Output saved to a staging pickle

4. **Loading Layer**
   - Python script (`etl/load.py`)
   - Loads transformed data into PostgreSQL warehouse

5. **Warehouse Layer**
   - PostgreSQL database
   - Accessed using SQLAlchemy (`warehouse/postgres_client.py`)

6. **Orchestration Layer**
   - Airflow DAG (`dags/example_etl_dag.py`)
   - Daily scheduled pipeline: extract → transform → load

7. **Visualization Layer**
   - Streamlit dashboard (`dashboard/app.py`)
   - Real-time querying of warehouse for insights

## 2. Components
- **Airflow** → Automation & scheduling  
- **PostgreSQL** → Storage & analytics  
- **Python ETL scripts** → Data manipulation  
- **Streamlit** → BI & dashboard  

## 3. High-Level Diagram (Text Version)

