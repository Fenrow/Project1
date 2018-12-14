"""Program który ułatwia sprawdzenie na jakiej postaci można jeszcze
zdobyć skrzynię hextech"""

import json

fname_template = 'template_champ.txt'
fname_config = 'OChamp.json'
fname_poschamp = 'PChamp.json'

owned_champs = []       #posiadane postacie
possible_chests = []     #postacie na ktorych mozna zdobyc skrzynie

def firstlaunch(file_name):
    """Funkcja używana podczas pierwszego uruchomienia do stworzenia
    listy posiadanych postaci (file_name 'fname_template.txt')"""

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


def check_champs(file_name):
    """Funkcja pokazująca dostępne postaci (file_name 'OChamp.json')"""
    with open(file_name) as fconfig:
        owned_champs = json.load(fconfig)

    for champ in owned_champs:
        answer2 = input('Czy mozesz zdobyć skrzynię na ' + champ + '?(T/N)')
        if answer2.lower() == 't':
            possible_chests.append(champ)

    if possible_chests:
        with open(fname_poschamp, 'w') as fpchamp:
            json.dump(possible_chests, fpchamp)
        for chest in possible_chests:
            print('\n\nMozesz zdobyć skrzynie na ' + chest)
    else:
        print('\nZosbyłeś skrzynie na wszystkich posiadanych postaciach')

try:
    check_champs(fname_config)
except FileNotFoundError:
    firstlaunch(fname_template)
