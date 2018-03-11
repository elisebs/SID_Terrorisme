# -*- coding: utf-8 -*-
"""
@author: Raphael
"""

import bs4
import requests
import time
import json, codecs

liste_pays = ['Villes de Suisse', 'Villes du Brésil', "Villes d'Argentine",
        'Villes du Chili', 'Villes de Bolivie', "Villes d'Uruguay",
        'Villes du Panama', 'Villes du Costa Rica', 'Villes du Honduras',
        'Villes du Guatemala', 'Villes de Cuba', "Villes d'Haïti", 
        'Villes de la République dominicaine','Villes de Jamaïque', 
        "Villes d'Islande",  'Villes du Suriname', 
        'Villes du Nicaragua','Villes de France','Villes de Russie',
        'Villes de Turquie','Villes de la Namibie', 'Villes du Botswana',
        'Villes du Zimbabwe','Villes du Mozambique',"Villes des États-Unis",
        'Villes de Zambie', "Villes d'Angola",
        'Villes de Tanzanie', 'Villes de la République démocratique du Congo',
        'Villes du Gabon','Villes de République du Congo', 
        'Villes du Soudan','Villes du Soudan du Sud', "Villes d'Érythrée",
        'Villes du Ghana','Villes du Togo', 'Villes du Bénin', 'Villes du Burkina Faso', 
        'Villes du Liberia', 'Villes de Sierra Leone', 
        'Villes de Guinée', 'Villes de Guinée-Bissau', 
        'Villes de Gambie', 'Villes du Sénégal','Villes du Portugal',
        'Villes de Malte', 'Villes de Roumanie', 'Villes de Slovénie', 
        "Villes d'Autriche",'Villes de Hongrie','Villes de Slovaquie', 
        'Villes de République tchèque',"Villes de la République d'Irlande", "Villes d'Estonie",
        'Villes de Lettonie', 'Villes de Lituanie','Villes de Biélorussie', 'Villes de Moldavie',
        'Villes de République de Macédoine', 'Villes de Géorgie', 'Villes du Kazakhstan',
        'Villes de Mongolie','Villes du Népal', 'Villes du Bhoutan', 'Villes de Malaisie',
        'Villes du Cambodge','Villes du Laos', 'Villes du Viêt Nam',
        'Villes de Nouvelle-Zélande',"Villes d'Afghanistan", 'Villes du Pakistan'
        'Villes de Bahreïn',"Villes d'Irak",
        "Villes d'Iran","Villes d'Israël",'Villes du Pakistan',
        'Villes du Liban',"Villes d'Ukraine","Villes d'Espagne",
        'Villes du Nigeria','Villes du Guyana','Villes des Bahamas']

def recovery_flux_url_rss(url_rss):
    """
    input : url 
    output : code XHTML 
    Prend en entrée le lien de la page et renvoi le code XHTML correspondant
    """
    req = requests.get(url_rss)
    data = req.text
    soup = bs4.BeautifulSoup(data, "lxml")
    return(soup)
    
def recovery_country(title, content):
    """
    input: title(nom du pays) et content(liste de ses villes)
    output: dictionnaire
    Prend en entrée le nom du pays et une liste contenant ses villes
    et renvoi un dictionnaire de clés PAYS et VILLES
    """
    pays_villes = {
                    "pays": title,
                    "villes": content
                  }
    return(pays_villes)

def collect_country(list_dictionaries, list_url_pays):
    """
    input: liste vide
           liste des url de chaque pays
    output: la liste vide remplie par des dictionnaires(pays,villes) correspondant a
            chaque pays
    """
    i = 0
    for url_pays in list_url_pays:          # pour trouver le code xhtml associé a l'url
       i+=1
       soup = recovery_flux_url_rss(url_pays) 
       
       for title in soup.find_all('title'):       # pour recherche le nom du pays
            l = title.get_text()
            if 'Wikipédia' in l.split(' — '):
                title = l.split(' — ')[0]
                 
       if title in liste_pays :      # verifie si le pays est dans la liste des pays cible
        content = []    #liste  vide des villes                 
        j=0
        for a in soup.find_all('a'): # recherche des villes associées au pays
           j +=1 
           if a.get("href") != None :
              e = a.get("href").split("/wiki/")
              if len(e) == 2:
                if len(e[1].split('_')) <= 2:
                   if len(e[1].split('_')) == 2:
                     if len(e[1].split('_')[0].split("%"))==1:
                         content.append(e[1].split('_')[0])
                   else:
                       if len(e[1].split("%"))==1:   
                         content.append(e[1])
                if (j%8 == 0):
                    time.sleep(2)
        content = list(set(content)) 
            
        new_country = recovery_country(title, content)
        list_dictionaries.append(new_country)
       if (i%8 == 0):
            time.sleep(2)
    return (list_dictionaries)
        
        

list_url_pays = []
url = "https://fr.wikipedia.org/wiki/Listes_des_villes_du_monde"
soup = recovery_flux_url_rss(url)
i=0
for li in soup.find_all('li'):
    if len(list_url_pays)>163:
        break
    else:
        i +=1
        for a in soup.find_all('a'):
            if len(list_url_pays)>163:
                break
            else:
               l = a.get('href')
               if l!=None:
                   if "/wiki/Villes" in l.split("_"):
                     url = 'https://fr.wikipedia.org' + l
                     list_url_pays.append(url)
                     if (i%16 == 0):
                         time.sleep(1)
        
list_dictionaries = []
liste_villes_par_pays_V2 = collect_country(list_dictionaries, list_url_pays)    

  
if __name__ == '__main__':
    with open('liste_villes_par_pays_V2.json', 'wb') as f: 
        json.dump(liste_villes_par_pays_V2, codecs.getwriter('utf-8')(f), ensure_ascii=False)
 