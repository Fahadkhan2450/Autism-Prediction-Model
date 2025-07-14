from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

class model_input(BaseModel):
    A1_Score: int
    A2_Score: int
    A3_Score: int
    A4_Score: int
    A5_Score: int
    A6_Score: int
    A7_Score: int
    A8_Score: int
    A9_Score: int
    A10_Score: int
    age: int
    gender: int
    ethnicity: int
    jaundice: int
    austim: int 
    contry_of_res: int
    used_app_before: int
    result: float
    relation: int

autism_model = pickle.load(open("best_model.sav", "rb"))

columns = [
    "A1_Score", "A2_Score", "A3_Score", "A4_Score", "A5_Score",
    "A6_Score", "A7_Score", "A8_Score", "A9_Score", "A10_Score",
    "age", "gender", "ethnicity", "jaundice", "austim",
    "contry_of_res", "used_app_before", "result", "relation"
]

@app.post("/autism_prediction")
def autism_pred(input_parameters: model_input):
    try:
        input_data = [[
            input_parameters.A1_Score, input_parameters.A2_Score, input_parameters.A3_Score,
            input_parameters.A4_Score, input_parameters.A5_Score, input_parameters.A6_Score,
            input_parameters.A7_Score, input_parameters.A8_Score, input_parameters.A9_Score,
            input_parameters.A10_Score, input_parameters.age, input_parameters.gender,
            input_parameters.ethnicity, input_parameters.jaundice, input_parameters.austim,
            input_parameters.contry_of_res, input_parameters.used_app_before,
            input_parameters.result, input_parameters.relation
        ]]

        df = pd.DataFrame(input_data, columns=columns)
        prediction = autism_model.predict(df)[0]

        return {
            "prediction": "Has autism" if prediction == 1 else "Does not have autism"
        }

    except Exception as e:
        return {"error": str(e)}  

@app.get("/")
def root():
    return {"message": "Autism Prediction API is running"}
