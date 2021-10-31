from scraper import notebooks_list
from fastapi import FastAPI
import json


app = FastAPI()


@app.get(r"/bot")
def start_bot():
    notebooks_list()
    return "Processo finalizado, acesse /bot/data para visualizar os resultados"


@app.get("/bot/data")
def results():

    with open('data.json', 'r') as a:
        data = json.load(a)
    return data

#uvicorn main:app --reload
