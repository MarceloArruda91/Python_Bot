# Devnology_Test

Bot em selenium com o objetivo acessar esse site e pegar todos notebooks Lenovo ordenando do mais barato para o mais caro. Pegar todos os dados disponíveis dos produtos.


# Requisitos do bot:
```
fastapi==0.70.0
selenium==4.0.0
```
## Funcionamento
```bash

# Entrar no root folder e executar o comando:
uvicorn main:app --reload

# Para inicializar o bot acesse:
localhost:8000/bot

# Assim que o bot for executado, os resultados estarão disponíveis na rota:
localhost:8000/bot/data

```