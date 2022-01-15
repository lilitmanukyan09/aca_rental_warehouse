#importing libraries
import pandas as pd
import numpy as np
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")

directory = 'Project'
parent_dir = 'C:/Users/Lilit/Lilit/Study/Data_Engineering/'
path = os.path.join(parent_dir, directory)
os.chdir(path)
os.getcwd()


#urls to scrape
urls = ['https://www.rentfaster.ca/bc/victoria/',
        'https://www.rentfaster.ca/bc/vancouver/', 
        'https://www.rentfaster.ca/bc/kelowna/', 
        'https://www.rentfaster.ca/ab/calgary/', 
        'https://www.rentfaster.ca/ab/edmonton/', 
        'https://www.rentfaster.ca/ab/red-deer/', 
        'https://www.rentfaster.ca/ab/fort-mcmurray/', 
        'https://www.rentfaster.ca/sk/saskatoon/', 
        'https://www.rentfaster.ca/sk/regina/', 
        'https://www.rentfaster.ca/mb/winnipeg/', 
        'https://www.rentfaster.ca/on/mississauga/', 
        'https://www.rentfaster.ca/on/toronto/', 
        'https://www.rentfaster.ca/on/ottawa/', 
        'https://www.rentfaster.ca/qc/montreal/', 
        'https://www.rentfaster.ca/ns/halifax/', 
        'https://www.rentfaster.ca/pe/charlottetown/', 
        'https://www.rentfaster.ca/nl/st-john-s/']


#Scraping the dataset for properties table
browser = webdriver.Chrome()
browser.maximize_window()

data = pd.DataFrame()

for url in urls:
    page = browser.get(url)
    time.sleep(6)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/aside/ul/li/div/div/div/div[1]/div/a[1]').click()
    time.sleep(3)
    browser.execute_script("scroll(0, 0);")

    for i in range(1, 51):
        try:
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/article/div[3]/div/div[2]/div/div[2]/div[2]/div[" + str(i) + "]/div/div/div[2]/a[3]").click()
            time.sleep(5)
            try:
                property_id = browser.find_element_by_class_name('listing-summary-value').text
            except:
                property_id = ""
            try:    
                region = browser.find_element_by_class_name('city').text.split(', ')[-1]
            except:
                region = ""
            try:
                city = url.split("/")[-2].title()
            except: 
                city = ""
            try: 
                location = browser.find_element_by_class_name('street-addr').text
            except:
                location = ""
            try:
                property_type = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[1]/span[2]').text
            except:
                property_type = ""
            try:    
                furnishing = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[7]').text
            except:
                furnishing = ""
            try:
                lease_term = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[8]').text
            except:
                lease_term = ""
            try:
                availability = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[9]').text
            except:
                availability = ""
            try:
                rent = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/span[2]/span[2]').text
            except:
                rent = ""    
            try:
                deposit = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]').text
            except:
                deposit = ""
            try:
                beds = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]').text
            except:
                beds = ""
            try:
                baths = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]').text
            except:
                baths = ""
            try:
                size = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[6]').text
            except:
                size = ""    
            try:
                pets = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[5]/ul/li[2]/span[2]/span').text
            except:
                pets = ""
            try:
                smoking = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[5]/ul/li[3]/span[2]').text
            except:
                smoking = ""
            try:
                parking = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[5]/ul/li[4]/span[2]/span[1]/span').text
            except:
                parking = ""

            df = pd.DataFrame({
                'property_id' : property_id,
                'region' : region,
                'city': city,
                'location': location, 
                'property_type':property_type, 
                'furnishing_state': furnishing, 
                'lease_term' : lease_term,
                'availability' : availability,                                                
                'rent': rent,
                'deposit': deposit,
                'beds': beds,
                'baths' : baths,
                'size': size,
                'pets' : pets,
                'smoking' : smoking, 
                'parking' : parking}, index = [i])
            print(df)
            data = data.append(df)
            webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        
        except:
            continue
browser.quit()

data.to_csv('properties.csv')
