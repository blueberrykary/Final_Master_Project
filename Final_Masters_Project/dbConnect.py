# Connect to PostgreSQL database
import psycopg2
import traceback

def getData(query:str):
    try:
        mydb = psycopg2.connect(
        host = "localhost",
        database = "api",
        user = "postgres",
        password = "Ks126352"
        )

        cursor = mydb.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results
    except:
        print("Error occured while connecting to database or fetching data from database. Error Trace: {}".format(traceback.format_exc()))
        return []
