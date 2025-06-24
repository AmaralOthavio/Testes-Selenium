from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    contact_name = request.form['contact_name']
    message = request.form['message']

    # Configurar o ChromeDriver
    driver_path = './chromedriver-win64/chromedriver.exe'  # Altere para o caminho correto
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # Acessar o WhatsApp Web
    driver.get("https://web.whatsapp.com")

    # Aguarde o usuário escanear o código QR
    input("Pressione Enter após escanear o código QR")

    wait = WebDriverWait(driver, 10)  # Espera até 10 segundos

    try:
        # Localizar o campo de busca de contatos
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='3']")))
        print("Campo de busca de contatos encontrado.")
        search_box.click()
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.RETURN)

        # Aguarde um pouco para garantir que a conversa carregue
        time.sleep(7)  # Você pode ajustar ou remover isso se usar esperas explícitas

        # Localizar o campo de mensagem
        message_box = wait.until(EC.presence_of_element_located(
(By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")  # '10' é mais comum agora
        ))

        print("Campo de mensagem encontrado.")
        message_box.click()
        message_box.send_keys(message)

        # Espera e clica no botão de envio
        send_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@data-icon='send']")
        ))
        print("Botão de envio encontrado.")
        send_button.click()

        return "Mensagem enviada!"
    except Exception as e:
        print(f"Erro: {str(e)}")
        return f"Erro: {e}."
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
