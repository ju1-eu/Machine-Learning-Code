![Machine Learning](attachment:MachineLearning-5.png)

# Machine Learning 

mit Python inkl. AI Einführung

Quelle: Jan Schaffranek (Udemy)

## Was ist Python, Anaconda und Jupyter Notebook?

Python:

- höhere Programmiersprache
- gut lesbar u. knapper Code-Style
- Erscheinungsjahr 1991
- Hauptentwickler Guido van Rossum

Anaconda:

- Python Distribution
- Einfache Erstellung von Python u. Tensorflow

Jupyter Notebook:

- Interaktives Scripting Tool
- Einbindung von Markdown
- Darstellung als Website
- gute Visualisierungen

Visual Studio Code:

- IDE
- Updates
- Addons, Git, Einfache konfig.

## Installation

Download Anaconda: https://www.anaconda.com/downloads   
Download Visual Studio Code: https://code.visualstudio.com/

Installation von Anaconda prüfen

    Win10 / cmd / 
    C:\Users\jan> activate base
    (base) C:\Users\jan>
        # Befehle
        python
        conda list
        # Programm nachinstallieren
        pip install markdown

## Git

### Repository - Machine-Learning-Notiz

    cd notiz
    # anlegen
    git remote add origin https://github.com/ju1-eu/Machine-Learning-Notiz.git
    git push -u origin master
    # clone
    git clone https://github.com/ju1-eu/Machine-Learning-Notiz.git notiz

### Repository - Machine-Learning-Code

    cd prj/Machine-Learning-Code
    # anlegen
    git remote add origin https://github.com/ju1-eu/Machine-Learning-Code.git
    git push -u origin master
    # clone
    git clone https://github.com/ju1-eu/Machine-Learning-Code.git

### git init 

    echo "# Machine Learning" >> README.md
    git init
    git add README.md
    git commit -m "start"

### git commit

    git add .
    git commit -a

### git status - git log

    git st
    git lg

### github - git push

    git pull
    git push

## Jupiter Notebook

Jupyter Notebook aus dem Kontextmenü des Dateimanagers starten, 
ansonsten nur vom Download o. Desktop Ordner!

https://github.com/hyperspy/start_jupyter_cm

    # Win10 / cmd / (Admin)
    # install
    pip install start_jupyter_cm
    
    # After installation, enable the context menu 
    start_jupyter_cm
    
    # Dateimanager öffnen
    re. Mausklick / Jupyter Notebook here

Absturz

    Browser:
    Jupiter Notebook / Kernel / Restart & Clear Output

Zellen:

- Aktive Zelle = Grün
- Passive Zelle = Blau

Passive Zelle wählen:

- a = Zelle oberhalb einfügen
- b = Zelle unterhalb einfügen


```python
print("Hallo Welt!") # Strg + Enter  = Code ausführen
```

### Python - Links 

- Aussagenlogik: https://de.wikipedia.org/wiki/Aussagenlogik
- Python Dokumentation: https://docs.python.org/3/
- Python Listen: https://developers.google.com/edu/python/lists
- Python Dicts: https://developers.google.com/edu/python/dict-files
- Python List Comprehensions: https://de.wikipedia.org/wiki/List_Comprehension
- Python Funktionen: https://www.tutorialspoint.com/python/python_functions.htm
- Python Klassen: https://www.learnpython.org/en/Classes_and_Objects
- Python Numpy Dokumentation: https://docs.scipy.org/doc/numpy-1.13.0/reference/
- Numpy Einleitung: http://cs231n.github.io/python-numpy-tutorial/
- Python Matplotlib Dokumentation: https://matplotlib.org/contents.html
- Matplotlib Einleitung: https://matplotlib.org/tutorials/index.html
