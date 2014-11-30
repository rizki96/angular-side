__author__ = 'rizki'

from PySide import QtCore, QtGui, QtWebKit
from ui import main, web_form
from aside import components


def center_coord(parent, width=640, height=480):
    desktop = parent
    screen_width = desktop.width()
    screen_height = desktop.height()
    if width > screen_width:
        width = screen_width
    if height > screen_height:
        height = screen_height
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2
    return x, y, width, height


class QtMainWindow(QtGui.QMainWindow):

    widget = {}
    form_ui = None

    def __init__(self, parent=None):
        super(QtMainWindow, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.create_form(), QtCore.Qt.FramelessWindowHint)
        x, y, width, height = center_coord(QtGui.QApplication.desktop(), 1024, 768)
        self.setGeometry(x, y, width, height)

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

