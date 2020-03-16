# Listen - Dictionary

    Liste: []
    Dicts: {key: val}

## Listen

```python
# Listen
my_list = [1, 2, 3, 1.5, True, "Jan"] # verschiedene Datentypen
print(my_list) # Ausgabe: [1, 2, 3, 1.5, True, 'Jan']
len(my_list)   # Länge: 6
```

```python
# Listen Funktionen
my_list = [1, 2, 3]

my_list.append(12)# Element hinzufügen

# 1, 2, 3, 12
print(my_list)    # Ausgabe: [1, 2, 3, 12]

1, 2, 3
my_list.pop()     # Element löschen

print(my_list)    # Ausgabe: [1, 2, 3]
```

```python
my_list = [12, 32, 30]

# auf Listenelemente zugreifen
print(my_list[0]) # Ausgabe: 12
print(my_list[1]) # Ausgabe: 32
print(my_list[2]) # Ausgabe: 30
```  

## Dictionary


```python
# Dictionary

# key, values
# "Peter": [34, "Fußball", "Berlin"]

my_dict = {"Peter": [34, "Fußball", "Berlin"],
          "Dennis": [31, "Handball", "Berlin"],}

print(my_dict) 
# Ausgabe: {'Peter': [34, 'Fußball', 'Berlin'], 
						'Dennis': [31, 'Handball', 'Berlin']}
```

```python
# Dictionary Funktionen

my_dict = {"Peter": [34, "Fußball", "Berlin"],
          "Dennis": [31, "Handball", "Berlin"],
          1:  12}

my_dict.pop("Dennis") # löschen
print(my_dict) 
# Ausgabe: {'Peter': [34, 'Fußball', 'Berlin'], 1: 12}

my_dict.update({"Dennis": [31, "Handball", "Berlin"]}) # hinzufügen
my_dict["Karl"] = [31, "Handball", "Berlin"]           # hinzufügen

my_dict["Karl"] = [31, "Handball", "Potsdam"]          # überschreiben      
print(my_dict) 
# Ausgabe: {'Peter': [34, 'Fußball', 'Berlin'], 1: 12, 
						'Dennis': [31, 'Handball', 'Berlin'], 
						'Karl': [31, 'Handball', 'Potsdam']}
```