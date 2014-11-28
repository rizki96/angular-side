__author__ = 'rizki'

from PySide import QtCore, QtGui, QtWebKit
from ui import main, web_form
from aside import components

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

    widget = {}

    def __init__(self, parent=None):
        super(QtMainWindow, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.create_form(), QtCore.Qt.FramelessWindowHint)
        x, y, WIDHT, HEIGHT = centerCoord(QtGui.QApplication.desktop(), 1024, 768)
        self.setGeometry(x, y, WIDHT, HEIGHT)


    def create_form(self):
        self.form_ui = web_form.Ui_WebForm()
        form_widget = QtGui.QWidget()
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
        self.form_ui.setupUi(form_widget)
        self.form_ui.webView.setPage(components.WebPage())
        return form_widget

