#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os

if os.path.isfile("Gares.db"):
    os.remove("Gares.db")

conn = sqlite3.connect("Gares.db")
conn.text_factory = str


cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS gares( 
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	depart TEXT,
    arrivee TEXT,
    temps INTEGER,
    vehicule TEXT
)
""")
conn.commit()

tchou = [
("Nancy", "Toul", "25", "Train"),
("Toul", "Nancy", "25", "Train"),
("Commercy", "Bar-le-Duc", "19", "Train"),
("Bar-le-Duc", "Commercy", "19", "Train"),
("Forbach", "Bening", "6", "Train"),
("Bening", "Forbach", "6", "Train"),
("Epinal", "Bruyeres", "31", "Train"),
("Bruyeres", "Epinal", "31", "Train"),
("Hagondange", "Conflans-Jarny", "31", "Train"),
("Conflans-Jarny", "Hagondange", "31", "Train"),
("Longuyon", "Conflans-Jarny", "35", "Train"),
("Conflans-Jarny", "Longuyon", "35", "Train"),
("Longwy", "Longuyon", "12", "Train"),
("Longuyon", "Longwy", "12", "Train"),
("Luxembourg", "Longwy", "32", "Train"),
("Longwy", "Luxembourg", "32", "Train"),
("Merrey", "Contrexeville", "26", "Train"),
("Contrexeville", "Merrey", "26", "Train"),
("Metz", "Hagondange", "12", "Train"),
("Hagondange", "Metz", "12", "Train"),
("Mirecourt", "Contrexeville", "19", "Train"),
("Contrexeville", "Mirecourt", "19", "Train"),
("Mirecourt", "Epinal", "42", "Bus"),
("Epinal", "Mirecourt", "42", "Bus"),
("Montmedy", "Longuyon", "14", "Train"),
("Longuyon", "Montmedy", "14", "Train"),
("Nancy", "Epinal", "53", "Train"),
("Epinal", "Nancy", "53", "Train"),
("Nancy", "Luneville", "25", "Train"),
("Luneville", "Nancy", "25", "Train"),
("Nancy", "Mirecourt", "60", "Train"),
("Mirecourt", "Nancy", "60", "Train"),
("Neufchateau", "Mirecourt", "41", "Bus"),
("Mirecourt", "Neufchateau", "41", "Bus"),
("Onville", "Bar-le-Duc", "100", "Bus"),
("Bar-le-Duc", "Onville", "100", "Bus"),
("Onville", "Conflans-Jarny", "22", "Train"),
("Conflans-Jarny", "Onville", "22", "Train"),
("Onville", "Metz", "14", "Train"),
("Metz", "Onville", "14", "Train"),
("Pagny-sur-Moselle", "Metz", "13", "Train"),
("Metz", "Pagny-sur-Moselle", "13", "Train"),
("Pagny-sur-Moselle", "Onville", "13", "Train"),
("Onville", "Pagny-sur-Moselle", "13", "Train"),
("Paris", "Chalon-en-Champagne", "95", "Train"),
("Chalon-en-Champagne", "Paris", "95", "Train"),
("Pont-a-Mousson", "Nancy", "15", "Train"),
("Nancy", "Pont-a-Mousson", "15", "Train"),
("Pont-a-Mousson", "Pagny-sur-Moselle", "8", "Train"),
("Pagny-sur-Moselle", "Pont-a-Mousson", "8", "Train"),
("Reding", "Morhange", "22", "Train"),
("Morhange", "Reding", "22", "Train"),
("Remilly", "Metz", "14", "Train"),
("Metz", "Remilly", "14", "Train"),
("La Bresse", "Remiremont", "54", "Bus"),
("Remiremont", "La Bresse", "54", "Bus"),
("Remiremont", "Bussang", "55", "Bus"),
("Bussang", "Remiremont", "55", "Bus"),
("Remilly", "Morhange", "15", "Train"),
("Morhange", "Remilly", "15", "Train"),
("Remiremont", "Epinal", "30", "Train"),
("Epinal", "Remiremont", "30", "Train"),
("Revigny", "Bar-le-Duc", "10", "Train"),
("Bar-le-Duc", "Revigny", "10", "Train"),
("Revigny", "Chalon-en-Champagne", "37", "Train"),
("Chalon-en-Champagne", "Revigny", "37", "Train"),
("Saarbrucken", "Forbach", "10", "Train"),
("Forbach", "Saarbrucken", "10", "Train"),
("Saint-Die", "Bruyeres", "29", "Train"),
("Bruyeres", "Saint-Die", "29", "Train"),
("Saint-Die", "Luneville", "50", "Train"),
("Luneville", "Saint-Die", "50", "Train"),
("Saint-Die", "Saales", "25", "Train"),
("Saales", "Saint-Die", "25", "Train"),
("Sarrebourg", "Luneville", "22", "Train"),
("Luneville", "Sarrebourg", "22", "Train"),
("Sarrebourg", "Morhange", "29", "Train"),
("Morhange", "Sarrebourg", "29", "Train"),
("Sarrebourg", "Reding", "3", "Train"),
("Reding", "Sarrebourg", "3", "Train"),
("Sarreguemines", "Bening", "20", "Train"),
("Bening", "Sarreguemines", "20", "Train"),
("Sarreguemines", "Saarbrucken", "20", "Train"),
("Saarbrucken", "Sarreguemines", "20", "Train"),
("Sarreguemines", "Sarrebourg", "130", "Bus + Train"),
("Sarrebourg", "Sarreguemines", "130", "Bus + Train"),
("Saverne", "Reding", "13", "Train"),
("Reding", "Saverne", "13", "Train"),
("Selestat", "Saint-Die", "70", "Bus"),
("Saint-Die", "Selestat", "70", "Bus"),
("Saint-Avold", "Bening", "9", "Train"),
("Bening", "Saint-Avold", "9", "Train"),
("Saint-Avold", "Remilly", "19", "Train"),
("Remilly", "Saint-Avold", "19", "Train"),
("Strasbourg", "Saales", "70", "Train"),
("Saales", "Strasbourg", "70", "Train"),
("Strasbourg", "Sarreguemines", "76", "Train"),
("Sarreguemines", "Strasbourg", "76", "Train"),
("Strasbourg", "Saverne", "36", "Train"),
("Saverne", "Strasbourg", "36", "Train"),
("Strasbourg", "Selestat", "28", "Train"),
("Selestat", "Strasbourg", "28", "Train"),
("Thionville", "Apach", "33", "Train"),
("Apach", "Thionville", "33", "Train"),
("Thionville", "Hagondange", "10", "Train"),
("Hagondange", "Thionville", "10", "Train"),
("Thionville", "Longuyon", "38", "Train"),
("Longuyon", "Thionville", "38", "Train"),
("Thionville", "Luxembourg", "25", "Train"),
("Luxembourg", "Thionville", "25", "Train"),
("Toul", "Neufchateau", "24", "Train"),
("Neufchateau", "Toul", "24", "Train"),
("Verdun", "Conflans-Jarny", "36", "Train"),
("Conflans-Jarny", "Verdun", "36", "Train"),
("Vittel", "Contrexeville", "4", "Train"),
("Commercy", "Toul", "12", "Train"),
("Toul", "Commercy", "12", "Train"),
("Contrexeville", "Vittel", "4", "Train"),
("Mirecourt", "Vittel", "19", "Train"),
("Vittel", "Mirecourt", "19", "Train"),
("Bruyeres", "Luneville", "55", "Bus"),
("Luneville", "Bruyeres", "55", "Bus")
]

cursor.executemany("""INSERT INTO gares(depart, arrivee, temps, vehicule) VALUES(?, ?, ?, ?)""", tchou)
conn.commit()
conn.close()