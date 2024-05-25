#include "predict_user.h"
#include "ui_predict_user.h"
#include "widget_initializer.h"
#include <QPixmap>
#include <QtGui>
#include "predictmanager.h"
#include <QScreen>
predict_user::predict_user(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_user)
{
    ui->setupUi(this);
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    WidgetInitializer().initHeroesMenu(heroes_menu);
    QScreen *screen = QGuiApplication::primaryScreen();
    QRect screenGeometry = screen->geometry();

    int newWidth = screenGeometry.width()*0.7;
    int newHeight = screenGeometry.height()*0.7;
    resize(newWidth, newHeight);
}

predict_user::~predict_user()
{
    delete ui;
}


void predict_user::on_PredictButton_clicked()
{
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    std::vector<std::string> teams = {"", ""};
    std::vector<std::string> heroes;
    for(auto hero_menu : heroes_menu)
        heroes.push_back(hero_menu->currentText().toStdString());
    double chance = PredictManager().getWinTeam(teams, heroes);
    std::string str_chance = "Radiant win\n";
    chance *= 100;
    if(chance < 50)
    {
        str_chance = "Dire win\n";
        chance = 100 - chance;
    }

    std::string buf = std::to_string(chance);
    for(int i = 0; i < 5; i++)
        str_chance += buf[i];
    str_chance += "%";
    ui->winner_label->setText(QString::fromStdString(str_chance));
}

