__author__ = 'rizki'

import logging

from PySide import QtCore, QtGui, QtWebKit

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

    def javaScriptConsoleMessage(self, msg, lineNumber, sourceID):
        self.logger.info("JsConsole(%s:%d): %s" % (sourceID, lineNumber, msg))
