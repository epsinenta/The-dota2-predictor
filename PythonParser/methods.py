import pickle

def save_to_pickle_file(saved_file, content):
    with open(saved_file, "wb") as file:
        pickle.dump(content, file)

def read_pickle_file(readed_file):
    with open(readed_file, "rb") as file:
        return pickle.load(file)
