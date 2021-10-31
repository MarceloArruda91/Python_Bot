import json
from operator import itemgetter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# CONFIG
PATH = Service(r"C:\Chromedriver\chromedriver.exe")
OPTIONS = Options()
OPTIONS.headless = True
OPTIONS.add_argument("window-size=1920x1080")
DRIVER = webdriver.Chrome(service=PATH, options=OPTIONS)  # Create driver

    # Iterar atraves da lista de notebooks e devolver o resultado filtrado em uma lista
def notebook_links() -> list:
    #  START
    website = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"  # website
    DRIVER.get(website)
    note_brand = "lenovo"
    links_list = []
    notebook_list = DRIVER.find_elements(By.CLASS_NAME, "caption")

    for notebook in notebook_list:
        if note_brand in notebook.text.lower():
            link = notebook.find_element(By.CLASS_NAME, "title").get_attribute("href")
            links_list.append(link)
    return links_list

    # Pegar todas as informacoes do notebook na pagina atual
def notebook_info() -> list:
    notebook_list = []
    base_dict = {}
    box = DRIVER.find_element(By.CLASS_NAME, "col-md-9")  # Encontrar Div com os elementos desejados

    #  Descricao
    note_description = box.find_element(By.CLASS_NAME, "description").text
    note_description_list = note_description.split(sep=",")

    #  Checar possiveis problemas na descrição
    if "lenovo" in note_description.lower():
        note_description_list.pop(0)  # Remover titulo da descricao para nao haver repeticao
        base_dict["flag"] = "Ok"
    else:
        base_dict["flag"] = "Not OK"

    #  Titulo do artigo
    title = box.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]").text

    #  Numero de reviews
    reviews = box.find_element(By.CLASS_NAME, "ratings")
    reviews_number = reviews.text[0]

    #  Rating do artigo
    rating = len(reviews.find_elements(By.CLASS_NAME, "glyphicon-star"))
    rating_text = f"{rating}/5"  # Rating formatado

    #  Inserir elementos no dicionario
    base_dict["model"] = title
    base_dict["info"] = note_description_list
    base_dict["rating"] = rating_text
    base_dict["reviews"] = reviews_number

    #  Iterar atraves dos botoes, pegar o preco de cada um e identificar o estoque
    buttons = box.find_elements(By.CLASS_NAME, "btn")

    for button in buttons:
        notebook_dict = base_dict.copy()  # Criar uma copia do dicionario para cada HDD diferente

        if "disabled" in button.get_attribute("class"):
            button.click()
            status = "out_of_stock"

        else:
            button.click()
            status = "in_stock"

        price = box.find_element(By.CLASS_NAME, "price").text.strip("$")
        hdd_type = button.get_attribute("value")

        #  Inserir elementos no dicionario
        notebook_dict["hdd"] = hdd_type
        notebook_dict["status"] = status
        notebook_dict["price"] = float(price)

        #  Inserir dicionario na lista de notebook
        notebook_list.append(notebook_dict)

    return notebook_list

    # Iterar atraves da lista de links e devolver a informacao de cada pagina de forma organizada em um json
def notebooks_list() -> None:
    notebooks_json = []

    for link in notebook_links():  # Iterar dentro da lista de links dos notebooks e clicar em cada link
        DRIVER.get(link)
        for product in notebook_info():  # Adicionar os notebooks individualmente na lista principal
            notebooks_json.append(product)
    DRIVER.quit()

    # Organizar todos os notebooks em ordem decrescente em relação ao preço
    notebooks_sorted = sorted(notebooks_json, key=itemgetter("price"))

    with open('/files/data.json', 'w') as a:
        json.dump(notebooks_sorted, a)
