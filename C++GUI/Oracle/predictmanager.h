#ifndef PREDICTMANAGER_H
#define PREDICTMANAGER_H
#include <string>
#include <vector>
class PredictManager
{
public:
    PredictManager();
    double getWinTeam(std::vector<std::string> teams, std::vector<std::string> heroes);
    double makePredict();
    std::string execute(std::string cmd);
};
#endif // PREDICTMANAGER_H
