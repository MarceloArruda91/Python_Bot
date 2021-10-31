import glob
import json
import os

from bot.scraper import notebooks_list
from datetime import datetime
from fastapi import APIRouter

router = APIRouter()


@router.get(r"/bot")
def start_bot():
    notebooks_list()
    return "Processo finalizado, acesse /bot/data para visualizar os resultados"


@router.get("/bot/data")
def results():
    """
    Pega o arquivo mais recente da pasta files e retorna na rota em questao
    """
    list_of_files = glob.glob('files/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    last_update = os.path.getctime(latest_file)
    with open(latest_file, 'r') as a:
        content = json.load(a)

    return {"response": 200,
            "last_update": datetime.utcfromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S'),
            "content": content}
