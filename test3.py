from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/")  # Acessar a página do Flask

url = driver.current_url
assert url == "http://127.0.0.1:5000/"

driver.execute_script("alert('Teste');")  # Rolar para baixo

time.sleep(5)

alert = driver.switch_to.alert
alert.accept()  # Aceitar o alerta

time.sleep(3)

driver.quit()
