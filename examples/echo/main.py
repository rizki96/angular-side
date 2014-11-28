__author__ = 'rizki'

import sys

from PySide import QtCore, QtGui, QtWebKit
from ui import mainwindow
from aside import components, pages, hooks, events

def centerCoord(parent, WIDTH=640, HEIGHT=480):
    desktop = parent
    screen_width = desktop.width()
    screen_height = desktop.height()
    if WIDTH > screen_width: WIDTH = screen_width
    if HEIGHT > screen_height: HEIGHT = screen_height
    x = (screen_width - WIDTH) / 2
    y = (screen_height - HEIGHT) / 2
    return (x,y,WIDTH,HEIGHT)


class QtMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(QtMainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        # default angular-side WebPage
        self.ui.webView.setPage(components.WebPage())
        self.ui.webView.setHtml(pages.retrieve('index'))
        self.web_settings()
        # center pos
        x, y, WIDHT, HEIGHT = centerCoord(QtGui.QApplication.desktop(), 800, 600)
        self.setGeometry(x, y, WIDHT, HEIGHT)

    def web_settings(self):
        for attr in [
                QtWebKit.QWebSettings.AutoLoadImages,
                QtWebKit.QWebSettings.JavascriptEnabled,
                QtWebKit.QWebSettings.JavaEnabled,
                QtWebKit.QWebSettings.PluginsEnabled,
                QtWebKit.QWebSettings.JavascriptCanOpenWindows,
                QtWebKit.QWebSettings.JavascriptCanAccessClipboard,
                QtWebKit.QWebSettings.DeveloperExtrasEnabled,
                QtWebKit.QWebSettings.SpatialNavigationEnabled,
                QtWebKit.QWebSettings.OfflineStorageDatabaseEnabled,
                QtWebKit.QWebSettings.OfflineWebApplicationCacheEnabled,
                QtWebKit.QWebSettings.LocalStorageEnabled,
                QtWebKit.QWebSettings.LocalStorageDatabaseEnabled,
                QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls,
                QtWebKit.QWebSettings.LocalContentCanAccessFileUrls,
            ]:
            QtWebKit.QWebSettings.globalSettings().setAttribute(attr, True)

if __name__ == '__main__':
    qtapp = QtGui.QApplication(sys.argv)

    pages.register_file('index', 'index.html')

    main = QtMainWindow()
    main.show()

    sys.exit(qtapp.exec_())
