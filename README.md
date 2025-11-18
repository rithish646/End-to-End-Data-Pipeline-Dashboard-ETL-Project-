# End-to-End Data Pipeline + Dashboard (ETL Project)


A complete ETL pipeline that ingests data, performs transformations, loads into a PostgreSQL warehouse, and exposes a Streamlit dashboard for visualization. Orchestrated by Apache Airflow (DAG included).


## Tech stack
- Python 3.10+
- Apache Airflow (Local development via docker-compose)
- PostgreSQL (data warehouse)
- Streamlit (dashboard)
- pandas, SQLAlchemy, psycopg2


## Quick start (local)
1. Clone the repo
2. Create a virtualenv and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
