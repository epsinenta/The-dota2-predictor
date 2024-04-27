#ifndef PREDICT_PRO_H
#define PREDICT_PRO_H

#include <QDialog>
#include <QMenu>
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

private:
    Ui::predict_pro *ui;
    QMenu *menu;
    QPushButton *team1pro;
    QHBoxLayout *horizon;
};

#endif // PREDICT_PRO_H
