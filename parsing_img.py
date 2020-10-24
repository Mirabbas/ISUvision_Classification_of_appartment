from selenium import webdriver
import re
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import json
import time
import vk_api

class Yandex(object):
  def __init__(self):
    self.vk = vk_api.VkApi(
     token="dcbf190bcf771b167752a82ff5669ff1cc8f0503c2")
    self.chrome_options = Options()
    self.chrome_options.add_argument("headless")
    self.chrome_options.add_argument('window-size=1920x935')
    self.driver = webdriver.Chrome(executable_path="C:/Users/pitonhik/Downloads/chromedriver.exe")
    self.tabs = self.driver.window_handles
  def get_url(self,path):
    if path[:4] == 'http':
        return path
    else:
        return vk_api.VkUpload(self.vk).photo_messages(photos=path)[0]['sizes'][4]['url']




  def make_url_yandex(self,url):
    s = url.replace('/','%2F')
    url = s.replace(':','%3A')
    print(url)
    rez = 'https://yandex.ru/images/search?url=' + url + '&rpt=imageview&from='
    return rez
  def get_info_yangex(self,url):
    url = self.get_url(url)
    
    u = self.make_url_yandex(url)
    print(u)
    self.driver.get(u)
               
    time.sleep(1)
    a = self.driver.find_elements_by_tag_name('a')
    text = []
    for i  in range(len(a)):
     try:
      at = a[i].get_attribute("tone")
      if at=='gray':
         text.append(a[i].text)
     except:
        True
    text = text[::-1]
    text = text[:4]
    try:
     g = self.driver.find_elements_by_class_name('MarketProduct-Inner')
    
     time.sleep(1)
    
     s1 = g[0].find_elements_by_tag_name('span')
     s2=g[1].find_elements_by_tag_name('span')
    
     price = int(s1[1].text) + int(s2[1].text)
     price = int(price/2)
    except:
        price = False
    return text , price
  def close(self):
      self.driver.close()
y = Yandex()
name ,price = y.get_info_yangex("39.jpg")
