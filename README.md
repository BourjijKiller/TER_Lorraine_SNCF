# UTILITAIRE DE RECHERCHE DE TRAJET TER & BUS SNCF EN RÉGION LORRAINE

---------------------------------------------------------------------------------

## DESCRIPTION

Ce projet consiste à mêler programmation et mathématiques pour, au final, produire un programme qui demande la saisie de deux gares desservies par le réseau **TER METROLOR**, ayant pour but de donner l'itinéraire _le plus rapide (et non pas le plus court)_ parmi les nombreux chemins existants.

En résumé, le but est de s'appuyer sur les outils informatiques pour reproduire un utilitaire de recherche de trajets en région Lorraine uniquement entre les villes (cet outil ne prend pas en compte les villages et hameau).

Afin de réaliser ce programme, nous nous sommes appuyé sur le plan ferroviaire du réseau **TER Lorraine**, que vous pouvez aperçevoir ci-dessous.

![](https://image.noelshack.com/fichiers/2018/09/6/1520074546-plan-terlor.png)

---------------------------------------------------------------------------------

## NOTIONS UTILISÉES

**[EN COURS]**

---------------------------------------------------------------------------------

## ASPECTS TECHNIQUES

**[EN COURS]**

---------------------------------------------------------------------------------

## OPÉRATIONS POSSIBLES

**[EN COURS]**

---------------------------------------------------------------------------------

## INSTALLATION ET LANCEMENT

**Avant tout, il est important, afin d'exécuter ce programme, de posséder l'environnement [Python](https://www.python.org/) sur votre machine**.

### Sous Linux

Sous les systèmes Linux, l'installation de l'environnement **Python** est plutôt simple. Ouvrir un terminal et taper la commande suivante :

* Pour **_Python 2.7 (installé par défaut normalement)_**
	```console
	$ sudo apt-get install python
	```

* Pour **_Python 3.6_**
	* Sous Ubuntu 14.04 et 16.04 :
		```console
		$ sudo add-apt-repository ppa:jonathonf/python-3.6
		$ sudo apt update
		$ sudo apt-get install python3.6
		```
	* Sous Ubuntu 17.04, **_Python 3.6_** est proposé dans le dépôt universe :
		```console
		$ sudo apt-get install python3.6
		```
	* Sous Ubuntu 17.10, **_Python 3.6_** est installé par défaut

* Vérification que Python est bien installé :
	```console
	$ python --version
	```

### Sous Windows

**[Si vous utilisez un terminal contenant un environnement Bash (Bash Ubuntu sous Windows / git bash / etc...), suivre la procédure ci-dessus]**

Sous les systèmes Windows, il faut se rendre sur la [page de téléchargement](https://www.python.org/downloads/) de Python et télécharger la version de votre choix.
Une fois téléchargé, il faut extraire le dossier de nom _**Python-xx-xx-xx (xx étant les numéros de version)**_ dans votre répertoire **Program Files (x86)** (`C:\Program Files (x86)`).
Enfin, pour pouvoir utiliser Python en ligne de commande, il est nécessaire d'ajouter le dossier que vous venez de télécharger dans les variables d'environnements de Windows.

1. Cliquer sur _Démarrer_
2. Clique droit sur _Ordinateur_ (ou _Ce PC_, dépend de votre version de Windows) --> _Propriétés_
3. Cliquer sur _Paramètres système avancés_
4. Cliquer sur _Variables d'environnement_
5. Double cliquer sur la variable de nom _Path_, une nouvelle fenêtre s'ouvre
6. Appuyer sur le bouton _Nouveau_, et ajouter le chemin vers votre dossier Python
7. Appuyer sur Ok sur toute les fenêtres ouvertes

* Vérification que Python est bien installé :
	```console
	$ python
	```

Une fois que **Python** est installé, vous remarquez l'existence de 2 fichiers :

* **BDD.py** --> Fichier correspondant à la base de données SQLite 3, contenant tout les trajets possibles, ce qui est nécessaire pour le programme principal.
* **TER2.py** --> Fichier contenant le programme d'exécution.

Placez ces deux fichiers au même endroits, et exécuter d'abord le fichier **BDD.py** :

* Python 2
	```console
	python BDD.py
	```
* Python 3.6
	```console
	python3.6 BDD.py
	```

Cette commande permet de générer un fichier d'extension _**.db**_, utilisé par le programme d'exécution, correspondant à la base de données.

Si vous exécuter **TER2.py** avant **BDD.py**, le programme affichera un message d'erreur...

![](https://image.noelshack.com/fichiers/2018/09/6/1520077532-fail-bd.png)

Enfin, pour lancer le programme, taper la commande :

* Python 2
	```console
	python TER2.py
	```
* Python 3.6
	```console
	python3.6 TER2.py
	```

---------------------------------------------------------------------------------

## RESSOURCES EXTERNES

Pour plus d'informations sur le projet, vous pouvez consulter [ce lien !](http://teammetrolor.xooit.org/index.php)

---------------------------------------------------------------------------------

## COLLABORATEURS DU PROJET

Ce projet s'inscrit dans le cadre de la formation **[DUT Informatique deuxième année]**, et a été réalisé en groupe, avec :

* **GOURMELON Lucas**
* **DAVAL Baptiste**