# Requête 1 : JOURNAUX | ANNEE | NB D'ARTICLES PUBLIES
SELECT name_np, YEAR(date_pub) AS annee, COUNT(id_article) AS nb_articles
FROM ARTICLE
GROUP BY name_np, YEAR(date_pub)
ORDER BY name_np, YEAR(date_pub);

# Requête 2 : LEMMA | OCCURENCE --> TOP 50
SELECT TOP 50 lemma, COUNT(id_word) AS nb_word
FROM WORD
GROUP BY lemma
ORDER BY nb_word DESC;

# Requête 3 ANNEE | NB D'ARTICLES PUBLIES
SELECT YEAR(date_pub) AS annee, COUNT(id_article) AS nb_articles
FROM ARTICLE
GROUP BY YEAR(date_pub)
ORDER BY YEAR(date_pub);

# Requête 4 : VILLES | OCCURENCE --> TOP 50
SELECT TOP 50 city, COUNT(id_localisation) AS nb_loc
FROM LOCALISATION
GROUP BY city
ORDER BY nb_loc DESC;

# Requête 5 : LEMMA | ANNEE | NB D'OCCURENCES
SELECT lemma, YEAR(date_pub), COUNT(id_word) AS nb_occ
FROM WORD, ARTICLE
WHERE (lemma='peur' 
OR lemma='terreur'
OR lemma='crainte'
OR lemma='colere'
OR lemma='rage' 
OR lemma='haine'
OR lemma='tristesse'
OR lemma='chagrin'
OR lemma='peine'
OR lemma='joie'
OR lemma='content')
AND WORD.id_article = ARTICLE.id_article
GROUP BY lemma, YEAR(date_pub)
ORDER BY lemma, YEAR(date_pub);

# Requête 5 bis 
SELECT YEAR(date_pub), COUNT(WORD.id_article)
FROM WORD, ARTICLE
WHERE (lemma='tristesse'
OR lemma='chagrin'
OR lemma='peine')
AND WORD.id_article = ARTICLE.id_article
GROUP BY YEAR(date_pub)
ORDER BY YEAR(date_pub);

SELECT YEAR(date_pub), COUNT(WORD.id_article)
FROM WORD, ARTICLE
WHERE (lemma='colere'
OR lemma='rage' 
OR lemma='haine')
AND WORD.id_article = ARTICLE.id_article
GROUP BY YEAR(date_pub)
ORDER BY YEAR(date_pub);

SELECT YEAR(date_pub), COUNT(WORD.id_article)
FROM WORD, ARTICLE
WHERE (lemma='peur' 
OR lemma='terreur'
OR lemma='crainte')
AND WORD.id_article = ARTICLE.id_article
GROUP BY YEAR(date_pub)
ORDER BY YEAR(date_pub);

SELECT YEAR(date_pub), COUNT(WORD.id_article)
FROM WORD, ARTICLE
WHERE (
lemma='joie'
OR lemma='content')
AND WORD.id_article = ARTICLE.id_article
GROUP BY YEAR(date_pub)
ORDER BY YEAR(date_pub);



# Requête 6 : LEMMA | ANNEE | NB D'OCCURENCE
SELECT lemma, YEAR(date_pub), COUNT(id_word) AS nb_occ
FROM WORD, ARTICLE
WHERE (lemma='loi' 
OR lemma='droit'
OR lemma='politique'
OR lemma='etat'
OR lemma='securite'
OR lemma='danger'
OR lemma='effrayer'
OR lemma='danger'
OR lemma='insecurite'
OR lemma='peur' 
OR lemma='terreur'
OR lemma='crainte')
AND WORD.id_article = ARTICLE.id_article
GROUP BY lemma, YEAR(date_pub)
ORDER BY lemma, YEAR(date_pub);
 
# Requête 7 : PAYS | VILLE | NB D'OCCURENCE
SELECT country, city, count(id_localisation) AS nb_loc
FROM LOCALISATION
GROUP BY country, city
ORDER BY country, city;

# Requête 8 : PAYS | NB D'OCCURENCE
SELECT country, count(id_localisation) AS nb_loc
FROM LOCALISATION
GROUP BY country
ORDER BY country;

# Requête 9 : VILLE FRANCAISE | NB D'OCCURENCE
SELECT city, count(id_localisation) AS nb_loc
FROM LOCALISATION
WHERE country='france'
GROUP BY city
ORDER BY city;

# Requête 10 : LEAMMA | MOIS | ANNEE | NB D'OCCURENCE
SELECT lemma, MONTH(date_pub), YEAR (date_pub), COUNT(id_word) AS nb_occ
FROM WORD, ARTICLE
WHERE (YEAR(date_pub)='2017' OR YEAR(date_pub)='2016' OR YEAR(date_pub)='2015')
AND (lemma='politique' 
OR lemma='loi'
OR lemma='antiterroriste'
OR lemma='droit')
AND WORD.id_article = ARTICLE.id_article
GROUP BY lemma, YEAR(date_pub), MONTH(date_pub)
ORDER BY lemma, YEAR(date_pub), MONTH(date_pub);
 
# Requête 11 : VILLES | OCCURENCE --> TOP 150
SELECT TOP 150 city, COUNT(id_localisation) AS nb_loc
FROM LOCALISATION
GROUP BY city
ORDER BY nb_loc DESC;

