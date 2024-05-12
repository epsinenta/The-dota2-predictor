#include "predict_user.h"
#include "ui_predict_user.h"
#include "widget_initializer.h"
#include <QPixmap>
#include <QtGui>
predict_user::predict_user(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_user)
{
    ui->setupUi(this);
    ui->img->setStyleSheet("image: url(:/image_oracle/dota_teams.jpg)");
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    WidgetInitializer().initHeroesMenu(heroes_menu);
}

predict_user::~predict_user()
{
    delete ui;
}


void predict_user::on_PredictButton_clicked()
{
    ui->winner_label->setText("Left team Winner!");
}

