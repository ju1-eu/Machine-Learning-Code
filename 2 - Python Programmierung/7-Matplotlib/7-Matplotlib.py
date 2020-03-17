#!/usr/bin/env python
# coding: utf-8
# Matplotlib
# Daten visualisieren

# ohne Pop-up Fenster in Jupyter Notebook
# %matplotlib inline 
import matplotlib.pyplot as plt
import numpy as np

# x-y Werte
x = np.array([1, 2, 3, 4])
y = np.array([8, 10, 22, 51])

# Plotten
plt.plot(x, y, color="red")# Punkte Verbinden
plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")
# Speichern als PNG-Datei:
plt.savefig('Diagramm_1.png')
# Speichern als SVG-Datei:
plt.savefig('Diagramm_1.svg')
#plt.show()

plt.scatter(x, y) # Punkte anlegen, nicht Verbinden
# Speichern als PNG-Datei:
plt.savefig('Diagramm_2.png')
# Speichern als SVG-Datei:
plt.savefig('Diagramm_2.svg')
#plt.show()


import random # Zufallswerte

x = [i for i in range(100)] # x-Werte von 0 - 99 generieren
y = [random.randint(0, 10) for i in range(100)]# y-Werte Zufallszahlen 100x generieren

plt.scatter(x, y) # Punkte anlegen
# Speichern als PNG-Datei:
plt.savefig('Diagramm_3.png')
# Speichern als SVG-Datei:
plt.savefig('Diagramm_3.svg')
#plt.show()

# Titel, Legende und Text hinzufügen
# grund-wissen.de/informatik/python/scipy/matplotlib.html

# x-y Werte
x = [i for i in range(11)]
y = [i for i in range(11)]

y1 = [a**2 for a in range(11)]

# Eine neues Matplot-Figure-Objekt mit 8x6 Zoll und
# einer Auflösung von 100 dpi erstellen:
# Länge mit 2,54 cm multiplizieren
plt.figure(figsize=(8, 6), dpi=80)

# Titel hinzufügen:
plt.title('Titel', fontsize=20, color='gray')

# Plotten
plt.plot(x, y, color="blue")# Punkte Verbinden
plt.plot(x, y1, color="red")# Punkte Verbinden

plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")

# Speichern als PNG-Datei:
plt.savefig('Diagramm_4.png')
# Speichern als SVG-Datei:
plt.savefig('Diagramm_4.svg')
#plt.show()

input() # Pause