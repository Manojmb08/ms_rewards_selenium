from selenium import webdriver
import time, random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.EdgeOptions()
# for mobile version
opt.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1")
opt.add_experimental_option("detach", True)
driver = webdriver.Edge(options=opt)
driver.get("https://www.bing.com")
time.sleep(20)

with open('songs.txt') as file:
    k = file.readlines()
    songs = [i[:-1] for i in k]

for i in range(30):
    print(i)
    sear = driver.find_element(By.ID, "sb_form_q")
    time.sleep(3)
    sear.clear()
    time.sleep(3)
    sear.send_keys(random.choice(k) + Keys.ENTER)
