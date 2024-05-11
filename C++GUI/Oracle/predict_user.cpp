#include "predict_user.h"
#include "ui_predict_user.h"

predict_user::predict_user(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::predict_user)
{
    ui->setupUi(this);
}

predict_user::~predict_user()
{
    delete ui;
}
