'''
Created on Aug 3, 2025

@author: fatimaatif

'''
from selenium import webdriver
import pyautogui
import time

import random


driver = webdriver.Chrome()
driver.get("https://demo-v3.app.senegalsoftware.com/Talents/list")
driver.maximize_window()
time.sleep(5)
driver.find_element("id", "email_address").send_keys("fatima.atif@dynamologic.com")
driver.find_element("id", "password").send_keys("Password123!")
driver.find_element("xpath","/html/body/div[2]/div[1]/div/form/button").click()
time.sleep(30)

for i in range(25):
  

    randomNumber = random.randint(0,1)

    
    print (randomNumber)

    
    if randomNumber == 0:

        #CreateAnAgent

        driver.get("https://demo-v3.app.senegalsoftware.com/Talents/create?id=-1&search_id=&parent_module=&parent_id=")

        driver.find_element("id","Users_UID_first_name_create").send_keys("A")

        pyautogui.typewrite(['u', 't', 'o', 'a', 'g', 'e', 'n', 't'], interval = 1)

        pyautogui.press("tab")

        driver.find_element("id","Users_UID_last_name_create").send_keys("L")

        pyautogui.typewrite(['a',
                                 's', 't', 'n', 'a', 'm', 'e'], interval = 1)

        pyautogui.press("tab")

        pyautogui.typewrite(['0', '8', '0', '9', '1', '9', '9', '0'], interval = 2)

        driver.find_element("id","Users_UID_email_address_create").send_keys("A")

        pyautogui.typewrite(['u', 't', 'o', '_', 'a', 'g', 'e', 'n', 't', '_' , '0', '@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm'], interval = 1.5)

        pyautogui.press("tab")

        pyautogui.press(["down", "down", "down"]) 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["down", "down", "down", "down", "down", "down", "down", "down", "down"]) 

        pyautogui.press("enter")  

        pyautogui.press("tab")

        pyautogui.press(["up", "up", "up", "up", "down", "up", "down", "up"]) 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["up", "up", "up", "up", "down", "up", "down", "up"]) 

        pyautogui.typewrite('3311422111', interval = 0.5)

        pyautogui.press("tab")

        pyautogui.typewrite('3300000000', interval = 1.25)

        pyautogui.press("tab")

        pyautogui.typewrite('476 Fifth Avenue, New York, NY 10018', interval = 1)

        pyautogui.press("tab")

        pyautogui.typewrite('New York, Street 12481 Next to MCD', interval = 2)

        pyautogui.press("tab")

        pyautogui.typewrite('California', interval = 1)

        pyautogui.press("enter")

        time.sleep(1)

        pyautogui.press("tab")

        pyautogui.press("453021", interval = 2)

        pyautogui.press("tab")

        pyautogui.press("tab")

        pyautogui.typewrite('California', interval = 2)

        pyautogui.press("enter")

        pyautogui.typewrite('New', interval = 1)

        pyautogui.press("enter")

        pyautogui.typewrite('Houston', interval = 1)

        pyautogui.press("enter")

        pyautogui.typewrite('Chicago', interval = 1)

        pyautogui.press("enter")

        pyautogui.typewrite('California', interval = 1)

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.typewrite('50', interval = 2)

        pyautogui.press("tab")

        pyautogui.press(["down", "down", "up", "up"]) 

        pyautogui.press("enter") 

        pyautogui.press("tab")

        pyautogui.press(["down", "down", "up",]) 

        pyautogui.press("enter")  

        pyautogui.press("tab")

        pyautogui.press(["4", "2", "9"], interval = 1)

        pyautogui.press("tab")

        pyautogui.press(["down", "down", "up","up"]) 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press("down") 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["5", "1", "4","9"], interval = 1.5) 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["f","a","t","i","m","a"], interval = 2) 

        pyautogui.press("enter")

        pyautogui.press(["I","C","L","_","A","G","E","N","C","Y"], interval = 2)

        pyautogui.press("enter")

        pyautogui.press(["t","e","s","t","i","n","g"], interval = 1) 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["P", "a", "s","s","w","o","r","d","1","2","3","!"], interval = 1) 

        pyautogui.press("enter")

        time.sleep(10)

        

    if randomNumber == 1:

        #createShift

        driver.get("https://demo-v3.app.senegalsoftware.com/Shifts/create?id=-1&search_id=&parent_module=&parent_id=")

        driver.find_element("id","Shifts_UID_name_create").send_keys("A")

        pyautogui.typewrite('uto_Shift_Automation', interval = 1)

        pyautogui.press("tab")

        pyautogui.typewrite('position', interval = 1.25)

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.typewrite('job', interval = 2)

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["down", "down", "down"]) 

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.typewrite('tag', interval = 1)

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["down"])

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["up","up"])

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.press(["down"])

        pyautogui.press("enter")

        pyautogui.press("tab")

        pyautogui.typewrite('con', interval = 2)

        pyautogui.press("enter")

        time.sleep(2)

        pyautogui.press("tab")

        pyautogui.typewrite('OnSite Contact Auto Name', interval = 2)

        pyautogui.press("tab")

        pyautogui.typewrite('autocontact@gmail.com', interval = 1)

        pyautogui.press("tab")

        pyautogui.typewrite('3311111111', interval = 2.5)

        pyautogui.press("enter")

        time.sleep(10)
