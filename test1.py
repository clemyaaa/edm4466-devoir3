#coding : utf-8

#Dans ce devoir, je cherche à trouver tous les articles publiés en novembre 2019 qui parlent de féminicides. En France, chaque mois ede novembre, on en parle soudainement beaucoup plus et je suis curieuse de savoir si c'est vraiment le cas. Cela me permet aussi de m'avancer pour mon projet final. 

#Je commence par importer les bons modules

import requests, csv
from bs4 import BeautifulSoup

#Je crée une liste qui va générer toutes les dates des jours. Pas besoin de rajouter le 0 entre 1 et 9 parce que l'url fonctionne sans.

dates = list(range(1,31))

for jour in dates:
    # print(jour) Je vérifie que ça marche 
    url="https://www.lemonde.fr/archives-du-monde/{}-11-2019/".format(jour) #Je l'utilise pour rentrer le jour dans les accolades
    # print(url) #Pour tester

    entetes = {
    "User-Agent":"Clémence Bouquerod - +33647021901 - requête envoyée dans le cadre d'un cours en journalisme de données",
    "From":"clemence.bouquerod@iscpalyon.net"
} #Je crée mes entetes pour m'annoncer au site du monde 
    site = requests.get(url, headers = entetes) 
    # print(site.status_code) #Je teste pour voir si cela fonctionne. > "404". Je m'étais trompée dans le .format. Maintenant, le problème est reglé, alors je le met en commentaire

    page = BeautifulSoup(site.text, "html.parser") #Je vais chercher le code html dans les urls choisis
    # print(page) #Je vérifiais juste si ça marchait 

    # titreArticle = page.find_all("div", class="article__heading")
    # titreArticle = page.find_all("div", class_="article__heading")
    # titreArticle = page.find_all("div", class_="article_heading") Ca ne marche pas, j'en teste d'autres
    # titreArticle = page.find_all("h1", class_="article_title")
    # titreArticle = page.find("h1", class_="article__title")
    # print(titreArticle)

    #Je dois d'abord aller trouver tous les url d'article dans le jour 

    articles = page.find_all("section", class_="teaser") #Je vais chercher dans tous les url la classe "section, teaser" dans laquelle il y a la variable "a" qui contient l'url
    for article in articles: #Dans chaque jour avec pleins d'articles, je vais chercher l'url de chaque article 
        urlarticle = article.find("a")["href"] #Les urls sont dans la section a
        # print(urlarticle) #J'ai testé, ça marche, tous les url s'impriment. Je recommence ce que j'avais commencé plus haut 
        site2 = requests.get(urlarticle, headers=entetes)
        page2 = BeautifulSoup(site2.text, "html.parser")
        # print(site2.status_code) #Je vérifie que l'accès m'est autorisé. Il l'est
        # titreArticle = page2.find("h1", class_="article_title") Ca ne marche pas 
        # titreArticle = page2.find("div", class_="article__heading") Celui la non plus 
        try: #Je fais ça pour que ça ne bug pas si ce n'est pas exactement le même code html (par exemple pour les articles en live, qui ne m'interessent pas personnelement)
            titreArticle = page2.find("h1", class_="article__title").text.strip() #Je rajoute ces deux éléments pour que le titre soit plus lisible 
        except: 
            titreArticle =""
        # print(titreArticle)

        #Pour rappel, je cherche à trouver tous les articles publiés en novembre 2019 qui parlent de féminicide. Je crée donc une condition 

        # if titreArticle == "féminicide" or titreArticle == "Féminicide" or titreArticle == "Feminicide" or titreArticle == "feminicide":
            # print(titreArticle)
            #Après un temps de chargement de 30 minutes, cela ne m'a rien sorti...Je laisse donc tomber et essaye déjà de faire un fichier csv avec tous les articles, même s'ils ne parlent pas de féminicides. Je n'ai aucune idée de ce qu'il faut faire pour que ça marche. J'ai pensé à faire une autre variable pour ne garder que ces articles-ci, mais je ne sais pas comment faire pour créer une recherche parmi les titres et avec if je ne crois pas qu'on puisse créer une variable... 
            #Donc je suis incapable de chercher ce que je voulais  

        #J'aimerai bien afficher les titres et les dates de publications dans la fichier csv final. Pour ça, je vais essayer de trouver maintenant les dates : 

        try:
            dates = page2.find("span", class_="meta__date").text.strip() #Encore une fois je rajoute ces éléments pour que ce soit plus visible & j'utilise le try au cas ou ca bug 
        except:
            date =""
        # print(dates) #Cela fonctionne bien

        #Je dois faire un fichier csv avec ces deux résultats. J'ai déjà importé csv. Je dois maintenant créer ma variable avec le fichier csv 

        fichier = "féminicidesnov.csv" 

        #Je dois aussi créer une liste dans laquelle il y aura l'url,  la date et le titre de l'article 

        #Je suis ce qu'on avait fait dans un cours précedent : 
        #Je crée une variable qui ouvre le fichier avec la fonction open puis avec le fameux "a" qui me permet d'écrire dans le fichier en mode "append"

        ouvrir = open(fichier,"a")

        #Je crée une variable liste dans laquelle je rentre la variable titreArticle et dates

        liste = []
        liste.append(titreArticle)
        liste.append(dates)

        #J'utilise la fonction writer en créant une autre variable 

        creer = csv.writer(ouvrir)
        creer.writerow(liste)

#N'ayant pas réussi à créer un fichier csv la dernière fois, je suis ravie que cette fois-ci cela ai fonctionné ! Même si j'ai été incapa ble d'y restreindre aux articles parlant de féminicides. 
#Pourriez-vous m'expliquer ce que j'ai fait de faux? Après j'aurai enfin compris les derniers cours ! 
#Merci d'avance

    



