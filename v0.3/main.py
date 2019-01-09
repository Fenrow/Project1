"""Program który ułatwia sprawdzenie na jakiej postaci można jeszcze
zdobyć skrzynię hextech. Zapisuje ona do pliku csv listę postaci oraz to czy
jest możliwość zdobyć na tej postaci skrzynię w formacie

|Nazwa postaci|Posiadana|Skrzynia| odpowiednio nazwa,0/1,0/1
np. Aatrox,1,1 oznacza że urzytkownik posiada postać 'Aatrox' oraz może zdobyć
na tej postaci skrzynie
"""

import csv
import os

all_champions = [
'aatrox','ahri','akali','alistar','amumu','anivia','annie','ashe','aurelion sol'
,'azir','bard','blitzcrank','brand','braum','caitlyn','camille','cassiopeia',
"cho'Gath",'corki','darius','diana','dr mundo','draven','ekko','elise','evelynn'
,'ezreal','fiddlesticks','fiora','fizz','galio','gangplank','garen','gnar',
'gragas','graves','hecarim','heimerdinger','illaoi','irelia','ivern','janna',
'jarvan IV','jax','jayce','jhin','jinx',"kai'Sa",'kalista','karma','karthus',
'kassadin','katarina','kayle','kayn','kennen',"kha'Zix",'kindred','kled',
"kog'Maw",'leBlanc','lee sin','leona','lissandra','lucian','lulu','lux',
'malphite','malzahar','maokai','master yi','miss fortune','mordekaiser',
'morgana','nami','nasus','nautilus','neeko','nidalee','nocturne','nunu i willump',
'olaf','orianna','ornn','pantheon','poppy','pyke','quinn','rakan','rammus',
"rek'Sai",'renekton','rengar','riven','rumble','ryze','sejuani','shaco','shen',
'shyvana','singed','sion','sivir','skarner','sona','soraka','swain','syndra',
'tahm kench','taliyah','talon','taric','teemo','thresh','tristana','trundle',
'tryndamere','twisted fate','twitch','udyr','urgot','varus','vayne','veigar',
"vel'Koz",'vi','viktor','vladimir','volibear','warwick','wukong','xayah',
'xerath','xin zhao','yasuo','yoric','zac','zed','ziggs','zilean','zoe','zyra'
]

owned_champions = []
possible_chests = []
owned_chest = []

filename = 'Champion.csv'
exit = False
fnfe = False #File not found error

def data_preparation():
    """Funkcja odpowiedzialna za przygotowanie danych z pliku csv"""
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            global owned_champions, possible_chests, owned_chest

            for row in reader:
                if row[1] == '1':
                    owned_champions.append(row[0])
                if row[2] == '1':
                    possible_chests.append(row[0])
                else:
                    if row[1] == '1':
                        owned_chest.append(row[0])

    except FileNotFoundError:
        with open(filename, 'a', newline='') as f:
            header = ['Champion name','Owned','Possible chest']
            writer = csv.writer(f)
            writer.writerow(header)

def menu():
    """Funkcja odpowiedzialna za przygotowanie menu dla użytkownika"""

    good_choice = False

    possible_options = [
    '1. Wyświetl możliwe do zdobycia skrzynie',
    '2. Zdobyłem skrzynie',
    '3. Kupiłem nową postać ',
    '4. Pierwsza konfiguracja',
    '5. Wyjście',
    ]

    os.system('CLS')
    print('\nMENU:')
    for possible_option in possible_options:
        print(possible_option)

    while good_choice == False:
        try:
            user_choice = int(input('\nWpisz numer opcji: '))
        except ValueError:
            print('To nie jest liczba')
            continue
        else:
            if user_choice >= 1 and user_choice <= len(possible_options):
                good_choice = True
            else:
                print('Nie istnieje opcja o tym numerze')

    if user_choice == 1:
        os.system('CLS')
        show_possible_chest()
    elif user_choice == 2:
        os.system('CLS')
        get_chest()
    elif user_choice == 3:
        os.system('CLS')
        new_champion()
    elif user_choice == 4:
        os.system('CLS')
        first_configuration()
    elif user_choice == 5:
        os.system('CLS')
        global exit
        exit = True
        return exit

def show_possible_chest():
    """Funkcja pokazująca użytkownikowi możliwe do zdobycia skrzynie"""
    pass

def get_chest():
    """Funkcja dodająca nowo zdobytą skrzynie"""
    pass

def new_champion():
    """Funkcja dodająca postać do listy posiadanych postaci"""
    pass

def first_configuration():
    """Funkcja wywoływana podczas pierwszej konfiguracji danego urzytkownika
    oraz zapisanie danych do pliku csv"""

    for champion in all_champions:
        answer1 = input('Czy posiadasz bohatera ' + champion.title() + ' (T/N)?: ')
        if answer1.lower() == 't':
            owned_champions.append(champion)

    for champion in owned_champions:
        answer2 = input('Czy możesz zdobyć skrzynię na ' + champion.title() + ' (T/N)?: ')
        if answer2.lower() == 't':
            possible_chests.append(champion)
        else:
            owned_chest.append(champion)



    for champion in all_champions:
        lines_to_csv = []
        lines_to_csv.append(champion.lower())
        if champion in owned_champions:
            lines_to_csv.append('1')
        else:
            lines_to_csv.append('0')
        if champion in possible_chests:
            lines_to_csv.append('1')
        else:
            lines_to_csv.append('0')

        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(lines_to_csv)

data_preparation()
while True:
    if exit == False:
        print('Posiadane', owned_champions)
        print('Możliwe', possible_chests)
        print('Zdobyte', owned_chest)
        menu()
    else:
        break
