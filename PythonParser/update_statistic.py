import time
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient
from datetime import datetime
import threading
import os
from methods import save_to_pickle_file, read_pickle_file
from classes.parse_manager import ParseManager


PARSE_MANAGER = ParseManager()


def update_heroes_list(patch_number, date):
    print("start update_heroes_list")
    url = 'https://www.dotabuff.com/heroes'
    first = datetime.now()
    soup = PARSE_MANAGER.parse(url, date)
    print(datetime.now() - first, "update_heroes_list")
    heroes_list_html = soup.findAll('div', class_='name')

    heroes_list = []
    for hero in heroes_list_html:
        heroes_list.append(hero.text)
    save_to_pickle_file(f'statistic/{patch_number}/heroes_list', heroes_list)


def update_heroes_win_rates(patch_number, date):
    print("start update_heroes_win_rates")
    heroes_list = read_pickle_file(f'statistic/{patch_number}/heroes_list')
    heroes_win_rate_dict = {}
    count = 0
    first = datetime.now()
    for hero in heroes_list:
        hero = "Sven"
        count += 1
        print(hero)
        _hero = hero
        if hero == "Nature's Prophet":
            hero = 'natures-prophet'
        url = f'https://www.dotabuff.com/heroes/{hero.replace(" ", "-").lower()}'
        soup = PARSE_MANAGER.parse(url, date)
        print(soup)
        hero = _hero
        if len(soup.findAll('span', class_='won')) == 0:
            print(soup.findAll('span', class_='lost'))
            hero_winrate = soup.findAll('span', class_='lost')[0].text[:-1]
        else:
            print(soup.findAll('span', class_='won'))
            hero_winrate = soup.findAll('span', class_='won')[0].text[:-1]
        heroes_win_rate_dict[hero] = hero_winrate
    print(datetime.now() - first)
    print(heroes_win_rate_dict)
    save_to_pickle_file(f'statistic/{patch_number}/heroes_win_rate_dict', heroes_win_rate_dict)


def update_counters():
    print("start update_counters")
    heroes_list = read_pickle_file('statistic/heroes_list')
    heroes_counters_dict = {}
    for hero in heroes_list:
        heroes_counters_dict[hero] = {}
    first = datetime.now()
    for hero in heroes_list:
        print(hero)
        _hero = hero
        if hero == "Nature's Prophet":
            hero = 'natures-prophet'
        url = f'https://www.dotabuff.com/heroes/{hero.replace(" ", "-").lower()}/counters'
        soup = PARSE_MANAGER.parse(url, str(datetime.now().date()).replace('-', ''))
        hero = _hero
        heroes_names = soup.findAll('a', class_='link-type-hero')

        data = soup.findAll('td')
        counters = []
        for d in data:
            if "data-value" in str(d):
                digit = str(d)[str(d).find("data-value") + 12:str(d).find("data-value") + 16]
                if digit.replace('.', '').replace('-','').isdigit():
                    digit = float(digit)
                    if -10 <= digit <= 10:
                        counters.append(digit)
        print(len(counters))
        if len(counters) < 120:
            continue
        for i, hero_name in enumerate(heroes_names):
            second_hero = hero_name.text
            if second_hero == "Outworld Devourer":
                second_hero = 'Outworld Destroyer'
            heroes_counters_dict[hero][second_hero] = counters[i]
            heroes_counters_dict[second_hero][hero] = -counters[i]

    print(datetime.now() - first, "heroes_counters_dict")
    save_to_pickle_file(f'statistic/heroes_counters_dict', heroes_counters_dict)


def find_pro_players(patch_number, date):
    print("start find_pro_players")
    pro_players_list = []
    pro_players_id_dict = {}
    pro_players_win_rate_dict = {}
    first = datetime.now()
    url = f'https://www.dotabuff.com/players'
    soup = PARSE_MANAGER.parse(url, date)
    all_players = soup.findAll('a', class_='link-type-player')
    for player in all_players:
        index = -1
        if '.' in player.text:
            index = player.text.find('.')
        index_id = len('/players/')
        pro_players_list.append(player.text[index + 1:])
        pro_players_id_dict[player.text[index + 1:]] = player['href'][index_id:]
    all_tds = soup.findAll('td', class_='r-none-mobile')
    for i in range(0, len(pro_players_list)):
        pro_players_win_rate_dict[pro_players_list[i]] = all_tds[i * 3]['data-value']
    print(datetime.now() - first, "pro_players")
    save_to_pickle_file(f'statistic/{patch_number}/pro_players_win_rate_dict', pro_players_win_rate_dict)
    save_to_pickle_file(f'statistic/{patch_number}/pro_players_list', pro_players_list)
    save_to_pickle_file(f'statistic/{patch_number}/pro_players_id_dict', pro_players_id_dict)

'''
from zenrows import ZenRowsClient
CLIENT_API = '55b20866e1939d82af622565306a8b05c55138bd'
PARAMS = {"js_render":"true","antibot":"true"}
client = ZenRowsClient(CLIENT_API)
params = PARAMS
def find_pro_players():
    pro_players_list = []
    pro_players_id_dict = {}
    pro_players_win_rate_dict = {}
    url = f'https://www.dotabuff.com/players'
    response = client.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    all_players = soup.findAll('a', class_='link-type-player')
    for player in all_players:
        index = -1
        if '.' in player.text:
            index = player.text.find('.')
        index_id = len('/players/')
        pro_players_list.append(player.text[index+1:])
        pro_players_id_dict[player.text[index+1:]] = player['href'][index_id:]
    all_tds = soup.findAll('td', class_='r-none-mobile')
    for i in range(0, len(pro_players_list)):
        pro_players_win_rate_dict[pro_players_list[i]] = all_tds[i * 3]['data-value']

    save_to_pickle_file('statistic/pro_players_win_rate_dict', pro_players_win_rate_dict)
    save_to_pickle_file('statistic/pro_players_list', pro_players_list)
    save_to_pickle_file('statistic/pro_players_id_dict', pro_players_id_dict)
'''

def find_patch_date():
    patches_date_dict = {'20240221': '7.35c', '20231221': '7.35b', '20231214': '7.35', '20231120': '7.34e'}
    date_patches_dict = {'7.35c': '20240221', '7.35b': '20231221', '7.35': '20231214', '7.34e': '20231120'}
    patches_list = ['7.35c', '7.35b', '7.35', '7.34e']
    p = ['']
    for year in range(2021, 2010, -1):
        p.append('/' + str(year))

    for y in p:
        url = f'https://dota2.fandom.com/wiki/Patches{y}'
        date = str(datetime.now().date())
        soup = PARSE_MANAGER.parse(url, date)
        all_patches = soup.findAll('td')
        dates = []
        patches = []
        for i in range(len(all_patches)):
            if i % 3 == 0:
                arr = all_patches[i].text.replace('Dec', '12').replace('Nov', '11').replace('Oct', '10').replace('Sep',
                                                                                                                 '09') \
                    .replace('Aug', '08').replace('Jul', '07').replace('Jun', '06').replace('May', '05').replace('Apr',
                                                                                                                 '04') \
                    .replace('Mar', '03').replace('Feb', '02').replace('Jan', '01').split()
                if len(arr) == 3:
                    dates.append(arr[2] + arr[1] + arr[0])
                else:
                    dates.append(dates[-1])
            if i % 3 == 1:
                arr = all_patches[i].text.split()
                s = ''
                for a in arr:
                    if '.' in a and ('7' in a or '6' in a):
                        s = a
                        break
                patches.append(s)
        for i in range(len(patches)):
            if patches[i]:
                patches_date_dict[dates[i]] = patches[i]
                date_patches_dict[patches[i]] = dates[i]
                patches_list.append(patches[i])
    print(patches_list)
    save_to_pickle_file('statistic/patches_list', patches_list)
    save_to_pickle_file('statistic/patches_date_dict', patches_date_dict)
    save_to_pickle_file('statistic/date_patches_dict', date_patches_dict)

def show_statistic():
    for file in os.listdir("statistic"):
        print(read_pickle_file(f'statistic/{file}'))

def parse_patch():
    f = open('const', 'r')
    consts = f.readlines()
    f.close()
    number = consts[1]
    if number[-1] == '\n':
        number = number[:-1]
    patches_dict = read_pickle_file(f'statistic/date_patches_dict')
    print(number, patches_dict[number])
    try:
        os.mkdir(f'statistic/{number}')
    except:
        pass

    find_pro_players(number, patches_dict[number])
    update_heroes_list(number, patches_dict[number])
    update_heroes_win_rates(number, patches_dict[number])

    '''
    threads = [threading.Thread(target=update_heroes_list, args=(number, patches_dict[number])),
               threading.Thread(target=update_heroes_win_rates, args=(number, patches_dict[number])),
               threading.Thread(target=update_counters, args=(number, patches_dict[number])),
               threading.Thread(target=find_pro_players, args=(number, patches_dict[number]))
    ]
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    '''
    patches_list = read_pickle_file(f'statistic/patches_list')
    for i, patch in enumerate(patches_list):
        if patch == number:
            if i != len(patches_list) - 1:
                number = patches_list[i + 1]
                break

    consts[1] = number
    if len(consts) > 2:
        consts[1] += '\n'
    f = open('const', 'w')
    s = ''
    for i in consts:
        s += i
    f.write(s)


def main():
    while 1:
        parse_patch()

    # show_statistic()


if __name__ == '__main__':
    main()

    '''for i, func in enumerate(functions):
        print(i, func.__name__)
    n = int(input())
    functions[n]()'''
