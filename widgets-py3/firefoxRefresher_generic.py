from selenium import webdriver
import time
import urllib

x = str(input('Qual website deseja abrir e recarregar automaticamente: '))
refreshrate = input('Quantos segundos entre cada recarregada: ')
refreshrate = int(refreshrate)
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
driver.get("http://"+x)

while True:
    time.sleep(refreshrate)
    driver.refresh()
driver.quit()