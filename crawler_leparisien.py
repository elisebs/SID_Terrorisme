from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
import g4_utils_v40 as utilsg4

fileTarget = "/Users/sofian/Documents/Projet_att/"

# Récupération article de la première page
url_rss_lp = "http://www.leparisien.fr/actus/attentat"
req = requests.get(url_rss_lp)
data = req.text
soup = BeautifulSoup(data, "lxml")

liste_url = []
# Retrieving all urls of new RSS feeds of different categories
for a in soup.find_all('a'):
    for valeur in re.finditer('article__hover-href', str(a.get("class"))):
        liste_url.append(a.get("href"))

# Récupération article attentat sur les pages 2 à 35
for i in range(2, 35):
    url_crawl = 'http://www.leparisien.fr/actus/attentat/page-' + str(i) 
    req2 = requests.get(url_crawl)
    data2 = req2.text
    soup2 = BeautifulSoup(data2, "lxml")
    for a2 in soup2.find_all('a'):
        for val in re.finditer('article__hover-href', str(a2.get("class"))):
            liste_url.append(a2.get("href"))
        
for url in liste_url:
    req = requests.get(url)
    data = req.text
    soup_article = BeautifulSoup(data, "lxml")

# Retrieving of title and newspaper
    balise_title = soup_article.title.string
    sep = balise_title.split(" - ")
    title = sep[0]

        # author
    for meta in soup_article.find_all('meta'):
        if meta.get("itemprop") == 'creator':
            author = meta.get("content")

        # Date de publication
    for meta in soup_article.find_all('meta'):
        if meta.get("itemprop") == 'datePublished':
            raw_date = meta.get("content")
            date_p = raw_date[0:10]
            date_p = datetime.strptime(date_p, "%Y-%m-%d").strftime("%d/%m/%Y")

        # theme
    for meta in soup_article.find_all('meta'):
        if meta.get("itemprop") == 'articleSection':
            categorie = meta.get("content")

# content
    content = ""

    for h2 in soup_article.find_all('h2'):
        if h2.get("class") == ['article-full__header']:
            content = h2.get_text() + " "
    for div in soup_article.find_all('div'):
        if div.get("class") == ['article-full__body-content']:
            for b in div.find_all('b'):
                b.string = ""
            for a in div.find_all('a'):
                a.string = ""
            content += div.get_text() + " "
        
    
    data = [{"title": title,
            "newspaper": "leparisien",
            "author": author,
            "date_publi": date_p,
            "theme": categorie,
            "content": content
            }]
    # Mis sous json les articles
    utilsg4.create_json(fileTarget, data, "leparisien", "lp")
