#include "predictpro.h"
#include "ui_predictpro.h"
PredictPRO::PredictPRO(QWidget *parent):
    QDialog(parent),
    ui(new Ui::PredictPRO)
{
    ui->setupUi(this);
}

PredictPRO::~PredictPRO()
{
    delete ui;
}


