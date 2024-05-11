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
    for(auto s : result){

        ui->cb1->addItem(QIcon(QString::fromStdString(":/image_oracle/" + s[1] + "_minimap_icon.png")), QString::fromStdString(s[1]));


    }

    ui->cb1->addItem(QIcon(":/image_oracle/Team_Spirit.png"), "PUDGE");

    ui->cb2->addItem("Hero 2");
    ui->cb2->addItem(QIcon(":/image_oracle/Team_Spirit.png"), "PUDGE");
    ui->cb2->addItem(QIcon(":/image_oracle/NAVI.png"), "ORACLE");
    ui->cb2->addItem(QIcon(":/image_oracle/cloud9.png"), "HERO");
    ui->cb3->addItem("Hero 3");
    ui->cb3->addItem(QIcon(":/image_oracle/Team_Spirit.png"), "PUDGE");
    ui->cb3->addItem(QIcon(":/image_oracle/NAVI.png"), "ORACLE");
    ui->cb3->addItem(QIcon(":/image_oracle/cloud9.png"), "HERO");
    ui->cb4->addItem("Hero 4");
    ui->cb5->addItem("Hero 5");
    ui->cb1_2->addItem("Hero 1");
    ui->cb2_2->addItem("Hero 2");
    ui->cb3_2->addItem("Hero 3");
    ui->cb4_2->addItem("Hero 4");
    ui->cb5_2->addItem("Hero 5");

}

predict_pro::~predict_pro()
{
    delete ui;
}

void predict_pro::on_comboBox1_activated(int index)
{
    if (index == 1){
        ui->imgT1->setStyleSheet("image: url(:/image_oracle/Team_Spirit.png)");
        ui->comboBox1->currentIndex();
    }
    else if (index == 2){
        ui->imgT1->setStyleSheet("image: url(:/image_oracle/liquid.png)");
        ui->comboBox1->currentIndex();
    }
    else if (index == 3){
        ui->imgT1->setStyleSheet("image: url(:/image_oracle/NAVI.png)");
        ui->comboBox1->currentIndex();
    }
    ui->cb1->addItem("Hero 1");
    ui->cb1->addItem(QIcon(":/image_oracle/Team_Spirit.png"), "PUDGE");
    ui->cb1->addItem(QIcon(":/image_oracle/NAVI.png"), "ORACLE");
    ui->cb1->addItem(QIcon(":/image_oracle/cloud9.png"), "HERO");
    ui->cb2->addItem("Hero 2");
    ui->cb2->addItem(QIcon(":/image_oracle/Team_Spirit.png"), "PUDGE");
    ui->cb2->addItem(QIcon(":/image_oracle/NAVI.png"), "ORACLE");
    ui->cb2->addItem(QIcon(":/image_oracle/cloud9.png"), "HERO");
    ui->cb3->addItem("Hero 3");
    ui->cb3->addItem(QIcon(":/image_oracle/Team_Spirit.png"), "PUDGE");
    ui->cb3->addItem(QIcon(":/image_oracle/NAVI.png"), "ORACLE");
    ui->cb3->addItem(QIcon(":/image_oracle/cloud9.png"), "HERO");
    ui->cb4->addItem("Hero 4");
    ui->cb5->addItem("Hero 5");
}


void predict_pro::on_comboBox1_2_activated(int index)
{
    if (index == 1){
        ui->imgT2->setStyleSheet("image: url(:/image_oracle/cloud9.png)");
        ui->comboBox1->currentIndex();
    }
    else if (index == 2){
        ui->imgT2->setStyleSheet("image: url(:/image_oracle/logo.png)");
        ui->comboBox1->currentIndex();
    }
    else if (index == 3){
        ui->imgT2->setStyleSheet("image: url(:/image_oracle/empire.png)");
        ui->comboBox1->currentIndex();
    }
    ui->cb1_2->addItem("Hero 1");
    ui->cb2_2->addItem("Hero 2");
    ui->cb3_2->addItem("Hero 3");
    ui->cb4_2->addItem("Hero 4");
    ui->cb5_2->addItem("Hero 5");
}


void predict_pro::on_predict_button_clicked()
{
    QPixmap pix(":/image_oracle/Team_Spirit.png");
    int w = ui->predict_team->width();
    int h = ui->predict_team->height();
    ui->predict_team->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
    ui->winner_label->setText("Spirit Winner!");
}

