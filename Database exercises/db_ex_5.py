import psycopg2
import datetime
from dateutil.relativedelta import relativedelta

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

def update_doctor_experience(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select Joining_Date from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        joining_date = cursor.fetchone()
        joining_date_1 = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
        today_date = datetime.datetime.now()
        experience = relativedelta(today_date, joining_date_1).years

        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update Doctor set Experience = %s where Doctor_Id =%s"""
        cursor.execute(sql_select_query, (experience, doctor_id))
        connection.commit()
        print("Doctor Id:", doctor_id, " Experience updated to ", experience, " years")
        close_connection(connection)

    except (Exception, psycopg2.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 5: Calculate and Update experience of all doctors  \n")
update_doctor_experience(101)
