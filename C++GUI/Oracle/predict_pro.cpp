#include "predict_pro.h"
#include "ui_predict_pro.h"
#include "widget_initializer.h"
#include <QPixmap>
#include <QtGui>
#include <memory>
#include <stdexcept>
#include "predictmanager.h"
#include <iostream>
#include <QScreen>
predict_pro::predict_pro(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_pro)
{
    ui->setupUi(this);
    std::vector<QComboBox*> teams_menu = {ui->team1_select_menu, ui->team2_select_menu};
    WidgetInitializer().initTeamsMenu(teams_menu);
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    WidgetInitializer().initHeroesMenu(heroes_menu);
    QScreen *screen = QGuiApplication::primaryScreen();
    QRect screenGeometry = screen->geometry();

    int newWidth = screenGeometry.width()*0.7;
    int newHeight = screenGeometry.height()*0.7;
    resize(newWidth, newHeight);
}

predict_pro::~predict_pro()
{
    delete ui;
}
std::string exec(std::string cmd) {
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
void predict_pro::on_predict_button_clicked()
{

    std::vector<QComboBox*> teams_menu = {ui->team1_select_menu, ui->team2_select_menu};
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    std::vector<std::string> teams;
    std::vector<std::string> heroes;
    for(auto team_menu : teams_menu)
        teams.push_back(team_menu->currentText().toStdString());
    for(auto hero_menu : heroes_menu)
        heroes.push_back(hero_menu->currentText().toStdString());
    double chance = PredictManager().getWinTeam(teams, heroes);
    int w = ui->predict_team->width();
    int h = ui->predict_team->height();
    chance *= 100;
    std::string winnerTeam = ui->team1_select_menu->currentText().toStdString();
    if(chance < 50)
    {
        winnerTeam = ui->team2_select_menu->currentText().toStdString();
        chance = 100 - chance;
    }
    std::string str_chance;
    std::string buf = std::to_string(chance);
    for(int i = 0; i < 5; i++)
        str_chance += buf[i];
    str_chance += "%";
    std::replace(winnerTeam.begin(), winnerTeam.end(), ' ', '_');
    std::replace(winnerTeam.begin(), winnerTeam.end(), '.', '_');
    QPixmap pix(QString::fromStdString(":/image_oracle/teams/" + winnerTeam + ".png"));
    ui->predict_team->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
    ui->winner_label->setText(QString::fromStdString(str_chance));
}


void predict_pro::on_team2_select_menu_activated(int index)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    if(index)
    {
        std::string team = result[index - 1][0];
        std::replace(team.begin(), team.end(), ' ', '_');
        std::replace(team.begin(), team.end(), '.', '_');
        ui->imgT2->setStyleSheet(QString::fromStdString("image: url(:/image_oracle/teams/" + team + ".png)"));
    }
}


void predict_pro::on_team1_select_menu_activated(int index)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    if(index)
    {
        std::string team = result[index - 1][0];
        std::replace(team.begin(), team.end(), ' ', '_');
        std::replace(team.begin(), team.end(), '.', '_');
        ui->imgT1->setStyleSheet(QString::fromStdString("image: url(:/image_oracle/teams/" + team + ".png)"));
    }
}

