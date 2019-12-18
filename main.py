from mylib.utils import conn_status, cursor_status
from psycopg2 import connect

conn = connect("dbname=trypsycopgdb user=trypsycopg")
cur = conn.cursor()
conn_status(conn)
cursor_status(cur)

TABLE_NAME = "table1st_basic_usage"
SAMPLE_DATA = (100, "abcdef")

cur.execute(
    f"CREATE TABLE {TABLE_NAME}"
    f"(id serial PRIMARY KEY, num integer, data varchar)"
    f";"
)

cur.execute(f"INSERT INTO {TABLE_NAME} (num, data) VALUES {SAMPLE_DATA}")

cur.execute(f"SELECT * FROM {TABLE_NAME}")
cur.fetchone()

conn.commit()

cur.close()
conn.close()
