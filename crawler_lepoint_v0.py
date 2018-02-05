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
    for url_article in list_url_articles:
        soup = utils.recovery_flux_url_rss(url_article)

        balise_title = soup.title.string
        sep = balise_title.split(" - Le Point")
        title = sep[0]

        list_authors = []
        for div in soup.find_all('div'):
            if div.get('class') == ['mbs']:
                for span in div.find_all('span'):
                    name = span.get_text()
                    name = re.sub('Par', '', name)
                    name = re.sub('\n', '', name)
                    list_authors.append(name)

        dates = []
        for balise_time in soup.find_all('time'):
            for valeur in re.finditer('[0-9]{2}\/[0-9]{2}\/[0-9]{4}',
                                      str(balise_time)):
                dates.append(date.datetime.strptime(valeur.group(0),
                                                    '%d/%m/%Y'))
        date_publication = date.datetime.strftime(min(dates), '%d/%m/%Y')
        date_publication = str(date.datetime.strptime(date_publication,
                                                      "%d/%m/%Y").date())

        theme = re.search("www.lepoint.fr/(.*)/", url_article)[1]

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
    for i in range(1, 95):
        url = 'http://www.lepoint.fr/recherche/index.php?query=attentats&page=' + str(i)
        soup = utils.recovery_flux_url_rss(url)

        for div in soup.find_all('div'):
            if re.search('image-search-wrap', str(div.get("class"))): 
                for fig in div.find_all('figure'):
                    url = "http://www.lepoint.fr" + fig.a.get("href")
                    list_url_articles.append(url)
        time.sleep(61)

    list_dictionaries = []
    
    collect_articles(list_dictionaries, list_url_articles)
     
    utils.create_json(file_target, list_dictionaries, "LePoint/",
                          "lpt")


if __name__ == '__main__':
    file_target = "/Users/sofian/Documents/Projet_att/" + str(date.datetime.now().date()) + "/"
    recovery_new_articles_lpt(file_target)
