import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URI = (
    f"postgresql+psycopg2://{os.getenv('PGUSER','etl_user')}:"
    f"{os.getenv('PGPASSWORD','etl_pass')}@"
    f"{os.getenv('PGHOST','localhost')}:"
    f"{os.getenv('PGPORT','5432')}/"
    f"{os.getenv('PGDATABASE','etl_db')}"
)

engine = create_engine(DB_URI)

def run_query(sql, params=None):
    with engine.connect() as conn:
        return conn.execute(text(sql), params or {})
