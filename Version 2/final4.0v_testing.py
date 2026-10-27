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
import traceback
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
    def sendMessage(name,message,attachment):
        print('>>>>>>>>>>>> starting for number ' + name)
        try:
            if(name == 'nan' or message == 'nan'):
                print(">>>>>>>>>>empty cell skipping")
                driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
                return
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
            time.sleep(1)
            driver.find_element_by_xpath("//div[@class='_3FeAD uu8jX']").send_keys("")
            driver.find_element_by_xpath("//div[@class='_3FeAD uu8jX']").send_keys(name)
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[*]/div/div/div[2]/div[1]/div[1]/span/span").click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']").click()
            if(dataSource == 'paste'):
                ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').perform()
            else:
                driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']").send_keys(message)
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()
            time.sleep(3)
            if(attachment != ['nan']):
                print("Attachment: ",str(attachment))
                files = "\n".join(attachment)
                driver.find_element_by_xpath("//*[@title='Attach']").click();
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input").send_keys(files)
                time.sleep(2)
                driver.find_element_by_xpath("//div[@class='_1g8sv NOJWi']").click();
            print(">>>>>>>>>>>>Done Function For ",name)
            time.sleep(1)
            #stop = input()
        except Exception as err:
            time.sleep(3)
            traceback.print_tb(err.__traceback__)
            print(">>>>>>>>>>not done for ", name)
            driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
            return 
    for i in range(len(df)):
        name = str(df['username'][i])
        if('.' in name):
            name = name[0:name.rfind('.')]
        msg = str(df['message'][i]).replace('\n', Keys.SHIFT + '\n' + Keys.SHIFT)
        attachment = str(df['files'][i]).split(';')
        #print(str(i)+". Name: "+name+" Files: "+str(str(df['files'][i]).split(';'))+" -> "+msg)
        sendMessage(name,msg,attachment)

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

#root = Tk()
#T = tk.Text(root, height=10, width=30)
#T.pack()
#userName = Button(root,text='Excel',command = lambda : enterDetails("excel"))
#userName.place(x=5,y=50)
#phNumber = Button(root,text='Copy/Paste',command = lambda : enterDetails("paste"))
#phNumber.place(x=5,y=15)

#tk.mainloop()


filePath = "D:\Selva logesh's folder\T project\Sudarsan\Version 2\Book1.csv"
dataSource = "excel"
chromePath = "D:\Selva logesh's folder\T project\Sudarsan\Version 2\chromedriver.exe"

print(dataSource,filePath,chromePath)
df = pd.read_csv(filePath)
driver = webdriver.Chrome(chromePath)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 400000)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ZP8RM"]')))
def sendMessage(name,message,attachment):
    print('>>>>>>>>>>>> starting for number ' + name)
    #try:
    if(name == 'nan' or message == 'nan'):
        print(">>>>>>>>>>empty cell skipping")
        #driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
        return
    #driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("(//div[@class='_3u328 copyable-text selectable-text'])[1]").send_keys("")
    driver.find_element_by_xpath("(//div[@class='_3u328 copyable-text selectable-text'])[1]").send_keys(name)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[*]/div/div/div[2]/div[1]/div[1]/span/span").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").click()
    if(dataSource == 'paste'):
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').perform()
    else:
        driver.find_element_by_xpath("(//div[@class='_3u328 copyable-text selectable-text'])[2]").send_keys("")
        driver.find_element_by_xpath("(//div[@class='_3u328 copyable-text selectable-text'])[2]").send_keys(message)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()
    time.sleep(3)
    if(attachment != ['nan']):
        print("Attachment: ",str(attachment))
        files = "\n".join(attachment)
        driver.find_element_by_xpath("//*[@title='Attach']").click();
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input").send_keys(files)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='_1g8sv NOJWi']").click();
    print(">>>>>>>>>>>>Done Function For ",name)
    time.sleep(1)
    #stop = input()
#except Exception as err:
#    time.sleep(3)
#    traceback.print_tb(err.__traceback__)
#    print(">>>>>>>>>>not done for ", name)
#    driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button").click()
#    return 

for i in range(len(df)):
    name = str(df['username'][i])
    if('.' in name):
        name = name[0:name.rfind('.')]
    msg = str(df['message'][i]).replace('\n', Keys.SHIFT + '\n' + Keys.SHIFT)
    attachment = str(df['files'][i]).split(';')
    #print(str(i)+". Name: "+name+" Files: "+str(str(df['files'][i]).split(';'))+" -> "+msg)
    sendMessage(name,msg,attachment)
