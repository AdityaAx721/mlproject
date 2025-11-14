import os 
import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql 

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")  

def read_sql_data():
    logging.info("Reading data from MySQL database started")
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            db="college",
            port=3306
        )

        logging.info("Connection Established successfully ✅")

        df = pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())

        mydb.close()
        return df

    except Exception as ex:
        raise CustomException(ex, sys)
