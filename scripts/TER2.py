#!/usr/bin/python
# -*- coding: utf-8 -*-

# Les imports nécessaires pour le fonctionnement du programme 
import os
from math import *
import random
import sqlite3
from time import *


def affiche_peres(pere,depart,extremite,trajet):
	"""
	À partir du dictionnaire des pères de chaque sommet on renvoie
	la liste des sommets du plus court chemin trouvé. Calcul récursif.
	On part de la fin et on remonte vers le départ du chemin.
	
	"""
	if extremite == depart:
		return [depart] + trajet
	else:
		return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))
 
def plus_court(graphe,etape,fin,visites,dist,pere,depart):
	"""
	Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
	visites est une liste et dist et pere des dictionnaires 
	graphe  : le graphe étudié                                                               (dictionnaire)
	étape   : le sommet en cours d'étude                                                     (sommet)
	fin     : but du trajet                                                                  (sommet)
	visites : liste des sommets déjà visités                                                 (liste de sommets)
	dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
	pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
	depart  : sommet global de départ                                                        (sommet)
	Retourne le couple (longueur mini (int), trajet correspondant (liste sommets)) 
	   
	"""
	# si on arrive à la fin, on affiche la distance et les peres
	if etape == fin:
		return dist[fin], affiche_peres(pere,depart,fin,[])
	# si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
	if len(visites) == 0:dist[etape]=0
	# on commence à tester les voisins non visités
	for voisin in graphe[etape]:
		if voisin not in visites:
			# la distance est soit la distance calculée précédemment soit l'infini
			dist_voisin = dist.get(voisin,float('inf'))
			# on calcule la nouvelle distance calculée en passant par l'étape
			candidat_dist = dist[etape] + graphe[etape][voisin]
			# on effectue les changements si cela donne un chemin plus court
			if candidat_dist < dist_voisin:
				dist[voisin] = candidat_dist
				pere[voisin] = etape
	# on a regardé tous les voisins : le noeud entier est visité
	visites.append(etape)
	# on cherche le sommet *non visité* le plus proche du départ
	non_visites = dict((s, dist.get(s,float('inf'))) for s in graphe if s not in visites)
	noeud_plus_proche = min(non_visites, key = non_visites.get)
	# on applique récursivement en prenant comme nouvelle étape le sommet le plus proche 
	return plus_court(graphe,noeud_plus_proche,fin,visites,dist,pere,depart)
 
def dij_rec(graphe,debut,fin):
	return plus_court(graphe,debut,fin,[],{},{},debut)

def Connection():
	# Connection à la base de donnée SQLite
	try:
		liste = []
		connection = sqlite3.connect('Gares.db')
		connection.text_factory = str
		cursor = connection.cursor()
		cursor.execute("""SELECT * FROM Gares""")
		for row in cursor:
			liste += '{0} : {1}, {2}'.format(row[0], row[1], row[2])
		return liste
	except sqlite3.OperationalError:
		print("\n La base de donnée .db n'existe pas....")
	except Exception as e:
		print("\n Erreur \n")
		connection.rollback()
		#raise e
	finally:
		print("\n Fermeture de la connexion \n")
		connection.close()

def Existence(gareDepart, gareArrivee):

	connection = sqlite3.connect('Gares.db')
	connection.text_factory = str
	cursor=connection.cursor()

	cursor.execute("""SELECT * FROM gares WHERE depart=?""",(gareDepart,))
	results=cursor.fetchall()
	if(results==[]):
		print("\n [*] Erreur: La gare de départ spécifiée n'existe pas [*] \n")
		exit()
	else:
		print("\n [*] La gare de départ spécifiée existe bien [*] \n")

	cursor.execute("""SELECT * FROM gares WHERE arrivee=?""",(gareArrivee,))
	results=cursor.fetchall()
	if(results==[]):
		print("\n [*] Erreur: La gare d'arrivée spécifiée n'existe pas [*] \n")
		exit()
	else:
		print("\n [*] La gare d'arrivée spécifiée existe bien [*] \n")
	connection.close()

def Vehicule(trajet):
	connection = sqlite3.connect('Gares.db')
	connection.text_factory = str
	cursor = connection.cursor()
	train = False
	bus = False
	mix = False
	for i in range(0,len(trajet)-1):
		cursor.execute("""SELECT vehicule FROM gares WHERE depart=? AND arrivee=?""",(trajet[i],trajet[i+1],))
		results=cursor.fetchone();
		if(results[0] == "Train"):
			train = True
		elif(results[0] == "Bus + Train"):
			mix = True
		else:
			bus = True
	if(mix or(train and bus)):
		print("\n [*] Le trajet se fera par Bus et Train [*] \n")
	elif(train):
		print("\n [*] Le trajet se fera par Train [*] \n")
	else:
		print("\n [*] Le trajet se fera par Bus [*] \n")

 
if __name__ == "__main__":
	#Affichage du titre
	os.system('clear')
	print "  |---------------------------------------------------------------------|"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                        Utilitaire TER Métrolor                      |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |                                                                     |"
	print "  |---------------------------------------------------------------------|\n"

	print "\n Connection à la base de donnée ..."
	if(Connection()):
		while 1 :
			depart = raw_input("\n Saisir une gare de départ : ")
			arrivee = raw_input("\n Saisir une gare d'arrivée : ")
			print("\n Vous avez saisit :")
			print("\n Gare de départ --> "+str(depart))
			print("\n Gare d'arrivée --> "+str(arrivee))
			print("\n Appuyez sur ENTREE pour continuer... ")
			raw_input()
			os.system('clear')
			print "  |---------------------------------------------------------------------|"
			print "  |                  Test de l'existence des gares                      |"
			print "  |---------------------------------------------------------------------|\n"
			Existence(depart, arrivee)
			if(depart == arrivee):
				print("\n [*] Impossible ! Gare de départ "+str(depart)+" et Gare d'arrivée "+str(arrivee)+" similaire ! [*]")
				choix = raw_input("\n Réessayer ? [Oui/Non] : ")
				if(choix == "Oui"):
					os.system('clear')
				else:
					print("\n Fermeture ... \n")
					break
			else:
				connection = sqlite3.connect('Gares.db')
				connection.text_factory = str
				cursor=connection.cursor()
				g = {}
				adjac = {}
				d = []
				i = 0

				cursor.execute("""SELECT depart FROM gares""")
				for ville in cursor:
					if not ville in d:
						d.append(ville)

				while i != len(d):
					cursor.execute("""SELECT arrivee, temps FROM gares WHERE depart = ?""", (d[i]))
					tmp = d[i]
					tmp = str(tmp).replace("('", "")
					tmp = tmp.replace("',)", "")
					d[i] = tmp
					for arr in cursor:
						adjac[arr[0]] = arr[1]
					g[d[i]] = adjac
					i = i+1
					adjac = {}

				temps, trajet = dij_rec(g,depart,arrivee)

				trajetstr = trajet
				trajetstr = str(trajetstr).replace("['", "")
				trajetstr = trajetstr.replace("']", "")
				trajetstr = trajetstr.replace("'", "")
				trajetstr = trajetstr.replace(",", " -->")

				print "|---------------------------------------------------------------------|"
				print "|                  Trajet le plus rapide                              |"
				print "|---------------------------------------------------------------------|\n"
				if(temps > 60):
					print("\n Trajet le plus rapide : "+trajetstr+" qui durera "+strftime("%M heure(s) %S minute(s)", gmtime(temps))+"\n")
					Vehicule(trajet)
				else:
					print("\n Trajet le plus rapide : "+trajetstr+" qui durera "+str(temps)+" minute(s)")
					Vehicule(trajet)

				while 1:
					choix2 = raw_input("\n Rechercher un nouveau trajet ? [Oui/Non] : ")
					if(choix2 == "Oui"):
						os.system('clear')
						break
					elif(choix2 == "Non"):
						print("\n Vous allez quitter l'utilitaire ....")
						print("\n Fermeture \n")
						exit()
					else:
						print("\n Saisie incorrecte ! ")
	else:
		exit()