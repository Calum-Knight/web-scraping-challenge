#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependancies
from splinter import Browser
import time
from selenium import webdriver

from bs4 import BeautifulSoup as bs
import pandas as pd


#Driver
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


def scrape_news(browser):
    # Setup splinter
   
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Set an empty dict for listings that we can save to Mongo
    news_dict = {}

    # The url we want to scrape
    news_url = 'https://redplanetscience.com/'
    
    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(news_url)

    # Let it sleep for 1 second
    time.sleep(1)    

        # Return all the HTML on our page
    news_html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    news_soup = bs(news_html, "html.parser")

    # Build our dictionary

    news_dict["title"] = news_soup.find("div", class_ = 'content_title').get_text()
    news_dict["paragraph"] = news_soup.find("div", class_ = 'article_teaser_body').get_text()

    # Quit the browser
    browser.quit()

    return news_dict


# In[3]:



# In[4]:


def scrape_img(browser):
    # Setup splinter
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # The url we want to scrape
    img_url = 'https://spaceimages-mars.com/'
    
    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(img_url)

    # Let it sleep for 1 second
    time.sleep(1)    

        # Return all the HTML on our page
    img_html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    img_soup = bs(img_html, "html.parser")


    featured_image_url = img_url+img_soup.find("img", class_ = "headerimage").get("src")

    # Quit the browser
    browser.quit()


    return featured_image_url


# In[5]:




# In[6]:

def mars_facts():
    mars_df = pd.read_html('https://galaxyfacts-mars.com/')[0]
    mars_df.columns=['Description', 'Mars', 'Earth']
    mars_df.set_index('Description', inplace=True)
    mars_df


# In[7]:


    return mars_df.to_html(classes="table table-striped")


# In[47]:


def scrape_hemespheres(browser):
    # Setup splinter
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # The url we want to scrape
    hemi_url = 'https://marshemispheres.com/'
    
    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(hemi_url)

    # Let it sleep for 1 second
    time.sleep(1)    

    # Return all the HTML on our page
    hemi_html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    hemi_soup = bs(hemi_html, "html.parser")

    # Build our dictionary

    hemisphere_image_urls = []

    for page in range(4):
        hemispheres = {}
        title = hemi_soup.find_all("h3")[(page)].text
        hemispheres["title"] = title
        hemi_link = hemi_soup.find_all("a", class_="itemLink")[(page*2)]['href']

        browser.visit(hemi_url+hemi_link)
        time.sleep(1)
#         browser.links.find_by_href(hemi_link).click()
        element = browser.links.find_by_text('Sample').first
        img_url = element['href']
        
        
        hemispheres["img_url"] = img_url
        hemisphere_image_urls.append(hemispheres)
        browser.back()

    # Quit the browser
    browser.quit()


    return hemisphere_image_urls


# In[48]:

def scrape_all():
    # Setup splinter
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    data = {
        "mars_news": scrape_news(browser),
        "featured_img": scrape_img(browser),
        "mars_facts": mars_facts(),
        "hemisphere_data": scrape_hemespheres(browser)
    }

    print(data)
    return(data)

# In[ ]:




