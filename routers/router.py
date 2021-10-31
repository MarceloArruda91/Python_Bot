import json
from bot.scraper import notebooks_list
from fastapi import APIRouter


router = APIRouter()


@router.get(r"/bot")
def start_bot():
    notebooks_list()
    return "Processo finalizado, acesse /bot/data para visualizar os resultados"


@router.get("/bot/data")
def results():

    with open('/files/data.json', 'r') as a:
        data = json.load(a)
    return data
