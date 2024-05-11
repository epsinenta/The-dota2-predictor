#include "predict_user.h"
#include "ui_predict_user.h"
#include "database_manager.h"
#include <QPixmap>
#include <QtGui>
predict_user::predict_user(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_user)
{
    ui->setupUi(this);
    ui->img->setStyleSheet("image: url(:/image_oracle/dota_teams.jpg)");
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result;
    std::map<std::string, std::string> m;
    m["patch"] = "7.35c";
    result = d.getRows("heroes_list", m);
    ui->cb1->addItem("Hero 1");
    ui->cb2->addItem("Hero 2");
    ui->cb3->addItem("Hero 3");
    ui->cb4->addItem("Hero 4");
    ui->cb5->addItem("Hero 5");
    ui->cb1_2->addItem("Hero 1");
    ui->cb2_2->addItem("Hero 2");
    ui->cb3_2->addItem("Hero 3");
    ui->cb4_2->addItem("Hero 4");
    ui->cb5_2->addItem("Hero 5");
    for(auto s : result){
        std::string start_s = s[1];
        std::replace(s[1].begin(), s[1].end(), ' ', '_');
        ui->cb1->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb2->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb3->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb4->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb5->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb1_2->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb2_2->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb3_2->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb4_2->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
        ui->cb5_2->addItem(QIcon(QString::fromStdString(":/image_oracle/heroes_png/" + s[1] + "_minimap_icon.png")), QString::fromStdString(start_s));
    }
}

predict_user::~predict_user()
{
    delete ui;
}


void predict_user::on_PredictButton_clicked()
{
    ui->winner_label->setText("Left team Winner!");
}

