#include "downloadlibrary.h"
#include "ui_downloadlibrary.h"

DownloadLibrary::DownloadLibrary(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DownloadLibrary)
{
    ui->setupUi(this);

}

DownloadLibrary::~DownloadLibrary()
{
    delete ui;
}
