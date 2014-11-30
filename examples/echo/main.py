__author__ = 'rizki'

import os
import sys

from PySide import QtCore, QtGui, QtWebKit
from ui import mainwindow
from aside import components, pages, hooks, events


def echo(inject=None, **kwargs):
    if 'message' in kwargs:
        message = kwargs['message']
        print 'Python: Got \'%s\' from Javascript' % message
        events.emit_signal('echo', message='pong')


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

    def __init__(self, parent=None):
        super(QtMainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        # default angular-side WebPage
        self.ui.webView.setPage(components.WebPage())
        self.ui.webView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.ui.webView.setHtml(pages.retrieve('index', current_path=current_path), "file:///")
        # center pos
        x, y, width, height = center_coord(QtGui.QApplication.desktop(), 640, 480)
        self.setGeometry(x, y, width, height)

    @staticmethod
    def web_settings():
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
    qt_app = QtGui.QApplication(sys.argv)

    pages.register_file('index', 'index.html')
    hooks.register_function('echo', echo, None)
    events.register_signal('echo')

    main = QtMainWindow()
    main.show()

    sys.exit(qt_app.exec_())
