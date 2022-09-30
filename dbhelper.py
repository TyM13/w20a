import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
        host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("operational error", error)
    except Exception as error:
        print("unknown error", error)


def execute_statment(cursor, statement, list_of_args=[]): #list of args becomes optional defaults to an empty list
    try:
        cursor.execute(statement)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as error:
        print('programming error', error)
    except mariadb.IntegrityError as error:
        print('integrity error', error)
    except mariadb.DataError as error:
        print('data error', error)
    except Exception as error:
        print('unknown error', error)



def close_connect(cursor):
    try:
        conn = cursor.connection
        cursor.close
        conn.close()
    except mariadb.OperationalError as error:
        print('operational error', error)
    except mariadb.InternalError as error:
        print('internal error', error)
    except Exception as error:
        print('unknown error', error)