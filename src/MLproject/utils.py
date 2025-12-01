import os 
import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import pickle 
import numpy as np

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


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for model_name in models:
            model = models[model_name]
            param = params.get(model_name, {})

            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_objects(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
