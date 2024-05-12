#include "predict_pro.h"
#include "ui_predict_pro.h"
#include "widget_initializer.h"
#include <QPixmap>
#include <QtGui>
predict_pro::predict_pro(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_pro)
{
    ui->setupUi(this);
    std::vector<QComboBox*> teams_menu = {ui->team1_select_menu, ui->team2_select_menu};
    WidgetInitializer().initTeamsMenu(teams_menu);
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    WidgetInitializer().initHeroesMenu(heroes_menu);
}

predict_pro::~predict_pro()
{
    delete ui;
}

void predict_pro::on_predict_button_clicked()
{
    QPixmap pix(":/image_oracle/Team_Spirit.png");
    int w = ui->predict_team->width();
    int h = ui->predict_team->height();
    ui->predict_team->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
    ui->winner_label->setText("Spirit Winner!");
}


void predict_pro::on_team2_select_menu_activated(int index)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    if(index)
    {
        std::string s = result[index - 1][0];
        std::replace(s.begin(), s.end(), ' ', '_');
        std::replace(s.begin(), s.end(), '.', '_');
        ui->imgT2->setStyleSheet(QString::fromStdString("image: url(:/image_oracle/teams/" + s + ".png)"));
    }
}


void predict_pro::on_team1_select_menu_activated(int index)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    if(index)
    {
        std::string s = result[index - 1][0];
        std::replace(s.begin(), s.end(), ' ', '_');
        std::replace(s.begin(), s.end(), '.', '_');
        ui->imgT1->setStyleSheet(QString::fromStdString("image: url(:/image_oracle/teams/" + s + ".png)"));
    }
}

