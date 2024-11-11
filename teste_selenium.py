from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurar o serviço e as opções do Chrome
_options = webdriver.ChromeOptions()
# _options.add_argument("--headless")  # Executa em modo headless (opcional)
_options.add_argument("--disable-extensions")  # Desativa extensões para melhorar o desempenho

# Inicializar o WebDriver com o serviço configurado
service = Service(ChromeDriverManager().install())
page = webdriver.Chrome(service=service, options=_options)

# Definir tempo máximo de espera para os elementos
wait = WebDriverWait(page, 10)

try:
    # Acessar a URL
    url = "https://www.4devs.com.br/gerador_de_pessoas"
    page.get(url)

    # Esperar até que o campo de entrada esteja presente e inserir "cpf"
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div/form/input")))
    input_field.send_keys("cpf")

    # Esperar até que o botão de gerar esteja presente e clicar
    generate_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/form/button")))
    generate_button.click()

    # Esperar até que o link de pessoas geradas esteja presente e clicar
    person_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/div[1]/div[2]/ul/li[2]/a")))
    person_link.click()

    # Esperar o conteúdo desejado na classe `app-info` antes de capturar a página
    app_info = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app-info")))

    # Obter o código-fonte da página e analisar com BeautifulSoup
    page_source = page.page_source
    html = BeautifulSoup(page_source, "html.parser")
    app_info_content = html.find(class_='app-info')

    # Extrair e imprimir o primeiro parágrafo encontrado na classe `app-info`
    if app_info_content and app_info_content.find_all('p'):
        print(app_info_content.find_all('p')[0].get_text())
    else:
        print("Nenhum parágrafo encontrado.")

finally:
    # Fechar o navegador ao final
    page.quit()
