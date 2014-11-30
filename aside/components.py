__author__ = 'rizki'

import logging
import json

from PySide import QtCore, QtGui, QtWebKit

import hooks
import events

class PyBridge(QtCore.QObject):

    def __init__(self):
        super(PyBridge, self).__init__()

    @QtCore.Slot(str, str)
    def call(self, name, params):
        # convert string to object
        params = json.loads(params)
        return hooks.invoke(name, **params)


class WebPage(QtWebKit.QWebPage):
    """
    Makes it possible to use a Python logger to print javascript console messages
    """
    def __init__(self, logger=None, parent=None):
        super(WebPage, self).__init__(parent)
        if not logger:
            logger = logging
            logger.getLogger().setLevel(logging.INFO)
        self.logger = logger
        self.py_bridge = PyBridge()
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
        #self.loadFinished.connect(self.on_load_finished)
        self.loadStarted.connect(self.on_page_started)

    def javaScriptConsoleMessage(self, msg, lineNumber, sourceID):
        self.logger.info("JsConsole(%s:%d): %s" % (sourceID, lineNumber, msg))

    def on_page_started(self):
        frame = self.mainFrame()
        frame.addToJavaScriptWindowObject("py_bridge", self.py_bridge)
        for item in events.signal_items():
            frame.addToJavaScriptWindowObject(item[0], item[1])

    def on_load_finished(self, ok):
        if ok:
            frame = self.mainFrame()
            frame.addToJavaScriptWindowObject("py_bridge", self.py_bridge)
            for item in events.signal_items():
                frame.addToJavaScriptWindowObject(item[0], item[1])
