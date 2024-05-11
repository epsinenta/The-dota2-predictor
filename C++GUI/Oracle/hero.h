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

private:
    Ui::Hero *ui;
};

#endif // HERO_H
