import pickle
from database_services import DataBaseManager

def save_to_pickle_file(saved_file, content):
    with open(saved_file, "wb") as file:
        pickle.dump(content, file)

def read_pickle_file(readed_file):
    with open(readed_file, "rb") as file:
        return pickle.load(file)


def auto_convert_patches():
    manager = DataBaseManager('Dota')
    manager.clear_table('patches')
    data = read_pickle_file('statistic/date_patches_dict')
    print(manager.get_struct('patches'))
    for key in data.keys():
        manager.add_row('patches', [key, data[key]])
    print(manager.get_full_table('patches'))

def auto_convert_heroes_counters():
    manager = DataBaseManager('Dota')
    manager.clear_table('heroes_counters')
    data = read_pickle_file('statistic/heroes_counters_dict')
    print(manager.get_struct('heroes_counters'))
    for first_hero in data.keys():
        for second_hero in data[first_hero].keys():
            manager.add_row('heroes_counters', [first_hero, second_hero, data[first_hero][second_hero]])
    print(manager.get_full_table('heroes_counters'))

def auto_convert_heroes_list_per_patch(patch):
    manager = DataBaseManager('Dota')
    data = read_pickle_file(f'statistic/{patch}/heroes_win_rate_dict')
    print(manager.get_struct('heroes_list'))
    for hero in data.keys():
        print(hero)
        manager.add_row('heroes_list', [patch, hero, data[hero]])


def auto_convert_players_heroes_statistic():
    manager = DataBaseManager('Dota')
    manager.clear_table('players_heroes_statistic')
    winrates = read_pickle_file(f'statistic/players_win_rate_on_heroes')
    count = read_pickle_file(f'statistic/count_matches_players_on_heroes')
    print(manager.get_struct('players_heroes_statistic'))
    for player in winrates.keys():
        for hero in winrates[player].keys():
            manager.add_row('players_heroes_statistic', [player, hero, winrates[player][hero], count[player][hero]])
    print(manager.get_full_table('players_heroes_statistic'))

def auto_convert_players_list_patch(patch):
    manager = DataBaseManager('Dota')
    data = read_pickle_file(f'statistic/{patch}/pro_players_win_rate_dict')
    print(manager.get_struct('pro_players_list'))
    for player in data.keys():
        manager.add_row('pro_players_list', [patch, player, data[player]])


if __name__ == '__main__':
    auto_convert_patches() #patches

    auto_convert_players_heroes_statistic() #players_heroes_statistic

    auto_convert_heroes_counters() #heroes_counters

    patches = read_pickle_file('statistic/patches_list')
    last_patch = open('const', 'r').readlines()[1]
    print(last_patch)
    for patch in patches:
        print(patch)
        if patch != last_patch:

            auto_convert_heroes_list_per_patch(patch) #heroes_list

            auto_convert_players_list_patch(patch) #pro_players_list

        else:
            break
