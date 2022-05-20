from audioop import add
from http.cookies import CookieError
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time



PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(service=Service(PATH))
site = 'sneakers'

url = 'https://www.nike.com/de/launch/t/air-zoom-flight-95-black-metallic'
login = 'https://www.nike.com/de/login'

a = False
while a:
    url = input("enter your shoes url from nike shop:\n")
    if  not "https://www.nike.com/" in url:
        print("enter a valid url")
    else:
        a= True

#driver.get(url)
driver.get(login)
time.sleep(1)
cookies = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div/div[2]/div[2]/button')
cookies.click()
email = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[7]/form/div[2]/input')
email.send_keys("Ikisivri.Ersin@gmx.de")
password = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[7]/form/div[3]/input')
password.send_keys("Hallo123456")
login = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[7]/form/div[6]')
login.click()
'''if site == 'nike':
    cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/button')
    cookies.click()
    select_size = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div[1]/fieldset/div/div[12]/label')
    select_size.click()
elif site == 'sneakers':
    cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div[1]/button')
    cookies.click()
    select_size = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[12]/button')
    select_size.click()
    addToBasket = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button')
    addToBasket.click()'''
