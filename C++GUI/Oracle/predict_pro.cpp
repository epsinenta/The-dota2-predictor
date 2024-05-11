#include "predict_pro.h"
#include "ui_predict_pro.h"
#include "database_manager.h"
#include <QPixmap>
#include <QtGui>
predict_pro::predict_pro(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_pro)
{
    ui->setupUi(this);
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    for(auto s : result){
        ui->comboBox1->addItem(QString::fromStdString(s[0]));
        ui->comboBox1_2->addItem(QString::fromStdString(s[0]));
    }
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

predict_pro::~predict_pro()
{
    delete ui;
}

void predict_pro::on_comboBox1_activated(int index)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    if(index)
    {
        std::string s = result[index - 1][0];
        std::replace(s.begin(), s.end(), ' ', '_');
        ui->imgT1->setStyleSheet(QString::fromStdString("image: url(:/image_oracle/teams/" + s + ".png)"));
    }
}

void predict_pro::on_comboBox1_2_activated(int index)
{
    DataBaseManager d("Dota");
    std::vector<std::vector<std::string>> result = d.getFullTable("teams_roasters");
    if(index)
    {
        std::string s = result[index - 1][0];
        std::replace(s.begin(), s.end(), ' ', '_');
        ui->imgT2->setStyleSheet(QString::fromStdString("image: url(:/image_oracle/teams/" + s + ".png)"));
    }
}


void predict_pro::on_predict_button_clicked()
{
    QPixmap pix(":/image_oracle/Team_Spirit.png");
    int w = ui->predict_team->width();
    int h = ui->predict_team->height();
    ui->predict_team->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
    ui->winner_label->setText("Spirit Winner!");
}

