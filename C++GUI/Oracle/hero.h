#ifndef HERO_H
#define HERO_H

#include <QDialog>

namespace Ui {
class Hero;
}

class Hero : public QDialog
{
    Q_OBJECT

public:
    explicit Hero(QWidget *parent = nullptr);
    ~Hero();

private slots:

    void on_Select_hero_clicked();

    void on_label_hero_1_objectNameChanged(const QString &objectName);

private:
    Ui::Hero *ui;
};

#endif // HERO_H
