#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "downloadlibrary.h"
#include "ui_downloadlibrary.h"

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


void MainWindow::on_pushButton_2_clicked()
{
	DownloadLibrary lib;
	lib.setModal(true);
	lib.exec();
}

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