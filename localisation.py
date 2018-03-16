# -*- coding: utf-8 -*-
"""
@author: raphael
"""

"""
Ce code permet de nettoyer la liste de toutes les villes du 
monde par pays pris sur la page wikipédia de "liste des villes du monde"
"""

#chargement de packages utiles
import json
import re
import codecs

#chargement de la liste de toutes les villes du monde par pays
file = open('C:/Users/cmisid/Documents/TableauDeBord/liste_villes_par_pays_V3.json',encoding='utf-8')
liste_villes_par_pays_complet = json.load(file)

### liste de toutes les villes
list_vil = []
for dico_pays in liste_villes_par_pays_complet:
    for ville in dico_pays['villes']:
        list_vil.append(ville.lower())

      

# nettoyage des noms des villes et pays
pays = []
for dico in liste_villes_par_pays_complet: 
    div = dico['pays'].split(" ")
    if len(div)==1:
        dico['pays']=div[0].lower()
    if len(div)==3:
        if "saoudite" in div:
            dico['pays']="arabie saoudite"
            pays.append("arabie saoudite")
        if "Castelli" in div:
            dico['pays']="castelli de saint-Martin"
            pays.append("castelli de saint-Martin")
        else:
           dico['pays']= div[2].lower()
           pays.append(div[2].lower())
    if len(div)==2:
        if "(suède)" in div:
            dico['pays']="suède"
            pays.append("suède")
        else:
            if len(div[1].split("'"))==2:
                dico['pays']= div[1].split("'")[1].lower() 
                pays.append(div[1].split("'")[1].lower())
            elif len(div[1].split("'"))==1:
                dico['pays']= div[1].split("'")[0].lower() 
                pays.append(div[1].split("'")[0].lower())
    else:
        if "Cameroun" in div:
            dico['pays']="cameroun"
            pays.append("cameroun")
        elif "Comores" in div:
            dico['pays']="union des comores"
            pays.append("union des comores")
        elif "Congo)" in div:
            dico['pays']="république démocratique du congo"
            pays.append("république démocratique du congo")
        elif "d'Ivoire" in div:
            dico['pays']="côte d'Ivoire"
            pays.append("côte d'Ivoire")
        elif "Djibouti" in div:
            dico['pays']="djibouti"
            pays.append("djibouti")
        elif "Lesotho" in div:
            dico['pays']="lesotho"
            pays.append("lesotho")
        elif "Niger" in div:
            dico['pays']="niger"
            pays.append("niger")
        elif "Tomé-et-Principe" in div:
            dico['pays']="sao tomé-et-Principe"
            pays.append("sao tomé-et-Principe")
        elif "Tanzanie" in div:
            dico['pays']="tanzanie"
            pays.append("tanzanie")
        elif "Barbade" in div:
            dico['pays']="babarde"
            pays.append("babarde") 
        elif "Canada" in div:
            dico['pays']="canada"
            pays.append("canada")
        elif "Paraguay" in div:
            dico['pays']="paraguay"
            pays.append("paraguay")
        elif "Sainte-Lucie" in div:
            dico['pays']="sainte-Lucie"
            pays.append("sainte-Lucie")
        elif "Salvador" in div:
            dico['pays']="salvador"
            pays.append("salvador")
        elif "d'Armanie" in div:
            dico['pays']="armanie"
            pays.append("armanie")
        elif "Bhoutan" in div:
            dico['pays']="bhoutan"
            pays.append("bhoutan")
        elif "Birmanie" in div:
            dico['pays']="birmanie"
            pays.append("birmanie")
        elif "Émirats" in div:
            dico['pays']="émirats arabes unis"
            pays.append("émirats arabes unis")
        elif "Kazakhstan" in div:
            dico['pays']="kazakhstan"
            pays.append("kazakhstan")
        elif "d'Allemagne" in div:
            dico['pays']="allemagne"
            pays.append("allemagne")
        elif "France" in div:
            dico['pays']="france"
            pays.append("france")
        elif "hongrois)" in div:
            dico['pays']="hongrie"
            pays.append("hongrie")
        elif "d'Irlande" in div:
            dico['pays']="irlande"
            pays.append("irlande")
        elif "Malte" in div:
            dico['pays']="malte"
            pays.append("malte")
        elif "Moldavie" in div:
            dico['pays']="moldavie"
            pays.append("moldavie")
        elif "Portugal" in div:
            dico['pays']="portugal"
            pays.append("portugal")
        elif "Russie" in div:
            dico['pays']="russie"
            pays.append("russie")
        elif "tchèque" in div:
            dico['pays']="république tchèque"
            pays.append("république tchèque")
        elif "Slovaquie" in div:
            dico['pays']="slovaquie"
            pays.append("slovaquie")
        elif "Slovénie" in div:
            dico['pays']="slovénie"
            pays.append("slovénie")
        elif "d'Australie" in div:
            dico['pays']="australie"
            pays.append("australie")
        elif "Niue" in div:
            dico['pays']="niue"
            pays.append("niue")
        elif "Palaos" in div:
            dico['pays']="palaos"
            pays.append("palaos")
        else:
            if "la" in div[2:]:
                dico['pays']= " ".join(div[3:]).lower()
                pays.append(" ".join(div[3:]).lower())
            else:
                dico['pays']= " ".join(div[2:]).lower() 
                pays.append(" ".join(div[2:]).lower())
pays = list(set(pays)) + ['yemen','suède','états-unis']         

# suppression des termes indésirables dans la liste des villes
del_list = pays + ['cookie','musique','accueil','ville','villes','privacy','conditions','501c','allemand','afrique','chef-lieu']
toutes_les_villes = []
for dico in liste_villes_par_pays_complet:
    list_vil = [vil.lower() for vil in dico['villes']] 
    list_vil1 = []
    for vil in list_vil:
        if vil not in del_list:
            list_vil1.append(vil)
    liste_villes = []
    for vil in list_vil1:
        if len(vil.split(":"))==1 and len(vil.split("#"))==1 and  len(re.findall("([0-9]+)", vil)) ==0:
              liste_villes.append(vil)
    liste_villes = list(set(liste_villes))
    dico['villes']=liste_villes
    toutes_les_villes+=liste_villes


        

#      
localisation = []
i=0 
test=[]
for dico in data_final:
    if dico['pos_tag']=='PROPN':
        search = dico['lemma'].lower()
        test.append(search)
        if search in toutes_les_villes:
            for dictio in liste_villes_par_pays_complet:
                for vil in dictio['villes']:
                    if search==vil:
                        p=dictio['pays']
                        i+=1
            loc = {
                   "id_art": dico['id_art'],
                   "id_loc": i,
                   "pays": p,
                   "ville": search
                    }
            localisation.append(loc)
            
        elif search in pays:
            i+=1
            loc = {
                    "id_art": dico['id_art'],
                    "id_loc": i,
                    "pays": search,
                    "ville": ''
                  }
            localisation.append(loc)
    
     
if __name__ == '__main__':    
# creation de la liste de dictionnaire pour chaque mot
    with open('liste_villes_par_pays_complet.json', 'wb') as f: 
        json.dump(liste_villes_par_pays_complet, codecs.getwriter('utf-8')(f), ensure_ascii=False)
    

