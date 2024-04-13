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


auto_convert_patches()