from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

url = driver.current_url
assert url == "https://www.google.com/"

driver.execute_script("alert('Teste');")  # Rolar para baixo

time.sleep(5)

alert = driver.switch_to.alert
alert.accept()  # Aceitar o alerta

time.sleep(3)

driver.quit()
