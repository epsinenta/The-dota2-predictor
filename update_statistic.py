from bs4 import BeautifulSoup
from zenrows import ZenRowsClient
import requests
import os

from constants import CLIENT_API, PARAMS
from methods import save_to_pickle_file, read_pickle_file

client = ZenRowsClient(CLIENT_API)
params = PARAMS


def update_heroes_list():
    url = 'https://www.dotabuff.com/heroes'
    response = client.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    heroes_list_html = soup.findAll('div', class_='name')

    heroes_list = []
    for hero in heroes_list_html:
        heroes_list.append(hero.text)

    save_to_pickle_file('statistic/heroes_list', heroes_list)


def update_heroes_win_rates():
    heroes_list = read_pickle_file('statistic/heroes_list')
    heroes_win_rate_dict = {}

    for hero in heroes_list:
        print(hero)
        _hero = hero
        if hero == "Nature's Prophet":
            hero = 'natures-prophet'
        url = f'https://www.dotabuff.com/heroes/{hero.replace(" ", "-").lower()}'
        hero = _hero
        response = client.get(url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        if len(soup.findAll('span', class_='won')) == 0:
            hero_winrate = soup.findAll('span', class_='lost')[0].text[:-1]
        else:
            hero_winrate = soup.findAll('span', class_='won')[0].text[:-1]
        heroes_win_rate_dict[hero] = hero_winrate

    save_to_pickle_file('statistic/heroes_win_rate_dict', heroes_win_rate_dict)


def update_counters():
    heroes_list = read_pickle_file('statistic/heroes_list')
    heroes_counters_dict = {}
    for hero in heroes_list:
        heroes_counters_dict[hero] = {}

    for hero in heroes_list:
        print(hero)
        _hero = hero
        if hero == "Nature's Prophet":
            hero = 'natures-prophet'
        url = f'https://www.dotabuff.com/heroes/{hero.replace(" ", "-").lower()}/counters'
        hero = _hero
        response = client.get(url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        heroes_names = soup.findAll('a', class_='link-type-hero')
        data = soup.findAll('td', class_='sorted')
        for i, hero_name in enumerate(heroes_names):
            heroes_counters_dict[hero][hero_name.text] = float(data[i].text[:-1])
            heroes_counters_dict[hero_name.text][hero] = -float(data[i].text[:-1])

    save_to_pickle_file('statistic/heroes_counters_dict', heroes_counters_dict)


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

def find_players_win_rate():
    pro_players_id_dict = read_pickle_file('statistic/pro_players_id_dict')
    players_win_rate_on_heroes = {}
    count_matches_players_on_heroes = {}
    for pair in pro_players_id_dict.items():
        print(pair[0])
        players_win_rate_on_heroes[pair[0]] = {}
        count_matches_players_on_heroes[pair[0]] = {}
        url = f'https://www.dotabuff.com/players/{pair[1]}/heroes'
        response = client.get(url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        all_statistic = soup.findAll('td')
        delta = 0
        for index in range(0, len(all_statistic), 7):
            count_matches_players_on_heroes[pair[0]][all_statistic[index + delta]['data-value']] =\
                all_statistic[index + 2 + delta]['data-value']
            players_win_rate_on_heroes[pair[0]][all_statistic[index + delta]['data-value']] =\
                all_statistic[index + 3 + delta]['data-value']
            if all_statistic[index + 5 + delta]['data-value'] == '-1':
                delta += -1
    save_to_pickle_file('statistic/players_win_rate_on_heroes', players_win_rate_on_heroes)
    save_to_pickle_file('statistic/count_matches_players_on_heroes', count_matches_players_on_heroes)

def show_statistic():
    for file in os.listdir("statistic"):
        print(read_pickle_file(f'statistic/{file}'))


functions = [update_heroes_list,
             update_heroes_win_rates,
             update_counters,
             find_pro_players,
             find_players_win_rate,
             show_statistic]

if __name__ == '__main__':
    show_statistic()

    '''for i, func in enumerate(functions):
        print(i, func.__name__)
    n = int(input())
    functions[n]()'''
