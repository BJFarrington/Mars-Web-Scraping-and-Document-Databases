#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


# In[7]:

def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


    url = 'https://mars.nasa.gov/news'
    browser.visit(url)


# In[9]:


    html = browser.html
    soup = bs(html, 'html.parser')


# In[22]:


#print(soup.prettify())


# In[10]:


    title = soup.find('div', class_="content_title").text

    paragraph = soup.find('div', class_="article_teaser_body").text



# In[11]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


    jpl_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)


# In[13]:


    html = browser.html
    soup = bs(html, 'html.parser')


# In[15]:


    featured_img_base = "https://www.jpl.nasa.gov"
    featured_img_url_raw = soup.find("div", class_="carousel_items").find("article")["style"]
    featured_img_url = featured_img_url_raw.split("'")[1]
    featured_img_url = featured_img_base + featured_img_url
    featured_img_url


# In[30]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[31]:


    twitter_url= 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)


# In[32]:


    html = browser.html
    soup = bs(html, 'html.parser')


# In[33]:


    recent_tweet = soup.find('div', class_="js-tweet-text-container")


# In[34]:


    mars_weather = str(recent_tweet.text.strip())


# In[35]:


    if mars_weather.endswith('hPapic.twitter.com/wEcSHS2b3u'):
        mars_weather = mars_weather[:-30]


# In[36]:


    


# In[ ]:





# In[37]:


    mars_super_facts_url= 'https://space-facts.com/mars/'


# In[38]:


    tables = pd.read_html(mars_super_facts_url)
    tables


# In[40]:


    df = tables[0]
    


# In[41]:


    html_table = df.to_html()
    clean_html_table = html_table.replace('\n', '')


# In[42]:


    


# In[20]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[21]:


    mars_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_url)


# In[22]:


    html = browser.html
    soup = bs(html, 'html.parser')


# In[24]:


    hemisphere_image_urls =[]
    for i in range (4):
        img_dict = {}
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = bs(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        img_dict["title"] = img_title
        img_dict["img_url"] = img_url
        print(img_dict["img_url"])
    
        hemisphere_image_urls.append(img_dict)
        browser.back()


# In[46]:





# In[47]:


    X_mars_info = {'title' : title, 'paragraph': paragraph,'featured_image' : featured_img_url,'weather' : mars_weather,'mars_facts' : clean_html_table,'mars_hemisphere' : hemisphere_image_urls}

    return X_mars_info;


# In[ ]:




