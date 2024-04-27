#include "hero.h"
#include "ui_hero.h"

Hero::Hero(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Hero)
{
    ui->setupUi(this);
}

Hero::~Hero()
{
    delete ui;
}
