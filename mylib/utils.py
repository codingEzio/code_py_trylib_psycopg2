def conn_status(client):
    if client.status == 1:
        print("Connected successfully 😀")
    else:
        print("Connection error.")


def cursor_status(cursor):
    if cursor.closed is False:
        print("Cursor opened successfully 😀")
    else:
        print("Cursor error.")
