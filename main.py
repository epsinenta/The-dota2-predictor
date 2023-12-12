import time

from bs4 import BeautifulSoup
import random
from zenrows import ZenRowsClient
import requests
import pandas as pd

client = ZenRowsClient("13ca0ec0fb07b2acca7653fa92acdccf9fee8e72")
params = {"js_render":"true","antibot":"true"}

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]

def find_all_id():
    f = open('id', 'r')
    a = f.readlines()[-1]
    f.close()
    f = open('id', 'a')
    print(a)
    for n in range(int(a)-1, 0, -1):
        url = f'https://www.cybersport.ru/matches/dota-2/{n}'
        page = requests.get(url)
        if page.status_code == 200:
            f.write(f'{n}\n')
    f.close()



def get_winrate(team, player, hero):
    url = f'https://www.dotabuff.com/search?q={player.replace(" ", "+")}&commit=Search'
    response = client.get(url, params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    players_html = soup.findAll('div', class_='inner')

    url = f'https://www.dotabuff.com/{players_html[0]["data-link-to"]}/heroes?metric=played'
    response = client.get(url, params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    heroes_html = soup.findAll('td', class_='cell-icon')
    played_html = soup.findAll('td', class_='sorted')


    url = f'https://www.dotabuff.com/{players_html[0]["data-link-to"]}/heroes?metric=played'
    response = client.get(url, params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    heroes_html = soup.findAll('td', class_='cell-icon')
    played_html = soup.findAll('td', class_='sorted')
    played = 0
    for i in range(len(heroes_html)):
        if heroes_html[i]["data-value"] == hero:
            played = played_html[i]["data-value"]


    url = f'https://www.dotabuff.com/{players_html[0]["data-link-to"]}/heroes?metric=winning'
    response = client.get(url, params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    heroes_html = soup.findAll('td', class_='cell-icon')
    winning_html = soup.findAll('td', class_='sorted')
    winrate = 0
    for i in range(len(heroes_html)):
        if heroes_html[i]["data-value"] == hero:
            winrate = winning_html[i]["data-value"]

    return [played, winrate]

def parse_match(id):
    url = f'https://ru.dltv.org/matches/{id}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    score_html = soup.findAll('div', class_='score__scores')
    count = int(score_html[0].text.replace(' ', '').replace('\n', '')[0]) + \
            int(score_html[0].text.replace(' ', '').replace('\n', '')[2])

    teams_html = soup.findAll('a', class_='team__stats-name')
    teams = []
    for team in teams_html:
        teams.append(team.text)

    score_board_html = soup.findAll('div', class_='scoreboard')
    all_teams = []
    swap_teams = [teams[1], teams[0]]
    score = []
    for score_board in score_board_html:
        score.append(int(not bool(str(score_board).index('Match ID') < str(score_board).index('<div class="winner">win</div>'))))
        if str(score_board).index('Силы тьмы') < str(score_board).index('Силы света'):
            all_teams.append(swap_teams)
        else:
            all_teams.append(teams)

    for i in range(count):
        if teams != all_teams[i]:
            score[i] = (score[i] + 1) % 2


    players_html = soup.findAll('div', class_='cell__name')
    players = []
    for player in players_html:
        players.append(player.text)

    heroes_html = soup.findAll('div', class_='pick pick-sm')
    heroes = []
    for hero in heroes_html:
        s = str(hero)[len('<div class="pick pick-sm" data-tippy-content="'):]
        s = s[:s.index('"')]
        heroes.append(s)

    players_on_heroes = []

    for i in range(count):
        cur = []
        for j in range(10):
            cur.append(players[i * 10 + j] + " on " + heroes[i * 10 + j])
        players_on_heroes.append(cur)
    #TODO: сделать винрейты
    winrates = []
    for i in range(count):
        cur = []
        for j in range(10):
            if j < 5:
                cur_team = all_teams[i][0]
            else:
                cur_team = all_teams[i][1]
            cur.append(get_winrate(cur_team, players[i * 10 + j], heroes[i * 10 + j]))
        winrates.append(cur)

    result = []
    for i in range(count):
        result.append([score[i], *all_teams[i], *players_on_heroes[i], *winrates[i]])


    return result


def parse_matches():
    last_match = int(open('const', 'r').readlines()[0])
    context = parse_match(last_match)
    last_match -= 1
    open('const', 'w').write(str(last_match))
    return context

if __name__ == '__main__':
    df = pd.read_csv('matches.csv')
    print(df)
    for i in range(10):
        cur_matches = parse_matches()
        for match in cur_matches:
            df.loc[-1] = [0, *match]
            df.index = df.index + 1
            df = df.sort_index()

    df.to_csv('matches.csv')

    print(df)
