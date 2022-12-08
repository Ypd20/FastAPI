import psycopg2

def get_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="Ypd@2010",
                                  host="localhost",
                                  port="5432",
                                  database="python_db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to PostgreSQL version: ", db_version)
        close_connection(connection)
        
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()
