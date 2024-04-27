#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QPixmap>
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

void MainWindow::on_help_clicked()
{
    heroc = new Hero(this);
    std::cout << 123;
    heroc->show();
    //hide();
}


void MainWindow::on_pushButton_clicked()
{
    heroc = new Hero(this);
    heroc->show();
}


void MainWindow::on_PredictPRO_clicked()
{
    pro = new predict_pro(this);
    pro->show();
    hide();
}


void MainWindow::on_PredictUSER_clicked()
{
    user = new predict_user(this);
    user->show();
    hide();
}

