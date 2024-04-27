#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QPixmap>
#include <iostream>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPixmap pix(":/image_oracle/772c7ffb-no-bg-HD (carve.photos).png");
    int w = ui->mainimg->width();
    int h = ui->mainimg->height();
    ui->mainimg->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_predictp_clicked()
{
    pro = new predict_pro(this);
    std::cout << 123;
    pro->show();
    hide();
}

void MainWindow::on_predictu_clicked()
{
    user = new predict_user(this);
    user->show();
    hide();
}

void MainWindow::on_help_clicked()
{
    heroc = new Hero(this);
    std::cout << 123;
    heroc->show();
    //hide();
}

