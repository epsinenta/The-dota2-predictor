import pandas as pd
from match_parser import MatchParser

def parse_matches():
    f = open('const', 'r')
    arr = f.readlines()
    f.close()
    last_match = int(arr[0][:-1])
    print(last_match)
    try:
        context = MatchParser(last_match).get_result()
    except:
        context = []
    last_match -= 1
    arr[0] = str(last_match) + '\n'
    res_str = ''
    for a in arr:
        res_str += a
    f = open('const', 'w')
    f.write(res_str)
    f.close()
    return context

if __name__ == '__main__':

    df = pd.read_csv('matches.csv')
    df.drop(df.columns[[0]], axis=1, inplace=True)
    print(df.head())
    print(df.shape)
    #df = pd.DataFrame([['413487.0', 0, 3968, '7.35b', 'Azure Ray', 'G2.iG', 'Faith_bian', '天命', 'fy', 'Ori', 'Lou', 'Monet', 'BoBoKa', 'NothingToSay', 'xNova', 'JT-', 'Timbersaw', 'Elder Titan', 'Shadow Shaman', 'Zeus', 'Clinkz', 'Luna', 'Lion', 'Razor', 'Disruptor', 'Magnus', 50, '52.842556', '58.38978', '55.028183', '53.42043', '54.84208', 50, 50, 50, '52.712887', 30, '77', '68', 30, '92', '62', 30, 30, 30, 30, '51.10', '48.94', '52.41', '51.38', '52.54', '49.73', '47.65', '49.14', '49.61', '47.72', 0.43, 0.54, 0.52, 0.95, 1.03, -0.2, 1.31, -1.82, -2.0, -0.02, 1.25, 0.55, 1.59, 0.26, 0.07, -1.61, 0.61, 0.31, 0.56, 0.98, 0.36, 0.98, 1.45, -0.76, -0.06], ['413487.1', 0, 2636, '7.35b', 'Azure Ray', 'G2.iG', 'Faith_bian', '天命', 'fy', 'Ori', 'Lou', 'Monet', 'BoBoKa', 'xNova', 'NothingToSay', 'JT-', 'Timbersaw', 'Shadow Demon', 'Shadow Shaman', 'Templar Assassin', 'Alchemist', 'Luna', 'Lion', 'Enchantress', 'Zeus', 'Doom', 50, '52.842556', '58.38978', '55.028183', '53.42043', '54.84208', 50, 50, 50, '52.712887', 30, '53', '68', 30, '83', '62', 30, 30, 30, 30, '51.10', '46.61', '52.41', '43.84', '46.43', '49.73', '47.65', '45.82', '51.38', '47.93', 0.43, 0.54, 1.14, -1.09, 1.45, -2.05, -0.24, 0.85, -1.51, 1.1, 1.25, 0.55, 2.35, -0.28, 1.27, 0.69, -0.8, 0.59, -2.16, 1.2, 0.33, -0.23, 0.55, -1.31, 0.88], ['413487.2', 1, 3188, '7.35b', 'Azure Ray', 'G2.iG', 'fy', '天命', 'Ori', 'Lou', 'Faith_bian', 'NothingToSay', 'xNova', 'Monet', 'BoBoKa', 'JT-', 'Gyrocopter', 'Clockwerk', 'Death Prophet', 'Naga Siren', 'Omniknight', 'Primal Beast', 'Shadow Shaman', 'Terrorblade', 'Mirana', 'Doom', '58.38978', '52.842556', '55.028183', '53.42043', 50, 50, 50, '54.84208', 50, '52.712887', '42', '101', 30, '208', 30, 30, 30, '199', 30, 30, '47.33', '49.16', '53.95', '48.54', '47.14', '47.92', '52.41', '49.42', '47.84', '47.93', 0.07, -0.58, -0.55, 0.24, 0.85, -2.08, -0.26, 1.38, 0.08, -0.11, -1.82, -0.93, 0.7, 1.25, -0.53, -0.03, -2.57, -1.91, -3.22, -0.99, 0.46, -1.8, 0.32, -0.9, 2.63], ['413487.3', 0, 3955, '7.35b', 'Azure Ray', 'G2.iG', 'Lou', 'fy', '天命', 'Faith_bian', 'Ori', 'JT-', 'xNova', 'Monet', 'NothingToSay', 'BoBoKa', 'Terrorblade', 'Rubick', 'Leshrac', 'Centaur Warrunner', 'Storm Spirit', 'Magnus', 'Shadow Demon', 'Luna', 'Razor', 'Hoodwink', '53.42043', '58.38978', '52.842556', 50, '55.028183', '52.712887', 50, '54.84208', 50, 50, '125', '372', '102', 30, 30, 30, 30, '62', 30, 30, '49.42', '45.34', '51.02', '52.41', '46.16', '47.72', '46.61', '49.73', '49.14', '50.95', -0.25, -0.65, -1.67, -0.7, 0.36, -0.86, 0.72, -1.87, 1.09, 0.35, -1.98, -0.99, -0.44, -0.1, 0.75, 0.33, -0.9, -0.13, 0.03, -1.09, -0.44, -2.07, 0.27, -1.35, -1.62]])
    for j in range(1):
        for i in range(10):
            cur_matches = parse_matches()
            if len(cur_matches) > 0:
                for match in cur_matches:
                    df.loc[-1] = [*match]
                    df.index = df.index + 1
                    df = df.sort_index()
        print('соточка прошла', j)
        df.to_csv('matches.csv')

    print(df.head())
    print(df.shape)

