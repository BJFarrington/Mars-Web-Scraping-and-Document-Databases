#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news'
browser.visit(url)


# In[4]:


html = browser.html
soup = bs(html, 'html.parser')


# In[6]:


#print(soup.prettify())


# In[7]:


title = soup.find('div', class_="content_title")

paragraph = soup.find('div', class_="article_teaser_body")

print(title.text)
print(paragraph.text)


# In[40]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[41]:


jpl_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)


# In[42]:


html = browser.html
soup = bs(html, 'html.parser')


# In[43]:


image = soup.find("img", title= "InSight Images a Sunset on Mars")["src"]
featured_image_url = "https://jpl.nasa.gov"+image


# In[44]:


print(featured_image_url)


# In[25]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[26]:


twitter_url= 'https://twitter.com/marswxreport?lang=en'
browser.visit(twitter_url)


# In[27]:


html = browser.html
soup = bs(html, 'html.parser')


# In[29]:


recent_tweet = soup.find('div', class_="js-tweet-text-container")


# In[53]:


mars_weather = str(recent_tweet.text.strip())


# In[54]:


if mars_weather.endswith('hPapic.twitter.com/wEcSHS2b3u'):
    mars_weather = mars_weather[:-30]


# In[55]:


mars_weather


# In[ ]:





# In[56]:


mars_super_facts_url= 'https://space-facts.com/mars/'


# In[57]:


tables = pd.read_html(mars_super_facts_url)
tables


# In[58]:


df = tables[0]


# In[59]:


html_table = df.to_html()
clean_html_table = html_table.replace('\n', '')


# In[60]:


clean_html_table


# In[89]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[90]:


mars_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(mars_url)


# In[91]:


html = browser.html
soup = bs(html, 'html.parser')


# In[92]:


hemisphere_image_urls =[]
for i in range (4):
    
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = bs(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    hemisphere_image_dict={"title":img_title,"img_url":img_url}
    hemisphere_image_urls .append(hemisphere_image_dict)
    browser.back()


# In[94]:


hemisphere_image_urls

