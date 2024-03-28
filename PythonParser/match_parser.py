from parse_manager import ParseManager
from methods import read_pickle_file

PARSE_MANAGER = ParseManager()

class MatchParser:
    def __init__(self, id):
        self.url = f'https://ru.dltv.org/matches/{id}'
        self.soup = PARSE_MANAGER.parse(self.url)
        self.date = self.get_date()
        self.patch = self.get_patch()
        self.count_of_maps = self.get_count_of_maps()
        self.teams = self.get_teams()
        self.durations = self.get_durations()
        self.scores = self.get_scores()
        self.players = self.get_players()
        self.heroes = self.get_heroes()

    def get_durations(self):
        durations_html = self.soup.findAll('div', class_='info__duration')
        durations = []
        for d in durations_html:
            durations.append(int(d.text[:d.text.find(':')]) * 60 + int(d.text[d.text.find(':')+1:]))
        return durations

    def get_heroes(self):
        heroes_html = self.soup.findAll('div', class_='pick pick-sm')
        heroes = []
        for i in range(self.count_of_maps):
            cur = []
            for j in range(10):
                hero = heroes_html[i * 10 + j]
                s = str(hero)[len('<div class="pick pick-sm" data-tippy-content="'):]
                s = s[:s.index('"')]
                cur.append(s)
            heroes.append(cur)
        return heroes

    def get_players(self):
        players_html = self.soup.findAll('div', class_='cell__name')[:self.count_of_maps * 10]
        players = []
        for i in range(self.count_of_maps):
            cur = []
            for j in range(10):
                player = players_html[i * 10 + j]
                cur.append(player.text)
            players.append(cur)
        return players

    def get_scores(self):
        score_board_html = self.soup.findAll('div', class_='scoreboard')
        all_teams = []
        swap_teams = [self.teams[1], self.teams[0]]
        score = []
        for score_board in score_board_html:
            score.append(int(not bool(
                str(score_board).index('Match ID') < str(score_board).index('<div class="winner">win</div>'))))
            if str(score_board).index('Силы тьмы') < str(score_board).index('Силы света'):
                all_teams.append(swap_teams)
            else:
                all_teams.append(self.teams)

        for i in range(self.count_of_maps):
            if self.teams != all_teams[i]:
                score[i] = (score[i] + 1) % 2
        return score

    def get_teams(self):
        teams_html = self.soup.findAll('a', class_='team__stats-name')
        teams = []
        for team in teams_html:
            teams.append(team.text)
        return teams

    def get_count_of_maps(self):
        count = 0
        score_html = self.soup.findAll('div', class_='score__scores')
        try:
            count = int(score_html[0].text.replace(' ', '').replace('\n', '')[0]) + \
                    int(score_html[0].text.replace(' ', '').replace('\n', '')[2])
        except:
            count = 0
        return count

    def get_date(self):
        date = self.soup.findAll('div', class_='score__date')
        return str(date)[len('[<div class="score__date"><span data-moment="LL - LT"> '):len('[<div  class="score__date"><span data-moment="LL - LT">2024-03-28')]

    def get_patch(self):
        patches_dict = read_pickle_file('statistic/date_patches_dict')
        patches_list = read_pickle_file('statistic/patches_list')
        for i, patch in enumerate(patches_list):
            if not self.check_dates(patches_dict[patch]):
                return patches_list[i + 1]
        return patches_list[0]

    def check_dates(self, date):
        if int(self.date[:4]) > int(date[:4]):
            return True
        elif int(self.date[:4]) < int(date[:4]):
            return False
        else:
            if int(self.date[4:6]) > int(date[4:6]):
                return True
            elif int(self.date[4:6]) < int(date[4:6]):
                return False
            else:
                if int(self.date[6:]) > int(date[6:]):
                    return True
                elif int(self.date[6:]) < int(date[6:]):
                    return False
                else:
                    return True


