# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:25:57 2019

@author: Selva Logesh R
"""

import pandas as pd
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from tkinter import *
import tkinter as tk

def excuteAction(dataSource,filePath,chromePath):
    print(dataSource,filePath,chromePath)
    df = pd.read_csv(filePath)
    driver = webdriver.Chrome(chromePath)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 400000)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ZP8RM"]')))
    def sendMessage(name,message):
        print('>>>>>>>>>>>> starting for number ' + name)
        try:
            if(name == 'nan' or message == 'nan'):
                print(">>>>>>>>>>empty cell skipping")
                driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
                return 
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys("")
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(name)
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[*]/div/div/div[2]/div[1]/div[1]/span/span").click()
            #stop = input()
        except:
            time.sleep(3)
            print(">>>>>>>>>>not done for ", name)
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
            return 
        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']").click()
        if(dataSource == 'paste'):
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').perform()
        else:
            driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']").send_keys(message)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()
        print(">>>>>>>>>>>>Done Function For ",name)
        time.sleep(1)
    for i in range(len(df)):
        name = str(df['username'][i])
        if('.' in name):
            name = name[0:name.rfind('.')]
        msg = str(df['message'][i]).replace('\n', Keys.SHIFT + '\n' + Keys.SHIFT)
        #print(str(i)+". Name: "+df['username'][i]+" -> "+msg)
        sendMessage(name,msg)


def areYouSure(dataSource):
    filePath = filePathInput.get()
    chromePath = chromePathInput.get()
    top = Toplevel()
    areYouSureButton = Button(top,text = 'Click to execute.',command = lambda : excuteAction(dataSource,filePath,chromePath))
    areYouSureButton.place(x=50,y=100)

def enterDetails(dataSource):
    global filePathInput,chromePathInput
    top = Toplevel()
    top.title("Choose data source")
    top.geometry("200x250")
    filePathObject = Label(top,text='Enter file path')
    filePathObject.place(x=5,y=25)
    filePathInput = Entry(top)
    chromePathObject = Label(top,text='Enter Chromedriver path')
    chromePathObject.place(x=5,y=70)
    chromePathInput = Entry(top)
    filePathInput.pack()
    chromePathInput.pack()
    filePathInput.place(x=5,y=50)
    chromePathInput.place(x=5,y=95)
    nextButton = Button(top,text='next',command = lambda : areYouSure(dataSource))
    nextButton.place(x=5,y=120)

root = Tk()
T = tk.Text(root, height=10, width=30)
T.pack()
userName = Button(root,text='Excel',command = lambda : enterDetails("excel"))
userName.place(x=5,y=50)
phNumber = Button(root,text='Copy/Paste',command = lambda : enterDetails("paste"))
phNumber.place(x=5,y=15)

tk.mainloop()
