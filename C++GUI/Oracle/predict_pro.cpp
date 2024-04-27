#include "predict_pro.h"
#include "ui_predict_pro.h"

predict_pro::predict_pro(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_pro)
{
    ui->setupUi(this);
    // team1pro = new QPushButton("team1");
    // horizon = new QHBoxLayout(this);
    // horizon->addWidget(team1pro);
}

predict_pro::~predict_pro()
{
    delete ui;
}

