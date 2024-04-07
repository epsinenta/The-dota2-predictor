#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "second.h"
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    hide();
    second pred;
    pred.setModal(true);
    pred.exec();
}


void MainWindow::on_pushButton_2_clicked()
{
    hide();
    second pred;
    pred.setModal(true);
    pred.exec();
}


void MainWindow::on_pushButton_3_clicked()
{
    hide();
    second pred;
    pred.setModal(true);
    pred.exec();
}

