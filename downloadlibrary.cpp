#include "downloadlibrary.h"
#include "ui_downloadlibrary.h"

DownloadLibrary::DownloadLibrary(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DownloadLibrary)
{
    ui->setupUi(this);
    ui->listWidget->addItem("Hi");
    ui->listWidget->addItem("H4i");
}

DownloadLibrary::~DownloadLibrary()
{
    delete ui;
}
