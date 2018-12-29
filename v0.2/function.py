import json

def new_user(all_champions, owned_champions, possible_chests, owned_chest):
    """funkcja inicjalizujaca nowego urzytkownika/nowy profil"""

    for champion in all_champions:
        answer1 = input('Czy posiadasz bohatera ' + champion.title() + '?(T/N)')
        if answer1.lower() == 't':
            owned_champions.append(champion)

    for champion in owned_champions:
        answer2 = input('Czy możesz zdobyć skrzynię na ' + champion.title() + '?(T/N)')
        if answer2.lower() == 't':
            possible_chests.append(champion)
        else:
            owned_chest.append(champion)

def save_data(all_champions, owned_champions, possible_chests, owned_chest, fname_owned_champ, fname_owned_chest, fname_possible_champ):
    """funkcja zapisująca dane do plików"""

    with open(fname_owned_champ, 'w') as f_ownch:
        json.dump(owned_champions, f_ownch)
    with open(fname_possible_champ, 'w') as f_posch:
        json.dump(possible_chests, f_posch)
    with open(fname_owned_chest, 'w') as f_ownche:
        json.dump(owned_chest, f_ownche)
