#ifndef DOWNLOADLIBRARY_H
#define DOWNLOADLIBRARY_H

#include <QDialog>

namespace Ui {
class DownloadLibrary;
}

class DownloadLibrary : public QDialog
{
    Q_OBJECT

public:
    explicit DownloadLibrary(QWidget *parent = nullptr);
    ~DownloadLibrary();

private:
    Ui::DownloadLibrary *ui;
};

#endif // DOWNLOADLIBRARY_H
