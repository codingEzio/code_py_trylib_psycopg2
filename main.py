from mylib.utils import conn_status, cursor_status
from psycopg2 import connect, sql

conn = connect("dbname=trypsycopgdb user=trypsycopg")
cur = conn.cursor()
conn_status(conn)
cursor_status(cur)

TABLE_NAME = "table1st_basic_usage"
SAMPLE_DATA = {"num": 1, "data": "ONEONE"}


stmt_create_table = (
    "CREATE TABLE {table} "
    "(id serial PRIMARY KEY, num integer, data varchar);"
)
stmt_insert_record = (
    "INSERT INTO {table} (num, data) " "VALUES (%(num)s, %(data)s);"
)
stmt_select_all = "SELECT * FROM {table};"

cur.execute(
    sql.SQL(stmt_create_table).format(table=sql.Identifier(TABLE_NAME))
)

cur.execute(
    sql.SQL(stmt_insert_record).format(table=sql.Identifier(TABLE_NAME)),
    vars=SAMPLE_DATA,
)

cur.execute(
    sql.SQL(stmt_select_all).format(table=sql.Identifier(TABLE_NAME))
)
cur.fetchone()

conn.commit()

cur.close()
conn.close()
