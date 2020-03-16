#!/usr/bin/env python
# coding: utf-8
# Funktionen - Klassen

# Funktionen
# Maximum der Liste bestimmen
def list_max(my_list):
    temp = 0
    
    for i in range(len(my_list)): # listenlänge
        if i == 0:                # index = 0
            temp = my_list[i]     # akt. Max-Wert
        else:
            if my_list[i] > temp:
                print("Last max: ", temp)
                print("New max: ", my_list[i])
                temp = my_list[i] # gefundenes Maximum 
                
    return temp

# Funktionsaufruf

# Liste
list_a = [1, 12, -5, -23, 19]

# Aufruf
list_max(list_a) # Maximum der Liste bestimmen

# Klassen
# Klasse: Bauplan
# Objekt: Eine Instanz der Klasse XYZ

# Klassen
# Maximum der Liste bestimmen
class extended_list:  # Klassenname
    # Membervariable erstellen
    m_list = [] # liste
    m_size = 0  # länge
    m_max = 0   # Max
    
    # Konstruktor: __init__    Wichtig: self => übergeben
    def __init__(self, input_list):
        # in Membervariable speichern
        self.m_list = input_list       # Liste übergeben
        self.m_size = len(self.m_list) # länge
    
    # Maximum der liste
    def list_max(self):
        temp = 0
        for i in range(len(self.m_list)):
            if i == 0:
                temp = self.m_list[i]
            else:
                if self.m_list[i] > temp:
                    temp = self.m_list[i]
        # in Membervariable speichern          
        self.m_max = temp # gefundenes Maximum 
    
    def print_max(self):
        print("Maximum is: ", self.m_max)

# Objekt von der Klasse erstellen

# Liste
input_list = [1, 50, 44, -2]

# Objekt
el = extended_list(input_list)
el.list_max()  # Maximum der Liste bestimmen
el.print_max() # Ausgabe

input() # Pause