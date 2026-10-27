# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:25:57 2019

@author: Susil Kumaar
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
# global string1

def messages(string1,string2):
    print("entering root function")
    df = pd.read_csv(string1)
    #df
    driver = webdriver.Chrome(string2)
    #print("entering root function1")
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 400000) 
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ZP8RM"]')))
    def sendMessage(name,message):
        #print("Starting Function For ", name, message)
        driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(name)
        #driver.find_element_by_xpath("//div[@class='ZP8RM _19OGD']").send_keys("Gandhari")
        time.sleep(2)
        try:
            #driver.find_element_by_xpath("//span[@title="+strName+"]").click()
            driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[*]/div/div/div[2]/div[1]/div[1]/span/span").click()
        except:
            #print(">>>>>>>>>>not done for ", name, message)
            driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/button').click()
            return 
        driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']").send_keys(message)
        time.sleep(2)
        #driver.find_element_by_xpath("//span[@data-icon='clip']").click()

        driver.find_element_by_xpath("//span[@data-icon='send']").click()
        print(">>>>>>>>>>>>Done Function For ", name, message)
        time.sleep(2)
    # Function call :
    #df['username'] = (df['username']/10000000000)*10000000000
    #df['username'].fillna(0,inplace = True)
    df.username = df.username.astype('int64')
    for i in range(len(df)):
        print(i)
        #if(i>4):
        sendMessage('{}'.format(df['username'][i]),str(df['message'][i]))#no need for char34{}
    
def message(string1,string2):
    df = pd.read_csv(string1)
    print(string1)
    #print(df)
    driver = webdriver.Chrome(string2)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 400000) 
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ZP8RM"]')))
    def sendMessage(Name,strName):
        #print('>>>>>>>>>>>> starting for number',Name)
        driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(Name)
        #time.sleep(3)
                #driver.find_element_by_xpath("//span[@title="+strName+"]").click()
        try:
            time.sleep(2)
            #driver.find_element_by_xpath("//span[@title="+strName+"]").click()
            driver.find_element_by_xpath("//span[@title="+strName+"]").click()
            #driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[*]/div/div/div[2]/div[1]/div[1]/span/span").click()
            #time.sleep(3)
        except:
            time.sleep(2)
            print(">>>>>>>>>>not done for ", Name)
            driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/button').click()
            return 
        time.sleep(1)
        #driver.find_element_by_xpath("//span[@title="+strName+"]").click()
        driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']").click()
        #time.sleep(1)
        actions = ActionChains(driver)
        target=driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']")
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').perform()
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span").click()
        time.sleep(1)
        #time.sleep(3)
        print(">>>>>>>>>>>>Done Function For ",Name)
        time.sleep(1)
    for i in range(len(df)):
        print(i)
        sendMessage(df['Name'][i],df['strName'][i])
    
def next1():
    global e,e1
    top = Toplevel()
    top.title("enter file path and chromedriver path")
    top.geometry("200x250")
    text1 = Label(top,text='enter file path')
    text1.place(x=5,y=25)
    e = Entry(top)
    text2 = Label(top,text='enter chromedriver path')
    text2.place(x=5,y=70)
    e1 = Entry(top)
    e.pack()
    e1.pack()
    e.place(x=5,y=50)
    e1.place(x=5,y=95)
    string1 = e.get()
    string2=e1.get()
    #print(string1)
    button1 = Button(top,text='next',command = message3)
    button1.place(x=5,y=120)

def message1():
    global e, e1
    string1 = e.get()
    string2 = e1.get()
    top = Toplevel()
    button2 = Button(top,text = 'are you sure',command = lambda : message(string1,string2))
    button2.place(x=50,y=100)

def message3():
    global e, e1
    string1 = e.get()
    string2 = e1.get()
    top = Toplevel()
    button2 = Button(top,text = 'are you sure',command = lambda : messages(string1,string2))
    button2.place(x=50,y=100)
    
def phonenumber():
    global e,e1
    top = Toplevel()
    top.title("sending message using phone number")
    top.geometry("200x250")
    text1 = Label(top,text='enter file path')
    text1.place(x=5,y=25)
    e = Entry(top)
    text2 = Label(top,text='enter chromedriver path')
    text2.place(x=5,y=70)
    e1 = Entry(top)
    e.pack()
    e1.pack()
    e.place(x=5,y=50)
    e1.place(x=5,y=95)
    string1 = e.get()
    string2=e1.get()
    #print(string1)
    button1 = Button(top,text='next',command = message1)
    button1.place(x=5,y=120)

def showCopyOptions():
    global e,e1
    top = Toplevel()
    top.title("Enter file path and chromedriver path")
    top.geometry("200x250")
    filePathLable = Label(top,text='Enter file path')
    filePathLable.place(x=5,y=25)
    e = Entry(top)
    chromePathLable = Label(top,text='Enter chromedriver path')
    chromePathLable.place(x=5,y=70)
    e1 = Entry(top)
    e.pack()
    e1.pack()
    e.place(x=5,y=50)
    e1.place(x=5,y=95)
    string1 = e.get()
    string2 = e1.get()
    button1 = Button(top,text='next',command = message3)
    button1.place(x=5,y=120)

root = Tk()
T = tk.Text(root, height=10, width=30)
T.pack()

button = Button(root,text='using name',command = showCopyOptions)
button.place(x=5,y=50)
button1 = Button(root,text='phone number', command = showCopyOptions)
button1.place(x=5,y=15)

tk.mainloop()
