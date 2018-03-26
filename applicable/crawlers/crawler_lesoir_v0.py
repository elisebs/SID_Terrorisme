# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 02:04:40 2018
@author: Raphael
"""
import datetime as date
import re
import g4_utils_v40 as utils
import time


def collect_articles(list_dictionaries, list_url_articles, list_titre):
    j = 0
    for url_article in list_url_articles:
        j = j+1
        soup = utils.recovery_flux_url_rss(url_article)

        for titl in soup.find_all('title'):       # find the title
            tit = titl.get_text()
            if len(tit.split('-')) == 2:
                title = tit.split('-')[0]

        authors = []
        for a in soup.find_all('a'):             # find the authors
            if a.get('href') is not None:
                if "dpi-authors" in a.get('href').split('/'):
                    tit = a.get('href').split('/')[-1]
                    authors.append(tit.split('-')[0] + ' ' + tit.split('-')[1])
        if len(authors) == 0:
            authors.append('')

        dates = []
        date_publication = []
        for balise_time in soup.find_all('time'):     # find publication's date
            if 'pubdate' in balise_time.get('class'):
                dates.append(balise_time.get('datetime').split('T')[0])
                date_publication.append(
                        balise_time.get('datetime').split('T')[0])

        theme = re.search("www.lesoir.be/(.*)/", url_article)[1]

        content = ''
        for p in soup.find_all('p'):
            if len(p.get_text().split(" ")) >= 2:
                content += p.get_text()

        new_article = utils.recovery_article(title, 'lesoir', authors,
                                             date_publication, content, theme)

        if (j == 3):
            time.sleep(71)
            j = 0

        if not utils.is_empty(new_article):
            erreur = "non"
            for tit in list_titre:
                if title == tit:
                    erreur = "oui"
            if len(content) > 10 and erreur == "non":
                list_titre.append(title)
                list_dictionaries.append(new_article)


def recovery_new_articles_lpt(
        file_target="C:/Users/cmisid/Documents/TableauDeBord/LESOIR/"
        + str(date.datetime.now().date()) + "/"):

    list_url_articles = []
    j = 0
    for i in range(0, 1650, 10):
        j = j+1
        url1 = 'http://www.lesoir.be/archives/recherche?datefilter=lastyear&sort=date+desc&start=' 
        + str(i) + '&word=terrorisme'
        soup1 = utils.recovery_flux_url_rss(url1)

        for a in soup1.find_all('a'):
            tit = a.get('href')
            if '/archive/' in tit.split('d'):
                url = 'http://www.lesoir.be' + tit
                list_url_articles.append(url)


        url2 = 'http://www.lesoir.be/archives/recherche?datefilter=lastyear&sort=date+desc&start='
        + str(i) + '&word=attentat'
        soup2 = utils.recovery_flux_url_rss(url2)

        for a in soup2.find_all('a'):
            tit = a.get('href')
            if '/archive/' in tit.split('d'):
                url = 'http://www.lesoir.be' + tit
                list_url_articles.append(url)

        if (j == 3):
            time.sleep(71)
            j = 0

    list_dictionaries = []
    list_titre = []
    collect_articles(list_dictionaries, list_url_articles, list_titre)
    utils.create_json(file_target, list_dictionaries, "lesoir/", "lsr")


if __name__ == '__main__':

    file_target = "C:/Users/cmisid/Documents/TableauDeBord/LESOIR/"
    + str(date.datetime.now().date()) + "/"
    recovery_new_articles_lpt(file_target)
