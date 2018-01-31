from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
import g4_utils_v40 as utilsg4

fileTarget = "/Users/sofian/Documents/Projet_att/"
    
links=[]
for i in range(1, 400):
    url_crawl = 'http://www.lemonde.fr/recherche/?keywords=attentat&page_num=' + str(i) + "&operator=and&exclude_keywords=&qt=recherche_texte_titre&author=&period=since_1944&start_day=01&start_month=01&start_year=1944&end_day=31&end_month=01&end_year=2018&sort=desc"
    req = requests.get(url_crawl)
    data = req.text
    soup = BeautifulSoup(data, "lxml")
    for h3 in soup.find_all('h3'):
        for a in h3.find_all('a'):
            url = 'http://www.lemonde.fr' + a.get("href")
            links.append(url)

list_articles = []
for article_link in links:
    req = requests.get(article_link) 
    data = req.text 
    soup = BeautifulSoup(data, "lxml") 

    title = soup.find('title').string
    title = title.lower()

    newspaper = "Le Monde"
         
    # Article theme 
    theme = ""
    for li in soup.find_all('li'):
        for val in re.finditer('ariane', str(li.get("class"))):
            theme = li.a.get_text()
        
    # Author of the article 
    if(soup.find("span", class_="auteur")):
        if(soup.find("span", class_="auteur").a):
            author = soup.find("span", class_="auteur").find("a").get_text()
        else:
            author = soup.find("span", class_="auteur").get_text()
        author = re.sub(r"\s\s+", " ", author)
        author = re.sub(r"^ ", "", author)
    else:
        author = ""

    # publication date
    date_p = ""
    for tim in soup.find_all('time'):
        if tim.get("itemprop") == 'datePublished':
            date_t = tim.get('datetime')
            date_p = date_t[0:10]
            date_p = datetime.strptime(date_p, "%Y-%m-%d").strftime("%d/%m/%Y")

    # Article content
    content = ""
    for div in soup.find_all('div'):
        if div.get("id") == 'articleBody':
            for p in div.find_all('p'):
                if p.get("class") == ['lire']:
                    p.string = ""
            content += div.get_text() + " "
    
    data = [{"title": title,
            "newspaper": newspaper,
            "author": author,
            "date_publi": date_p,
            "theme": theme,
            "content": content
            }]
        
    utilsg4.create_json(fileTarget, data, "le_monde", "lmde")
                
