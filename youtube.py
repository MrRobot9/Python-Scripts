import time
import re
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 

def get_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


 
def init_driver():
    driver = webdriver.PhantomJS()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver, query,driver2):
    driver.get("https://www.youtube.com/results?search_query="+query)
    html_list = driver.find_element_by_class_name("item-section")
    items = html_list.find_elements_by_tag_name("li")
    stack=[]
    index = 0
    for item in items:
        index+=1
        link = item.find_elements_by_xpath("//div[@class='yt-lockup-thumbnail contains-addto']/a")
        title = item.find_elements_by_xpath('//div[@class="yt-lockup-content"]/h3/a')
        try:
          print (index,"--->  ",(title[index].get_attribute("title").encode("utf-8")))
          stack.append(link[index].get_attribute("href"))
          #stack.append(re.sub('https://www.youtube.com','',link[index].get_attribute("href")))
        except IndexError:
           break
        
    
    number= int(input('which link you would like to download : '))    
    print(stack[number-1])    
    driver2.get("http://www.ssyoutube.com")
    try:
        box = driver2.wait.until(EC.presence_of_element_located(
            (By.NAME, "sf_url")))
        button = driver2.wait.until(EC.element_to_be_clickable(
            (By.NAME, "sf_submit")))
        box.send_keys(stack[number-1])
        button.click()
        download = driver2.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "def-btn-box")))
        download.click()
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    driver2=get_driver()  
    name=input('Search : ')
    lookup(driver, name,driver2)
   