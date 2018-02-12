import utils_v0 as utils
import re
from datetime import datetime
import datetime as date


file_target = "/Users/sofian/Documents/Projet_att/" + str(date.datetime.now().date()) + "/"

article_noob = []
for i in range(1, 30):
    url_rss_noob = "http://recherche.nouvelobs.com/?p=" + str(i) + "&q=attentat&c=bnJlc3VsdHMlM0QxMCUyNnN0YXJ0JTNEMjgwJTI2bG9naWMlM0RzbHJlZm9udGUtZ2xvYmFsZSUyNnElM0RhdHRlbnRhdCUyQiUyNTI4Tk9UJTJCY29ycG9yYXRlJTI1MkZ0cmVlJTI1M0FUb3AlMjUyRnR5cGUlMjUyRmRlcGVjaGVzJTJCQU5EJTJCTk9UJTJCY29ycG9yYXRlJTI1MkZ0cmVlJTI1M0FUb3AlMjUyRnR5cGUlMjUyRnJlZGlyZWN0aW9uJTI1MjklMkJBTkQlMkIlMjUyOGNvcnBvcmF0ZSUyNTJGdHJlZSUyNTNBVG9wJTI1MkZteXNvdXJjZSUyNTJGbm91dmVsb2JzLmNvbSUyQk9SJTJCY29ycG9yYXRlJTI1MkZ0cmVlJTI1M0FUb3AlMjUyRm15c291cmNlJTI1MkZsZXBsdXMlMkJPUiUyQmNvcnBvcmF0ZSUyNTJGdHJlZSUyNTNBVG9wJTI1MkZteXNvdXJjZSUyNTJGb2JzZXNzaW9uJTJCT1IlMkJjb3Jwb3JhdGUlMjUyRnRyZWUlMjUzQVRvcCUyNTJGbXlzb3VyY2UlMjUyRnRlbGVvYnMuY29tJTJCT1IlMkJjb3Jwb3JhdGUlMjUyRnRyZWUlMjUzQVRvcCUyNTJGbXlzb3VyY2UlMjUyRmJpYmxpb2JzJTI1Mjk%3D"
    soup_url = utils.recovery_flux_url_rss(url_rss_noob)
    for h2 in soup_url.find_all('h2'):
        if h2.get("class") == ['title']:
            if re.search('www.nouvelobs.com', str(h2.a.get("href"))):
                article_noob.append(h2.a.get("href"))

for i in range(1, 30):
    url_rss_noob = "http://recherche.nouvelobs.com/?p=" + str(i) + "&q=terrorisme&c=bnJlc3VsdHMlM0QxMCUyNnN0YXJ0JTNEMjkwJTI2bG9naWMlM0RzbHJlZm9udGUtZ2xvYmFsZSUyNnElM0R0ZXJyb3Jpc21lJTJCJTI1MjhOT1QlMkJjb3Jwb3JhdGUlMjUyRnRyZWUlMjUzQVRvcCUyNTJGdHlwZSUyNTJGZGVwZWNoZXMlMkJBTkQlMkJOT1QlMkJjb3Jwb3JhdGUlMjUyRnRyZWUlMjUzQVRvcCUyNTJGdHlwZSUyNTJGcmVkaXJlY3Rpb24lMjUyOSUyQkFORCUyQiUyNTI4Y29ycG9yYXRlJTI1MkZ0cmVlJTI1M0FUb3AlMjUyRm15c291cmNlJTI1MkZub3V2ZWxvYnMuY29tJTJCT1IlMkJjb3Jwb3JhdGUlMjUyRnRyZWUlMjUzQVRvcCUyNTJGbXlzb3VyY2UlMjUyRmxlcGx1cyUyQk9SJTJCY29ycG9yYXRlJTI1MkZ0cmVlJTI1M0FUb3AlMjUyRm15c291cmNlJTI1MkZvYnNlc3Npb24lMkJPUiUyQmNvcnBvcmF0ZSUyNTJGdHJlZSUyNTNBVG9wJTI1MkZteXNvdXJjZSUyNTJGdGVsZW9icy5jb20lMkJPUiUyQmNvcnBvcmF0ZSUyNTJGdHJlZSUyNTNBVG9wJTI1MkZteXNvdXJjZSUyNTJGYmlibGlvYnMlMjUyOQ%3D%3D"
    soup_url = utils.recovery_flux_url_rss(url_rss_noob)
    for h2 in soup_url.find_all('h2'):
        if h2.get("class") == ['title']:
            if re.search('www.nouvelobs.com', str(h2.a.get("href"))):
                article_noob.append(h2.a.get("href"))

# analyse de chaque article
titre =[]
for url_article in article_noob:
 
    try:    
        soup_article = utils.recovery_flux_url_rss(url_article)
    
        title = soup_article.title.get_text()
        title = title.lower()

   
        find_date = soup_article.find('time', attrs={"class": "date"})
        for a in find_date.find_all('a'):
            find_valeur = re.compile('[0-9]{4}\/[0-9]{2}\/[0-9]{2}')
            for valeur in find_valeur.finditer(str(a.get("href"))):
                date_p = valeur.group(0)
                date_p = datetime.strptime(date_p, "%Y/%m/%d")\
                .strftime("%Y-%m-%d")

        # Retrieval of the author of the article
        author = []
        for div in soup_article.find_all('div'):
            if re.search('author', str(div.get("class"))):
                author.append(div.p.span.get_text())
  
        # Retrieval of the artical theme
        theme = ""
        for nav in soup_article.find_all('nav'):
            if nav.get("class") == ['breadcrumb']:
                for ol in nav.find_all('ol'):
                    for a in ol.find_all('a'):
                        theme = a.get_text()

            # Retrieving the content of the article
        contents = ""
        for div in soup_article.find_all('div'):
            if re.search('body', str(div.get("id"))):
                for aside in div.find_all('aside'):
                    for p in aside.find_all('p'):
                        p.string = ""
                for p in div.find_all('p'):
                    for a in p.find_all('a'):
                        if a.get("class") == ['lire']:
                            a.string = ""
                    for img in p.find_all('img'):
                        p.string = ""
                    contents += p.get_text() + " "

        data = [{"title": title,
                 "newspaper": 'NouvelObservateur',
                 "author": author,
                 "date_publi": date_p,
                 "theme": theme,
                 "content": contents
                    }]

        erreur="non"
        for tit in titre:
            if title == tit:
                erreur="oui"
        if len(contents) > 10 and erreur == "non":
            titre.append(title)
            utils.create_json(file_target, data, "nouvelobs", "noob")

    except:
        print("Probleme")