#!/usr/bin/env python
# coding: utf-8

# In[38]:


get_ipython().system('pip install selenium')


# In[60]:


import pandas as pd
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[61]:


driver=webdriver.Chrome(r"https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_mac64.unzip")


# In[72]:


driver.get("https://www.naukri.com/")


# In[ ]:


# QUESTION 1
#Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
This task will be done in following steps:
1. First get the webpage https://www.naukri.com/
2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
location” field.
3. Then click the search button.
4. Then scrape the data for the first 10 jobs results you get.
5. Finally create a dataframe of the scraped data.


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,("suggestor-input "))
designation.send_keys('Data analyst')


# In[ ]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('bangalore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in tag[0:10]:
    title=i.text
    job_title.append(title)
    
location_tag= driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    j=i.text
    job_location.append(j)
company_tag= driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    j=i.text
    company_name.append(j)
    
exp_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')   
for i in exp_tag[0:10]:
    j=i.text
    experience_required.append(j)
    
    

                                  


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df=pd.DataFrame({"JOB TITLE":job_title,
                 "JOB LOCATION":job_location,
                 "COMPANY":company_name,
                 "EXPERIENCE":experience_required})
df


# In[ ]:


# QUESTION NO 2
#  Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
This task will be done in following steps:
1. First get the webpage https://www.naukri.com/
2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
location” field.
3. Then click the search button.
4. Then scrape the data for the first 10 jobs results you get.
5. Finally create a dataframe of the scraped data.


# In[73]:


designation=driver.find_element(By.CLASS_NAME,("suggestor-input "))
designation.send_keys('Data Scientist')


# In[ ]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('bangalore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in tag[0:10]:
    title=i.text
    job_title.append(title)
    
location_tag= driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    j=i.text
    job_location.append(j)
company_tag= driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    j=i.text
    company_name.append(j)
    
exp_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')   
for i in exp_tag[0:10]:
    j=i.text
    experience_required.append(j)
    


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df=pd.DataFrame({"JOB TITLE":job_title,
                 "JOB LOCATION":job_location,
                 "COMPANY":company_name,
                 })
df


# In[ ]:


#question--3
You have to use the location and salary filter.
You have to scrape data for “Data Scientist” designation for first 10 job results.
You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
The task will be done as shown in the below steps:
1. first get thewebpage https://www.naukri.com/
2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
3. Then click the searchbutton.
4. Then apply the location filter and salary filter by checking the respective boxes
5. Then scrape the data for the first 10 jobs results youget.
6. Finally create a dataframe of the scraped data.


# In[74]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('DELHI')


# In[75]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[79]:


All_filter = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft filterLabel"]')

        
         
        


# In[80]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[81]:


tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in tag[0:10]:
    title=i.text
    job_title.append(title)
    
location_tag= driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    j=i.text
    job_location.append(j)
company_tag= driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    j=i.text
    company_name.append(j)
    
exp_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')   
for i in exp_tag[0:10]:
    j=i.text
    experience_required.append(j)
    


# In[82]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[83]:


df=pd.DataFrame({"JOB TITLE":job_title,
                 "JOB LOCATION":job_location,
                 "COMPANY":company_name,
                 })
df


# In[ ]:


#Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes: 1. Brand
#2. Product Description
#3. Price
#The attributes which you have to scrape is ticked marked in the below image.
#To scrape the data you have to go through following steps:
#1. Go to Flipkart webpage by url : https://www.flipkart.com/
#2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and
#click the search icon
#3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
#required data a


# In[62]:


driver.get("https://www.flipkart.com/")


# In[63]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
location.send_keys('sunglasses')


# In[65]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[66]:


brand=[]
product_description=[]
price=[]


# In[67]:


brand_tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tag[0:40]:
    title=i.text
    brand.append(title)
    
description_tag= driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in description_tag[0:40]:
    j=i.text
    product_description.append(j)
    
price_tag= driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tag[0:40]:
    j=i.text
    price.append(j)
    


# In[68]:


items=[]
start=1
end=3
for i in range(start,end):
    title=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for j in title:
        brand.append(j.text)
                              
    title_1=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for k in title_1:
         product_description.append(k.text)
                              
    title_2=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for l in title_2:
         price.append(l.text)
                              
next_element=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
next_element.click()


# In[69]:


print(len(brand),len(product_description),len(price))


# In[ ]:




