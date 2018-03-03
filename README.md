# UTILITAIRE DE RECHERCHE DE TRAJET TER & BUS SNCF EN R�GION LORRAINE

---------------------------------------------------------------------------------

## DESCRIPTION

Ce projet consiste � m�ler programmation et math�matiques pour, au final, produire un programme qui demande la saisie de deux gares desservies par le r�seau **TER METROLOR**, ayant pour but de donner l'itin�raire _le plus rapide (et non pas le plus court)_ parmi les nombreux chemins existants.

En r�sum�, le but est de s'appuyer sur les outils informatiques pour reproduire un utilitaire de recherche de trajets en r�gion Lorraine uniquement entre les villes (cet outil ne prend pas en compte les villages et hameau).

Afin de r�aliser ce programme, nous nous sommes appuy� sur le plan ferroviaire du r�seau **TER Lorraine**, que vous pouvez aper�evoir ci-dessous.

![](https://image.noelshack.com/fichiers/2018/09/6/1520074546-plan-terlor.png)

---------------------------------------------------------------------------------

## NOTIONS UTILIS�ES

**[EN COURS]**

---------------------------------------------------------------------------------

## ASPECTS TECHNIQUES

**[EN COURS]**

---------------------------------------------------------------------------------

## OP�RATIONS POSSIBLES

**[EN COURS]**

---------------------------------------------------------------------------------

## INSTALLATION ET LANCEMENT

**Avant tout, il est important, afin d'ex�cuter ce programme, de poss�der l'environnement [Python](https://www.python.org/) sur votre machine**.

### Sous Linux

Sous les syst�mes Linux, l'installation de l'environnement **Python** est plut�t simple. Ouvrir un terminal et taper la commande suivante :

* Pour **_Python 2.7 (install� par d�faut normalement)_**
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
	* Sous Ubuntu 17.04, **_Python 3.6_** est propos� dans le d�p�t universe :
		```console
		$ sudo apt-get install python3.6
		```
	* Sous Ubuntu 17.10, **_Python 3.6_** est install� par d�faut

* V�rification que Python est bien install� :
	```console
	$ python --version
	```

### Sous Windows

**[Si vous utilisez un terminal contenant un environnement Bash (Bash Ubuntu sous Windows / git bash / etc...), suivre la proc�dure ci-dessus]**

Sous les syst�mes Windows, il faut se rendre sur la [page de t�l�chargement](https://www.python.org/downloads/) de Python et t�l�charger la version de votre choix.
Une fois t�l�charg�, il faut extraire le dossier de nom _**Python-xx-xx-xx (xx �tant les num�ros de version)**_ dans votre r�pertoire **Program Files (x86)** (`C:\Program Files (x86)`).
Enfin, pour pouvoir utiliser Python en ligne de commande, il est n�cessaire d'ajouter le dossier que vous venez de t�l�charger dans les variables d'environnements de Windows.

1. Cliquer sur _D�marrer_
2. Clique droit sur _Ordinateur_ (ou _Ce PC_, d�pend de votre version de Windows) --> _Propri�t�s_
3. Cliquer sur _Param�tres syst�me avanc�s_
4. Cliquer sur _Variables d'environnement_
5. Double cliquer sur la variable de nom _Path_, une nouvelle fen�tre s'ouvre
6. Appuyer sur le bouton _Nouveau_, et ajouter le chemin vers votre dossier Python
7. Appuyer sur Ok sur toute les fen�tres ouvertes

* V�rification que Python est bien install� :
	```console
	$ python
	```

Une fois que **Python** est install�, vous remarquez l'existence de 2 fichiers :

* **BDD.py** --> Fichier correspondant � la base de donn�es SQLite 3, contenant tout les trajets possibles, ce qui est n�cessaire pour le programme principal.
* **TER2.py** --> Fichier contenant le programme d'ex�cution.

Placez ces deux fichiers au m�me endroits, et ex�cuter d'abord le fichier **BDD.py** :

* Python 2
	```console
	python BDD.py
	```
* Python 3.6
	```console
	python3.6 BDD.py
	```

Cette commande permet de g�n�rer un fichier d'extension _**.db**_, utilis� par le programme d'ex�cution, correspondant � la base de donn�es.

Si vous ex�cuter **TER2.py** avant **BDD.py**, le programme affichera un message d'erreur...

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

Ce projet s'inscrit dans le cadre de la formation **[DUT Informatique deuxi�me ann�e]**, et a �t� r�alis� en groupe, avec :

* **GOURMELON Lucas**
* **DAVAL Baptiste**