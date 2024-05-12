#ifndef PREDICT_PRO_H
#define PREDICT_PRO_H

#include <QDialog>
#include <QPushButton>
#include <QHBoxLayout>
namespace Ui {
class predict_pro;
}

class predict_pro : public QDialog
{
    Q_OBJECT

public:
    explicit predict_pro(QWidget *parent = nullptr);
    ~predict_pro();

private slots:

    void on_predict_button_clicked();

    void on_team2_select_menu_activated(int index);

    void on_team1_select_menu_activated(int index);

private:
    Ui::predict_pro *ui;
};

#endif // PREDICT_PRO_H
