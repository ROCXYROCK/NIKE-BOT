'''from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


URL = 'https://www.nike.com/de/t/blazer-low-jumbo-herrenschuh-HK5Kqs/DV3506-100'
Proxy = '212.62.95.45:1080'

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % Proxy)

chrome = webdriver.Chrome(chrome_options = chrome_options)
chrome.get(URL)
cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/button')
cookies.click()

select_size = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[2]/form/div[1]/fieldset/div/div[12]/label')
select_size.click()'''

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_ip_port = '156.17.193.1:80'
URL = 'https://mail.tutanota.com/login?noAutoLogin=true'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome('/usr/local/bin/chromedriver', desired_capabilities=capabilities)

driver.get(URL)


