from dotenv import load_dotenv
from utils import get_connection
import pandas as pd

load_dotenv()

connection = get_connection()

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT tasa_x_moneda('GBP')"
        cursor.execute(sql)
        df = pd.DataFrame(cursor.fetchall())

print(df)
