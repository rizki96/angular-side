__author__ = 'rizki'

import json
from PySide import QtCore
import puremvc.patterns.proxy

import facade


def register_signal(name):
    _proxy().install(name)


def retrieve_signal(name):
    proxy = _proxy()
    return proxy.events[name] if name in proxy.events else None


def emit_signal(name, **kwargs):
    _proxy().emit_signal(name, **kwargs)


def signal_items():
    return _proxy().events.iteritems()


def _proxy():
    event_proxy = facade.AsideFacade.getInstance().retrieveProxy(EventProxy.NAME)
    if not event_proxy:
        facade.AsideFacade.getInstance().registerProxy(EventProxy())
        event_proxy = facade.AsideFacade.getInstance().retrieveProxy(EventProxy.NAME)
    return event_proxy


class PyEvent(QtCore.QObject):

    py_event = QtCore.Signal(str)

    def __init__(self):
        super(PyEvent, self).__init__()


class EventProxy(puremvc.patterns.proxy.Proxy):
    NAME = "EventProxy"
    events = {}

    def __init__(self):
        super(EventProxy, self).__init__(EventProxy.NAME, [])

    def install(self, name):
        self.events[name] = PyEvent()

    def emit_signal(self, name, **kwargs):
        params = json.dumps(kwargs)
        self.events[name].py_event.emit(params)
