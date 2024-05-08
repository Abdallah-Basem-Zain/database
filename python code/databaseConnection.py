import mysql.connector


db_config = {
    'host': '127.0.0.1',
    'database': 'MainSchema',
    'user': 'root',
    'password': 'root'
}


def connect_to_db():
    return mysql.connector.connect(**db_config)

