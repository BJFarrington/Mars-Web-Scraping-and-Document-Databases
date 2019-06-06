#from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser=init_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')


    news_title  = soup.find('div', class_="content_title").text

    paragraph = soup.find('div', class_="article_teaser_body").text

    



    jpl_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)


    html = browser.html
    soup = bs(html, 'html.parser')



    image = soup.find("img", alt="Curiosity")["src"]
    featured_image_url = "https://jpl.nasa.gov"+image










    twitter_url= 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)



    html = browser.html
    soup = bs(html, 'html.parser')



    recent_tweet = soup.find('div', class_="js-tweet-text-container")



    mars_weather = str(recent_tweet.text.strip())




    if mars_weather.endswith('hPapic.twitter.com/wEcSHS2b3u'):
        mars_weather = mars_weather[:-30]












    mars_super_facts_url= 'https://space-facts.com/mars/'



    tables = pd.read_html(mars_super_facts_url)
    tables




    df = tables[0]
    df




    html_table = df.to_html()
    clean_html_table = html_table.replace('\n', '')




    







    mars_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_url)




    html = browser.html
    soup = bs(html, 'html.parser')



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




    hemisphere_image_urls




    mars_info = []


    mars_info.append({'Title' : news_title, 'Paragraph': paragraph})
    mars_info.append({'Mars featured image' : featured_image_url})
    mars_info.append({'weather' : mars_weather})
    mars_info.append({'Mars Facts' : clean_html_table})
    mars_info.append({'Mars Hemisphere' : hemisphere_image_urls})

    mars_info

    browser.quit()

    return mars_info

