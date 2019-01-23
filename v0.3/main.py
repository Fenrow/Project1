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
    '4. Dodano nową postać',
    '5. Opcje',
    '6. Wyjście',
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
            if int(user_choice) >= 1 and int(user_choice) <= len(possible_options):
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
        get_new_champion()
    elif user_choice == 4:
        os.system('CLS')
        new_champion()
    elif user_choice == 5:
        os.system('CLS')
        first_configuration()
    elif user_choice == 6:
        os.system('CLS')
        global exit
        exit = True

def new_sesson():
    """Funkcja resetująca zdobyte skrzynie na posiadanych postaciach"""

    global owned_champions, possible_chests, owned_chest

    for c in owned_chest:
        possible_chests.append(c)
        owned_chest.remove(c)

    save_to_file()

def show_possible_chest():
    """Funkcja pokazująca użytkownikowi możliwe do zdobycia skrzynie"""

    global possible_chests

    possible_chests.sort()

    if possible_chests:
        for possible_chest in possible_chests:

            print(possible_chest)
    else:
        print("Zdobyłeś już wszystkie skrzynie")

    answer1 = input('\nCzy chcesz wyjść? (T/N): ')
    if answer1.lower() == 't':
        global exit
        exit = True
    else:
        menu()

def get_chest():
    """Funkcja dodająca nowo zdobytą skrzynie"""

    new_chest = input('Wpisz nazwę postaci na której zdobyłeś skrzynię: ')

    global owned_champions, possible_chests, all_champions, owned_chest

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            if row[0] == new_chest.lower():
                if row[1] == '1':
                    possible_chests.remove(new_chest.lower())
                    owned_chest.append(new_chest.lower())
                else:
                    print('Nie posiadasz tej postaci')
            else:
                continue

    save_to_file()

def get_new_champion():
    """Funkcja dodająca postać do listy posiadanych postaci, tym samym dodająca
    ją do postaci na których można zdobyć skrzynię"""

    global owned_champions, possible_chests, all_champions

    get_name = False
    bad_data = False


    while get_name == False:
        if bad_data == True:
            print('\nNieprawidłowe dane!\n')
        new_champ = input('Wpisz nazwę postaci którą chcesz dodać do listy posiadanych: ')


        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                if row[0] == new_champ.lower():
                    if row[1] != '1':
                        owned_champions.append(new_champ.lower())
                        possible_chests.append(new_champ.lower())
                        get_name = True
                        bad_data = False
                    else:
                        bad_data = True
                else:
                    bad_data = True

    save_to_file()

def new_champion():
    """Funkcja dodająca nową postać do list 'all_champions'"""
    get_name = False
    bad_data = False

    while get_name == False:

        if bad_data == True:
            print('\nNieprawidłowe dane!\n')
        new_champ = input('Wpisz nazwę postaci którą chcesz dodać do listy wszystkich postaci: ')
        new_champ_apr = input('Wpisz nazwę jeszcze raz: ')

        if new_champ.lower() == new_champ_apr.lower():
            all_champions.append(new_champ_apr)
            save_to_file()
            get_name = True
        else:
            bad_data = True

def first_configuration():
    """Funkcja wywoływana podczas pierwszej konfiguracji danego urzytkownika"""

    global all_champions, owned_champions, possible_chests, owned_chest

    possible_options = [
    '1. Pierwsze uruchomienie',
    '2. Nowy sezon',
    '3. Powrót',
    ]
    good_choice = False

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
            if int(user_choice) >= 1 and int(user_choice) <= len(possible_options):
                good_choice = True
            else:
                print('Nie istnieje opcja o tym numerze')

    if user_choice == 1:
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

        save_to_file()

    elif user_choice == 2:
        new_sesson()

    elif user_choice == 3:
        menu()

def save_to_file():
    """Funkcja odpowiadająca za zapis danych do pliku csv"""

    global all_champions, owned_champions, possible_chests, owned_chest

    with open(filename, 'w', newline='') as f:
        header = ['Champion name','Owned','Possible chest']
        writer = csv.writer(f)
        writer.writerow(header)

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
        menu()
    else:
        break
