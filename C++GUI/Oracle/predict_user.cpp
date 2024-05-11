#include "predict_user.h"
#include "ui_predict_user.h"
#include <QPixmap>
#include <QtGui>
predict_user::predict_user(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_user)
{
    ui->setupUi(this);
    ui->img->setStyleSheet("image: url(:/image_oracle/dota_teams.jpg)");
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
}

predict_user::~predict_user()
{
    delete ui;
}


void predict_user::on_PredictButton_clicked()
{
    ui->winner_label->setText("Left team Winner!");
}

