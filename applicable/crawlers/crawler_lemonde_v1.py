import datetime as date
from datetime import datetime
import re
import utils_v0 as utils
import time

'''
Fonction qui prend en paramètre :
    une liste de dictionnaire + la liste des urls des articles
Cette fonction va pour chaque article récupérer:
    le thème, le titre, l'autheur, 
    la date de publication et le contenu de l'article
'''
def info_articles(list_dictionaries, list_url_articles):
    try:
        j = 0
        titre = []
        for url_article in list_url_articles:
            soup = utils.recovery_flux_url_rss(url_article)

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
                    author = soup.find("span",class_="auteur").find("a").get_text()
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

            new_article = utils.recovery_article(title, newspaper, author,
                                                 date_p, content, theme)

            if (j == 3):
                time.sleep(61)
                j = 0

            erreur = "non"
            for tit in titre:
                if title == tit:
                    erreur = "oui"
            if len(content) > 10 and erreur == "non":
                titre.append(title)
                list_dictionaries.append(new_article)

    except:
        print("Probleme")


'''
Fonction qui prend en paramètre :
    le chemin du dossier dans lequel fichier article sera mis
Cette fonction va récupérer les urls de chaque article qui parle d'attentat, 
terrorisme, impact attentat. Puis qui va faire appel à la fonction info_articles
pour récupérer le contenu, le titre etc..
puis après avoir récupérer les informations de chaque article, on les mets en json
'''
def recuperation_info_lmde(file_target="/Users/sofian/Documents/Projet_att/" +
                           str(date.datetime.now().date()) + "/"):

    list_url_articles = []
    j = 0
    # récupération des articles avec la recherche: impact attentat
    for i in range(1, 16):
        j = j+1
        url = 'http://www.lemonde.fr/recherche/?keywords=attentat+impact&page_num=' + str(i) +'&operator=and&exclude_keywords=&qt=recherche_texte_titre&author=&period=since_1944&start_day=01&start_month=01&start_year=1944&end_day=18&end_month=02&end_year=2018&sort=desc'
        soup = utils.recovery_flux_url_rss(url)

        for h3 in soup.find_all('h3'):
            for a in h3.find_all('a'):
                url = 'http://www.lemonde.fr' + a.get("href")
                list_url_articles.append(url)

        if (j == 3):
            time.sleep(61)
            j = 0

    # récupération des articles avec la recherche: attentat
    for i in range(1, 600):
        j = j+1
        url = 'http://www.lemonde.fr/recherche/?keywords=attentat&page_num=' + str(i) + "&operator=and&exclude_keywords=&qt=recherche_texte_titre&author=&period=since_1944&start_day=01&start_month=01&start_year=1944&end_day=31&end_month=01&end_year=2018&sort=desc"
        soup = utils.recovery_flux_url_rss(url)

        for h3 in soup.find_all('h3'):
            for a in h3.find_all('a'):
                url = 'http://www.lemonde.fr' + a.get("href")
                list_url_articles.append(url)

        if (j == 3):
            time.sleep(61)
            j = 0

    # récupération des articles avec la recherche: terrorisme
    for i in range(1, 800):
        j = j+1
        url = 'http://www.lemonde.fr/recherche/?keywords=terrorisme&page_num=' + str(i) + '&operator=and&exclude_keywords=&qt=recherche_texte_titre&author=&period=since_1944&start_day=01&start_month=01&start_year=1944&end_day=18&end_month=02&end_year=2018&sort=desc'

        soup = utils.recovery_flux_url_rss(url)

        for h3 in soup.find_all('h3'):
            for a in h3.find_all('a'):
                url = 'http://www.lemonde.fr' + a.get("href")
                list_url_articles.append(url)

        if (j == 3):
            time.sleep(61)
            j = 0

    list_dictionaries = []

    info_articles(list_dictionaries, list_url_articles)
    utils.create_json(file_target, list_dictionaries, "LeMonde/", "lmde")


if __name__ == '__main__':
    file_target = "/Users/sofian/Documents/Projet_att/" + str(date.datetime.now().date()) + "/"
    recuperation_info_lmde(file_target)
