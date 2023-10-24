from dotenv import load_dotenv
import psycopg2, os


def get_db_connection():
    conn = psycopg2.connect(
        database=os.getenv("BLOCK_DB_NAME"),
        user=os.getenv("BLOCK_DB_USER"),
        password=os.getenv("BLOCK_DB_PWD"),
        host=os.getenv("BLOCK_DB_SERVER"),
        port=os.getenv("BLOCK_DB_PORT")
    )

    return conn