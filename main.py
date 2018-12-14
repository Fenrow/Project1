"""Program który ułatwia sprawdzenie na jakiej postaci można jeszcze
zdobyć skrzynię hextech"""

import json

fname_template = 'template_champ.txt'
fname_config = 'config.json'

owned_champs = []

def firstlaunch(file_name):
    """Funkcja używana podczas pierwszego uruchomienia do stworzenia
    listy posiadanych postaci"""

    try:
        with open(file_name) as ftemplate:
            for line in ftemplate:
                champion = ftemplate.readline()
                answer1 = input('Czy posiadasz postać ' + champion.strip() + '?(T/N)')
                if answer1.lower() == 't':
                    champion = champion.strip()
                    owned_champs.append(champion)
    except FileNotFoundError:
        print('plik ' + file_name + ' nie znajduje się w tym samym katalogu')

    with open(fname_config, 'w') as fcon:
        json.dump(owned_champs, fcon)

def read_champs(file_name):
    """Funkcja pokazująca dostępne postaci"""
    with open(file_name) as fconfig:
        owned_champs = json.load(fconfig)
        print(owned_champs)

try:
    read_champs(fname_config)
except FileNotFoundError:
    firstlaunch(fname_template)
