#ifndef PREDICT_USER_H
#define PREDICT_USER_H

#include <QDialog>
#include <QPushButton>
#include <QHBoxLayout>
namespace Ui {
class predict_user;
}

class predict_user : public QDialog
{
    Q_OBJECT

public:
    explicit predict_user(QWidget *parent = nullptr);
    ~predict_user();

private slots:
    void on_PredictButton_clicked();

private:
    Ui::predict_user *ui;
};

#endif // PREDICT_USER_H
