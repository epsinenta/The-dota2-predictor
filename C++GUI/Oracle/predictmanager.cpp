#include "predictmanager.h"
#include <memory>
#include <stdexcept>
#include <array>
#include <vector>
#include <map>
#include "database_manager.h"
#include "text_file_manager.h"
PredictManager::PredictManager(){};

std::string PredictManager::execute(std::string cmd)
{
    std::array<char, 128> buffer;
    std::string result;
#ifdef _WIN32
    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(cmd.c_str(), "r"), _pclose);
#else
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
#endif
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

double PredictManager::makePredict()
{
    std::string result = execute("python ..\\..\\model\\get_predict.py");
    std::string chance = "";
    for(int i = 7; i < 13; i++)
        chance += result[i];
    return std::stod(chance);
}

double PredictManager::getWinTeam(std::vector<std::string> teams, std::vector<std::string> heroes)
{
    std::vector<std::string> request;
    std::string patch = "7.35b";
    request.push_back(patch);
    DataBaseManager d("Dota");


    std::vector<std::string> players;

    for(auto team : teams)
    {
        std::vector<std::vector<std::string>> result;
        std::map<std::string, std::string> args;
        args["team_name"] = team;
        result = d.getRows("teams_roasters", args);
        if(result.size())
            for(int i = 1; i < 6; i++)
            {
                players.push_back(result[0][i]);
            }
        else
            for(int i = 0; i < 5; i++)players.push_back("");
    }


    std::vector<std::string> winrates;
    for(int i = 0; i < 10; i++)
    {
        std::string player = players[i];
        std::vector<std::vector<std::string>> result;
        std::map<std::string, std::string> args;
        args["patch"] = patch;
        args["player_name"] = player;
        result = d.getRows("pro_players_list", args);
        if(result.size())
            winrates.push_back(result[0][2]);
        else
            winrates.push_back("50.0");
    }
    std::vector<std::string> winrates_on_heroes;
    std::vector<std::string> count_on_heroes;

    for(int i = 0; i < 10; i++)
    {
        std::string player = players[i];
        std::string hero = heroes[i];
        std::vector<std::vector<std::string>> result;
        std::map<std::string, std::string> args;
        args["hero_name"] = hero;
        args["player_name"] = player;
        result = d.getRows("players_heroes_statistic", args);
        if(result.size())
        {
            winrates_on_heroes.push_back(result[0][2]);
            count_on_heroes.push_back(result[0][3]);
        }
        else
        {
            winrates_on_heroes.push_back("50.0");
            count_on_heroes.push_back("30");
        }
    }
    std::vector<std::string> heroes_winrates;
    for(int i = 0; i < 10; i++)
    {
        std::string hero = heroes[i];
        std::vector<std::vector<std::string>> result;
        std::map<std::string, std::string> args;
        args["patch"] = patch;
        args["hero_name"] = hero;
        result = d.getRows("heroes_list", args);
        if(result.size())
            heroes_winrates.push_back(result[0][2]);
        else
            heroes_winrates.push_back("50.0");
    }
    std::vector<std::string> counters;
    for(int i = 0; i < 5; i++)
    {
        std::string hero1 = heroes[i];
        for(int j = 5; j < 10; j++)
        {
            std::string hero2 = heroes[j];
            std::vector<std::vector<std::string>> result;
            std::map<std::string, std::string> args;
            args["first_hero_name"] = hero1;
            args["second_hero_name"] = hero2;
            result = d.getRows("heroes_counters", args);
            if(result.size())
                counters.push_back(result[0][2]);
            else
                counters.push_back("0");
        }
    }
    std::string str_request = "0,2400," + patch;
    std::cout << teams.size() << ' ' << players.size() << ' ' << heroes.size() << ' ' << winrates.size() << ' ' << count_on_heroes.size() << ' ' << winrates_on_heroes.size() << ' ' << heroes_winrates.size() << ' ' << count_on_heroes.size() << '\n';
    for(auto team : teams)
        str_request += "," + team;
    for(auto player : players)
        str_request += "," + player;
    for(auto hero : heroes)
        str_request += "," + hero;
    for(auto winrate : winrates)
        str_request += "," + winrate;
    for(auto count_on_hero : count_on_heroes)
        str_request += "," + count_on_hero;
    for(auto winrate_on_hero : winrates_on_heroes)
        str_request += "," + winrate_on_hero;
    for(auto hero_winrate : heroes_winrates)
        str_request += "," + hero_winrate;
    for(auto counter : counters)
        str_request += "," + counter;
    std::cout << str_request;

    TextFileManager().write("row.txt", str_request);
    return makePredict();
}
