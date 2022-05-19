from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



PATH = "/home/rooter/snap/geckodriver"
driver = webdriver.Firefox(service=Service(PATH))

a = False
while a:
    url = input("enter your shoes url from nike shop:\n")
    if  not "https://www.nike.com/" in url:
        print("enter a valid url")
    else:
        a= True

driver.get(url)