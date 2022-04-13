import mariadb

from config import database_config


def db_connection():
    return mariadb.connect(**database_config)
    connection = None
    try:
        connection = mariadb.connect(**database_config)
        yield connection
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return
    finally:
        if connection is not None:
            connection.close()
        return


