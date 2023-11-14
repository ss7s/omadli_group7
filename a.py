from selenium import webdriver
import time
#object of ChromeOptions class
c = webdriver.EdgeOptions()
#incognito parameter passed
c.add_argument("--incognito")
#set chromodriver.exe path
driver = webdriver.Edge(executable_path="C:\msedge.exe",options=c)
driver.implicitly_wait(0.5)
#launch URL
for _ in range(100):
    driver.get('https://www.instagram.com/reel/CwOVL86JUEn/?igshid=MzRlODBiNWFlZA==')
    time.sleep(190)
