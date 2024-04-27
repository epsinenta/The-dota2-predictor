#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include "predict_user.h"
#include "hero.h"
#include "predict_pro.h"
QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_predictp_clicked();

    void on_predictu_clicked();

    void on_help_clicked();

private:
    Ui::MainWindow *ui;

    Hero *heroc;
    predict_user *user;
    predict_pro *pro;
};
#endif // MAINWINDOW_H
