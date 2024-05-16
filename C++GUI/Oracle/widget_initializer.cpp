#include "widget_initializer.h"

WidgetInitializer::WidgetInitializer() {}

void WidgetInitializer::initHeroesMenu(std::vector<QComboBox*>& heroes_menu)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result;
    std::map<std::string, std::string> args;
    args["patch"] = "7.35c";
    result = d.getRows("heroes_list", args);
    for(int i = 0; i < 10; i++)
    {
        heroes_menu[i]->addItem(QString::fromStdString("Hero " + std::to_string((i % 5) + 1)));
    }
    for(auto s : result){
        std::string start_s = s[1];
        std::replace(s[1].begin(), s[1].end(), ' ', '_');
        for(auto hero_menu : heroes_menu)
            hero_menu->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
    }
}

void WidgetInitializer::initTeamsMenu(std::vector<QComboBox*>& teams_menu)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    for(auto s : result)
        for(auto team : teams_menu)
            team->addItem(QString::fromStdString(s[0]));
}
