from dotenv import load_dotenv
import pymysql.cursors
import os
import pandas as pd

load_dotenv()


# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=f'{os.getenv("PASSWORD")}',
    database="dbdatabanco",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT tasa_x_moneda('GBP')"
        cursor.execute(sql)
        df = pd.DataFrame(cursor.fetchall())

print(df)
