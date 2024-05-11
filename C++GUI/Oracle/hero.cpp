#include "hero.h"
#include "ui_hero.h"
#include "database_manager.h"
#include <QPixmap>
Hero::Hero(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Hero)
{
    ui->setupUi(this);

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

Hero::~Hero()
{
    delete ui;
}

void Hero::on_Select_hero_clicked()
{
    QPixmap first_hero(":/image_oracle/gyrocopter.jpg");
    int w = ui->hero1->width();
    int h = ui->hero1->height();
    ui->hero1->setPixmap(first_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap second_hero(":/image_oracle/chel.jpg");
    w = ui->hero2->width();
    h = ui->hero2->height();
    ui->hero2->setPixmap(second_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap third_hero(":/image_oracle/chel2.jpg");
    w = ui->hero3->width();
    h = ui->hero3->height();
    ui->hero3->setPixmap(third_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap fouth_hero(":/image_oracle/chel3.jpg");
    w = ui->hero4->width();
    h = ui->hero4->height();
    ui->hero4->setPixmap(fouth_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap fifth_hero(":/image_oracle/chel4.jpg");
    w = ui->hero5->width();
    h = ui->hero5->height();
    ui->hero5->setPixmap(fifth_hero.scaled(w,h,Qt::KeepAspectRatio));
}

