import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def search(n):
    for i in range(n):
        print(i)
        sear = driver.find_element(By.ID, "sb_form_q")
        time.sleep(3)
        sear.clear()
        time.sleep(3)
        sear.send_keys(random.choice(k) + Keys.ENTER)


# mob()
if __name__ == "__main__":
    mob = True  # for mobile set mob = True
    opt = webdriver.EdgeOptions()
    # opt.add_experimental_option("detach", True) #to keep window open after search
    if mob:
        opt.add_argument(
            "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/117.0.0.0")
    driver = webdriver.Edge(options=opt)
    driver.get("https://www.bing.com")
    time.sleep(15)  # time required to login
    with open('songs.txt') as file:
        k = file.readlines()
        songs = [i[:-1] for i in k]
    if mob:
        search(30)
    else:
        search(45)
