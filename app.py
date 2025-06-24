from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    # Localizar o campo de busca de contatos
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.RETURN)

    # Aguarde um pouco para garantir que a conversa carregue
    time.sleep(2)

    # Localizar o campo de mensagem
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.RETURN)

    # Fechar o navegador
    driver.quit()

    return "Mensagem enviada!"

if __name__ == '__main__':
    app.run(debug=True)
