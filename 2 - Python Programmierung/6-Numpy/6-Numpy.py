#!/usr/bin/env python
# coding: utf-8
# Numpy
# numerische Berechnungen

# Pakete verwenden
# import numpy     # numpy.methode
import numpy as np # np.methode

my_array = np.array([1, 2, 3]) # Liste in Vektor Speichern

print(my_array)       # Array - Vektor: 1 - Dimensional
print(my_array.shape) # Länge

my_array2 = np.array([1, 0, 0, 1])

print(my_array2)       # Vektor: 1 - Dim.  [1 0 0 1]
print(my_array2.shape) # Länge: 4

# 2x2 Matrix aus Vektor erstellen. Achtung: Anzahl beachten!
my_array3 = my_array2.reshape((2, 2)) # Übergabe Tupel: (2, 2)

print(my_array3)       # [[1 0][0 1]]
print(my_array3.shape) # Länge: (2, 2)

my_zero = np.zeros(shape=(3, 3), dtype=np.float32) # 3x3 Matrix, float

print(my_zero) # float 0.

my_zero.astype(np.int8, copy=False) # 3x3 Matrix, int8 = 8 bit = 256

# Funktion anwenden
np.linalg.eig(my_array3) # Matrix übergeben

