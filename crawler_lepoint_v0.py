import datetime as date
import re
import utils_v0 as utils
import time


def collect_articles(list_dictionaries, list_url_articles):
    """Add the articles (dictionaries) from a list of URL in a list of
    dictionaries
    Arguments:
        list_dictionaries {list} -- list of dictionaries
        list_url_articles {list} -- list of URL
        theme {string} -- theme related to the list of dictionaries
    """
    ## Boucle qui va pour chaque url d'un article récupéré les informations (titre, date de publication, auteur, le theme et le contenu de l'article
    for url_article in list_url_articles:
        soup = utils.recovery_flux_url_rss(url_article) # récupère le code html de l'url

        balise_title = soup.title.string # récupère le titre de l'article
        sep = balise_title.split(" - Le Point")
        title = sep[0] 

        list_authors = []
        # On va récupéré les auteurs qui sont dans une balise <span> qui est dans une balise <div>
        for div in soup.find_all('div'):
            if div.get('class') == ['mbs']:
                for span in div.find_all('span'):
                    name = span.get_text()
                    name = re.sub('Par', '', name)
                    name = re.sub('\n', '', name)
                    list_authors.append(name)

        dates = []
        # On va récupéré la date qui est dans une balise <time>
        for balise_time in soup.find_all('time'):
            for valeur in re.finditer('[0-9]{2}\/[0-9]{2}\/[0-9]{4}',
                                      str(balise_time)):
                dates.append(date.datetime.strptime(valeur.group(0),
                                                    '%d/%m/%Y'))
        date_publication = date.datetime.strftime(min(dates), '%d/%m/%Y')
        date_publication = str(date.datetime.strptime(date_publication,
                                                      "%d/%m/%Y").date())

		# On récupère le theme à l'aide de l'url de l'article par exemple : "http:/www.lepoint.fr/ "  pour cette article on récupère le thème sport
        theme = re.search("www.lepoint.fr/(.*)/", url_article)[1]
		
		# On va récupéré le contenu de l'article qui est dans une balise <h2 class='art-chapeau'> et aussi dans une balise <div class='art-text">
		content = ''
        for h2 in soup.find_all('h2'):
            if h2.get('class') == ['art-chapeau']:
                content += h2.get_text()+" "
        for div in soup.find_all('div'):
            if div.get('class') == ['art-text']:
                for p in div.find_all('p'):
                    content += p.get_text()+" "

        new_article = utils.recovery_article(title, 'LePoint',
                                             list_authors,
                                             date_publication, content,
                                             theme)
        if not utils.is_empty(new_article):
            list_dictionaries.append(new_article)


def recovery_new_articles_lpt(file_target="/Users/sofian/Documents/Projet_att/" +
                              str(date.datetime.now().date()) + "/"):
    """Procedure that calls all the others functions and procedures in order to
    collect articles from a newspaper in a file
    Arguments:
        file_target {string} -- path where the articles will be recorded
    """    
    list_url_articles = []
    # boucle qui va aller de la page 1 à la page 95 de la recherche attentat
    for i in range(1, 95):
        url = 'http://www.lepoint.fr/recherche/index.php?query=attentats&page=' + str(i)
        soup = utils.recovery_flux_url_rss(url) # récupère le code html de l'url

		# on récupère tout les urls des articles qui sont dans les balises <div class='image-search-wrap'> <figure> </figure> </div>
        for div in soup.find_all('div'):
            if re.search('image-search-wrap', str(div.get("class"))): 
                for fig in div.find_all('figure'):
                    url = "http://www.lepoint.fr" + fig.a.get("href")
                    list_url_articles.append(url)
        time.sleep(61) # On se met en veille pendant 61 secondes pour pas que le site internet reconnaisse qu'on soit un robot
    list_dictionaries = []
    
    collect_articles(list_dictionaries, list_url_articles) ## Appel à la fonction collect_articles, pour avoir les informations de l'article
     
    utils.create_json(file_target, list_dictionaries, "LePoint/",
                          "lpt") # On crée le fichier json pour chaque article


if __name__ == '__main__':
    file_target = "/Users/sofian/Documents/Projet_att/" + str(date.datetime.now().date()) + "/"
    recovery_new_articles_lpt(file_target)
