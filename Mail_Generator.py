from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
import time
import random
import string

proxy_ip_port = '194.219.175.210:8080'	
URL = 'https://mail.tutanota.com/login'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
for i in range(1):
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', desired_capabilities=capabilities)
    driver.get(URL)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[3]/div/button/small').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[4]/div/div/div/button[1]/div').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[5]/button/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/input').click()
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]/div').click()
    time.sleep(1)
    a = True
    mail = ''
    password = ''
    while a:
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/input').clear()
        mail = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(15))
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/input').send_keys(f'{mail}')
        time.sleep(4)
        print(driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/small/div').text)
        if driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/small/div').text == 'Email address is available.':
            a = False
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(15))
            driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/input[4]').send_keys(f'{password}')
            time.sleep(5)
            driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div/div/div/input').send_keys(f'{password}')
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/input').click()
    with open('/home/ersin-linux/Documents/Data.txt', 'a') as f:
        f.write(mail + ' <=> ' + password + '\n')
        f.close()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[5]/button/div').click()
    #time.sleep(5)
    #driver.close()

