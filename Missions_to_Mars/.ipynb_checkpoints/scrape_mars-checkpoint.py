{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependancies\n",
    "from splinter import Browser\n",
    "import time\n",
    "from selenium import webdriver\n",
    "\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "import requests\n",
    "import pymongo\n",
    "\n",
    "#Driver\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_news():\n",
    "    # Setup splinter\n",
    "   \n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    # Set an empty dict for listings that we can save to Mongo\n",
    "    news_dict = {}\n",
    "\n",
    "    # The url we want to scrape\n",
    "    news_url = 'https://redplanetscience.com/'\n",
    "    \n",
    "    # Call visit on our browser and pass in the URL we want to scrape   \n",
    "    browser.visit(news_url)\n",
    "\n",
    "    # Let it sleep for 1 second\n",
    "    time.sleep(1)    \n",
    "\n",
    "        # Return all the HTML on our page\n",
    "    news_html = browser.html\n",
    "    \n",
    "    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'\n",
    "    news_soup = bs(news_html, \"html.parser\")\n",
    "\n",
    "    # Build our dictionary\n",
    "\n",
    "    news_dict[\"title\"] = news_soup.find(\"div\", class_ = 'content_title').get_text()\n",
    "    news_dict[\"paragraph\"] = news_soup.find(\"div\", class_ = 'article_teaser_body').get_text()\n",
    "\n",
    "    # Quit the browser\n",
    "    browser.quit()\n",
    "\n",
    "    return news_dict\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Downloading: 100%|████████████████████████████████████████████████████████| 6.68M/6.68M [00:01<00:00, 5.70MB/s]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'title': \"6 Things to Know About NASA's Ingenuity Mars Helicopter\",\n",
       " 'paragraph': 'The first helicopter attempting to fly on another planet is a marvel of engineering. Get up to speed with these key facts about its plans.'}"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scrape_news()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_img():\n",
    "    # Setup splinter\n",
    "    # browser = init_browser()\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    # The url we want to scrape\n",
    "    img_url = 'https://spaceimages-mars.com'\n",
    "    \n",
    "    # Call visit on our browser and pass in the URL we want to scrape   \n",
    "    browser.visit(img_url)\n",
    "\n",
    "    # Let it sleep for 1 second\n",
    "    time.sleep(1)    \n",
    "\n",
    "        # Return all the HTML on our page\n",
    "    img_html = browser.html\n",
    "    \n",
    "    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'\n",
    "    img_soup = bs(img_html, \"html.parser\")\n",
    "\n",
    "\n",
    "    featured_image_url = img_soup.find(\"img\", class_ = \"headerimage\").get(\"src\")\n",
    "\n",
    "    # Quit the browser\n",
    "    browser.quit()\n",
    "\n",
    "\n",
    "    return featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scrape_img()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "Description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_df = pd.read_html('https://galaxyfacts-mars.com/')[0]\n",
    "mars_df.columns=['Description', 'Mars', 'Earth']\n",
    "mars_df.set_index('Description', inplace=True)\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>Description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_hemespheres():\n",
    "    # Setup splinter\n",
    "    # browser = init_browser()\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    # The url we want to scrape\n",
    "    hemi_url = 'https://marshemispheres.com/'\n",
    "    \n",
    "    # Call visit on our browser and pass in the URL we want to scrape   \n",
    "    browser.visit(hemi_url)\n",
    "\n",
    "    # Let it sleep for 1 second\n",
    "    time.sleep(1)    \n",
    "\n",
    "    # Return all the HTML on our page\n",
    "    hemi_html = browser.html\n",
    "    \n",
    "    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'\n",
    "    hemi_soup = bs(hemi_html, \"html.parser\")\n",
    "\n",
    "    # Build our dictionary\n",
    "\n",
    "    hemisphere_image_urls = []\n",
    "\n",
    "    for page in range(4):\n",
    "        hemispheres = {}\n",
    "        title = hemi_soup.find_all(\"h3\")[page].text\n",
    "        hemispheres[\"title\"] = title\n",
    "        hemi_link = hemi_soup.find_all(\"a\", class_=\"itemLink\")[page]['href']\n",
    "\n",
    "        browser.visit(hemi_url+hemi_link)\n",
    "        time.sleep(1)\n",
    "#         browser.links.find_by_href(hemi_link).click()\n",
    "        element = browser.links.find_by_text('Sample').first\n",
    "        img_url = element['href']\n",
    "        \n",
    "        \n",
    "        hemispheres[\"img_url\"] = img_url\n",
    "        hemisphere_image_urls.append(hemispheres)\n",
    "        browser.back()\n",
    "\n",
    "    # Quit the browser\n",
    "    browser.quit()\n",
    "\n",
    "\n",
    "    return hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'}]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scrape_hemespheres()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  },
  "vscode": {
   "interpreter": {
    "hash": "1487494d1930e91d962159de15fe4593b68bb1e7b34efac8b35e8bd9484bfe5a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
