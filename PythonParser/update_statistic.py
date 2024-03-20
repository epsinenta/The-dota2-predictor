import time
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient
from datetime import datetime
import threading
import os
from methods import save_to_pickle_file, read_pickle_file
from classes.parse_manager import ParseManager


PARSE_MANAGER = ParseManager()


def update_heroes_list():
    print("start update_heroes_list")
    url = 'https://www.dotabuff.com/heroes'
    date = str(datetime.now().date())
    first = datetime.now()
    soup = PARSE_MANAGER.parse(url, date)
    print(datetime.now() - first, "update_heroes_list")
    heroes_list_html = soup.findAll('div', class_='name')

    heroes_list = []
    for hero in heroes_list_html:
        heroes_list.append(hero.text)
    # save_to_pickle_file('statistic/heroes_list', heroes_list)


def update_heroes_win_rates():
    print("start update_heroes_win_rates")
    heroes_list = read_pickle_file('statistic/heroes_list')
    heroes_win_rate_dict = {}
    count = 0
    first = datetime.now()
    for hero in heroes_list:
        count += 1
        print(hero)
        _hero = hero
        if hero == "Nature's Prophet":
            hero = 'natures-prophet'
        url = f'https://www.dotabuff.com/heroes/{hero.replace(" ", "-").lower()}'
        date = str(datetime.now().date())
        soup = PARSE_MANAGER.parse(url, date)
        hero = _hero
        if len(soup.findAll('span', class_='won')) == 0:
            hero_winrate = soup.findAll('span', class_='lost')[0].text[:-1]
        else:
            hero_winrate = soup.findAll('span', class_='won')[0].text[:-1]
        heroes_win_rate_dict[hero] = hero_winrate
    print(datetime.now() - first)
    print(heroes_win_rate_dict)
    # save_to_pickle_file('statistic/heroes_win_rate_dict', heroes_win_rate_dict)


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
        date = str(datetime.now().date())
        soup = PARSE_MANAGER.parse(url, date)
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
        for i, hero_name in enumerate(heroes_names):
            second_hero = hero_name.text
            if second_hero == "Outworld Devourer":
                second_hero = 'Outworld Destroyer'

            heroes_counters_dict[hero][second_hero] = counters[i]
            heroes_counters_dict[second_hero][hero] = -counters[i]

    print(datetime.now() - first, "heroes_counters_dict")
    # save_to_pickle_file('statistic/heroes_counters_dict', heroes_counters_dict)


def find_pro_players():
    print("start find_pro_players")
    pro_players_list = []
    pro_players_id_dict = {}
    pro_players_win_rate_dict = {}
    first = datetime.now()
    url = f'https://www.dotabuff.com/players'
    date = str(datetime.now().date())
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
    # save_to_pickle_file('statistic/pro_players_win_rate_dict', pro_players_win_rate_dict)
    # save_to_pickle_file('statistic/pro_players_list', pro_players_list)
    # save_to_pickle_file('statistic/pro_players_id_dict', pro_players_id_dict)

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



def show_statistic():
    for file in os.listdir("statistic"):
        print(read_pickle_file(f'statistic/{file}'))


def main():
    threads = []

    #threads.append(threading.Thread(target=update_heroes_list))
    threads.append(threading.Thread(target=update_heroes_win_rates))
    #threads.append(threading.Thread(target=update_counters))
    #threads.append(threading.Thread(target=find_pro_players))
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    # show_statistic()


if __name__ == '__main__':
    main()

    '''for i, func in enumerate(functions):
        print(i, func.__name__)
    n = int(input())
    functions[n]()'''
