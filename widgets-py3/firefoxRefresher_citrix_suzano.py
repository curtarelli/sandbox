from selenium import webdriver
import time
import urllib

x = 'apps.suzano.com.br/Citrix/suzanoWeb/'
refreshrate = 90
refreshrate = int(refreshrate)
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
driver.get("http://"+x)

while True:
    time.sleep(refreshrate)
    driver.refresh()
driver.quit()