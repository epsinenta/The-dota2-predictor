#ifndef WIDGETINITIALIZER_H
#define WIDGETINITIALIZER_H
#include <Vector>
#include <QComboBox>
#include "database_manager.h"
class WidgetInitializer
{
public:
    WidgetInitializer();
    void initHeroesMenu(std::vector<QComboBox*>& heroes_menu);
    void initTeamsMenu(std::vector<QComboBox*>& teams_menu);
};

#endif // WIDGETINITIALIZER_H
