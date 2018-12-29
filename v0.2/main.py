"""Program który ułatwia sprawdzenie na jakiej postaci można jeszcze
zdobyć skrzynię hextech"""

import json

import function as f

all_champions = [
'aatrox','ahri','akali','alistar','amumu','anivia','annie','ashe','aurelion sol'
,'azir','bard','blitzcrank','brand','braum','caitlyn','camille','cassiopeia',
"cho'Gath",'corki','darius','diana','dr mundo','draven','ekko','elise','evelynn'
,'ezreal','fiddlesticks','fiora','fizz','galio','gangplank','garen','gnar',
'gragas','graves','hecarim','heimerdinger','illaoi','irelia','ivern','janna',
'jarvan IV','jax','jayce','jinx','jhin',"kai'Sa",'kalista','karma','karthus','kassadin'
,'katarina','kayle','kayn','kennen',"kha'Zix",'kindred','kled',"kog'Maw",
'leBlanc','lee sin','leona','lissandra','lucian','lulu','lux','malphite',
'malzahar','maokai','master yi','miss fortune','mordekaiser','morgana','nami',
'nasus','nautilus','neeko','nidalee','nocturne','nunu i willump','olaf',
'orianna','ornn','pantheon','poppy','pyke','quinn','rakan','rammus',"rek'Sai",
'renekton','rengar','riven','rumble','ryze','sejuani','shaco','shen','shyvana',
'singed','sion','sivir','skarner','sona','soraka','swain','syndra','tahm kench',
'taliyah','talon','taric','teemo','thresh','tristana','trundle','tryndamere',
'twisted fate','twitch','udyr','urgot','varus','vayne','veigar',"vel'Koz",'vi',
'viktor','vladimir','volibear','warwick','wukong','xayah','xerath','xin zhao',
'yasuo','yoric','zac','zed','ziggs','zilean','zoe','zyra'
]
owned_champions = []
possible_chests = []
owned_chest = []

fname_owned_champ = 'owned_champ.json' #posiadane postacie
fname_possible_champ = 'poss_champ.json' #postacie na ktorych mozna zdobyc skrzynie
fname_owned_chest = 'owned_chest.json' #postacie na ktorych posiada sie skrzynie

try:
    with open(fname_owned_champ) as f_ownch:
        owned_champions = json.load(f_ownch)
except FileNotFoundError:
    print('Plik ' + fname_owned_champ + ' nie istnieje')
    load_data_1 = False
else:
    load_data_1 = True

try:
    with open(fname_possible_champ) as f_posch:
        possible_chests = json.load(f_posch)
except FileNotFoundError:
    print('Plik ' + fname_possible_champ + 'nie istnieje')
    load_data_2 = False
else:
    load_data_2 = True

try:
    with open(fname_owned_chest) as f_ownche:
        owned_chest = json.load(f_ownche)
except FileNotFoundError:
    print('Plik ' + fname_owned_chest + ' nie istnieje')
    load_data_3 = False
else:
    load_data_3 = True

if load_data_1 == True and load_data_2 == True and load_data_3 == True:
    load_data_OK = True
else:
    load_data_OK = False

if load_data_OK == True:
    print('\n')
    print('Możesz zdobyć skrzynie na następujących bohaterach:\n')
    for possible in possible_chests:
        print(possible.title())
else:
    f.new_user(all_champions, owned_champions, possible_chests, owned_chest)

f.save_data(all_champions, owned_champions, possible_chests, owned_chest, fname_owned_champ, fname_owned_chest, fname_possible_champ)
