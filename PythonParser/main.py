from bs4 import BeautifulSoup
from zenrows import ZenRowsClient
import requests
import pandas as pd
from methods import read_pickle_file
from constants import CLIENT_API, PARAMS

client = ZenRowsClient(CLIENT_API)
params = PARAMS
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
    try:
        count = int(score_html[0].text.replace(' ', '').replace('\n', '')[0]) + \
                int(score_html[0].text.replace(' ', '').replace('\n', '')[2])
    except:
        count = 0
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


    players_html = soup.findAll('div', class_='cell__name')[:count * 10]
    players = []
    for i in range(count):
        cur = []
        for j in range(10):
            player = players_html[i * 10 + j]
            cur.append(player.text)
        players.append(cur)

    heroes_html = soup.findAll('div', class_='pick pick-sm')
    heroes = []
    for i in range(count):
        cur = []
        for j in range(10):
            hero = heroes_html[i * 10 + j]
            s = str(hero)[len('<div class="pick pick-sm" data-tippy-content="'):]
            s = s[:s.index('"')]
            cur.append(s)
        heroes.append(cur)

    heroes_win_rate_dict = read_pickle_file('statistic/heroes_win_rate_dict')
    heroes_winrates = []
    for i in range(count):
        cur = []
        for j in range(10):
            hero = heroes[i][j]
            if hero == "Nature's Prophet":
                hero = 'natures-prophet'
            cur.append(heroes_win_rate_dict[hero])
        heroes_winrates.append(cur)

    heroes_counters_dict = read_pickle_file('statistic/heroes_counters_dict')
    heroes_counters = []
    for i in range(count):
        cur = []
        for j in range(5):
            for k in range(5, 10):
                hero1 = heroes[i][j]
                hero2 = heroes[i][k]
                cur.append(heroes_counters_dict[hero1][hero2])
        heroes_counters.append(cur)
    '''
    players_on_heroes = []
    for i in range(count):
        cur = []
        for j in range(10):
            cur.append(players[i * 10 + j] + " on " + heroes[i * 10 + j])
        players_on_heroes.append(cur)
    '''
    '''
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
    '''
    winrates = [[50.0] * 10] * count
    result = []
    for i in range(count):
        result.append([score[i], *all_teams[i], *players[i], *winrates[i], *heroes_winrates[i], *heroes_counters[i]])
    print(id, 123)
    return result


def parse_matches():
    last_match = int(open('const', 'r').readlines()[0])
    print(last_match)
    try:
        context = parse_match(last_match)
    except:
        context = []
    last_match -= 1
    open('const', 'w').write(str(last_match))
    return context

if __name__ == '__main__':
    a = read_pickle_file("statistic/pro_players_id_dict")
    print(a)
    '''
    df = pd.read_csv('matches.csv')
    df.drop(df.columns[[0]], axis=1, inplace=True)
    print(df)
    #df = pd.DataFrame([[1, 'Sporkface Killaz', 'Bullish on Gaming', 'Kurona', 'babitich', 'jah', 'Chola', 'Fayde', 'Mark', 'Froogoss', 'NFLS.ClouD', 'Harold', 'Double King', 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, '49.41', '51.04', '54.92', '50.19', '51.85', '47.34', '46.43', '48.89', '50.24', '48.96', 0.5, -0.54, -0.59, 0.54, 0.37, 0.48, -0.15, 1.57, 1.07, 1.59, -0.53, -0.23, 2.78, 0.27, -0.28, 1.16, -0.71, -0.02, -0.07, 0.96, 1.55, 0.99, -0.15, -3.49, 1.3]])
    for j in range(200):
        for i in range(100):
            cur_matches = parse_matches()
            if len(cur_matches) > 0:
                for match in cur_matches:
                    df.loc[-1] = [*match]
                    df.index = df.index + 1
                    df = df.sort_index()
        print('соточка прошла')
        df.to_csv('matches.csv')

    print(df)
    '''
