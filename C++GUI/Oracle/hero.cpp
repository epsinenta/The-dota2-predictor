#include "hero.h"
#include "ui_hero.h"
#include "widget_initializer.h"
#include <QPixmap>
#include <QScreen>
Hero::Hero(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Hero)
{
    ui->setupUi(this);
    std::vector<QComboBox*> heroes_menu = {ui->team1_hero1_select_menu, ui->team1_hero2_select_menu, ui->team1_hero3_select_menu, ui->team1_hero4_select_menu, ui->team1_hero5_select_menu, ui->team2_hero1_select_menu, ui->team2_hero2_select_menu, ui->team2_hero3_select_menu, ui->team2_hero4_select_menu, ui->team2_hero5_select_menu};
    WidgetInitializer().initHeroesMenu(heroes_menu);
    QScreen *screen = QGuiApplication::primaryScreen();
    QRect screenGeometry = screen->geometry();

    int newWidth = screenGeometry.width();
    int newHeight = screenGeometry.height();
    resize(newWidth, newHeight);
}

Hero::~Hero()
{
    delete ui;
}

void Hero::on_Select_hero_clicked()
{
    QPixmap first_hero(":/image_oracle/heroes_png/Mirana_minimap_icon.png");
    int w = ui->hero1->width();
    int h = ui->hero1->height();
    ui->hero1->setPixmap(first_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap second_hero(":/image_oracle/heroes_png/Shadow_Shaman_minimap_icon.png");
    w = ui->hero2->width();
    h = ui->hero2->height();
    ui->hero2->setPixmap(second_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap third_hero(":/image_oracle/heroes_png/Weaver_minimap_icon.png");
    w = ui->hero3->width();
    h = ui->hero3->height();
    ui->hero3->setPixmap(third_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap fouth_hero(":/image_oracle/heroes_png/Doom_minimap_icon.png");
    w = ui->hero4->width();
    h = ui->hero4->height();
    ui->hero4->setPixmap(fouth_hero.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap fifth_hero(":/image_oracle/heroes_png/Arc_Warden_minimap_icon.png");
    w = ui->hero5->width();
    h = ui->hero5->height();
    ui->hero5->setPixmap(fifth_hero.scaled(w,h,Qt::KeepAspectRatio));
}
