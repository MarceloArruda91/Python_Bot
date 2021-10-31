# Devnology_Test

Bot em selenium com o objetivo acessar [esse site](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops), pegar todos notebooks Lenovo ordenando do mais barato para o mais caro e pegar todos os dados disponíveis dos produtos.


# Requisitos do bot:
```
fastapi==0.70.0
selenium==4.0.0

```

Baixar o [chromedriver](https://chromedriver.chromium.org/downloads) da versão correta e por na pasta drive

## Funcionamento
```bash

# Entrar no root folder e executar o comando:
uvicorn main:app --reload

# Para inicializar o bot acesse:
localhost:8000/bot

# Assim que o bot for executado, os resultados estarão disponíveis na rota:
localhost:8000/bot/data

```
