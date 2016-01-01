__author__ = 'rizki'

import os
import urllib2

from bs4 import BeautifulSoup
from string import Template
import puremvc.patterns.proxy
import facade

PAGE_FILE_TYPE = "pageFileType"
PAGE_URL_TYPE = "pageURLType"

# Page register and retrieve


def _proxy():
    page_proxy = facade.AsideFacade.getInstance().retrieveProxy(PageProxy.NAME)
    if not page_proxy:
        facade.AsideFacade.getInstance().registerProxy(PageProxy())
        page_proxy = facade.AsideFacade.getInstance().retrieveProxy(PageProxy.NAME)
    return page_proxy


def register_file(name, page):
    _proxy().install(name, page, typ=PAGE_FILE_TYPE)


def register_url(name, page):
    _proxy().install(name, page, typ=PAGE_URL_TYPE)


def retrieve(name, **kwargs):
    content = None
    prefix = None
    if _proxy().page_type(name) == PAGE_FILE_TYPE:
        fullpath = _proxy().path(name)
        content = open(str(fullpath)).read()
        prefix = 'file:///'
    elif _proxy().page_type(name) == PAGE_URL_TYPE:
        fullpath = _proxy().path(name)
        response = urllib2.urlopen(fullpath)
        content = response.read()
        prefix = 'http://'

    if content:
        temp = Template(content)
        params = kwargs
        js_file = '{}/js/aside.js'.format(os.path.dirname(os.path.realpath(__file__)))
        if not ('ASIDE_JS' in params and params['ASIDE_JS']):
            params.update({'ASIDE_JS': js_file})
        content = temp.safe_substitute(**params)
        soup = BeautifulSoup(content)
        for tag in soup.find_all(type='text/ng-template'):
            if tag.name.strip() == "script" and "src" in tag.attrs:
                script = open(str(tag["src"])).read()
                tag.string = ''
                tag.string.replace_with(script)
        temp = Template(soup.prettify())
        content = temp.safe_substitute(**params)
        return '<!DOCTYPE html>\r\n%s' % unicode(content), prefix
    return '', prefix


class PageProxy(puremvc.patterns.proxy.Proxy):
    NAME = "PageProxy"
    pageList = {}

    def __init__(self):
        super(PageProxy, self).__init__(PageProxy.NAME, [])

    def install(self, name, page, typ=PAGE_FILE_TYPE):
        if typ == PAGE_URL_TYPE:
            value = {'fullpath': page, 'type': PAGE_URL_TYPE}
        else:
            value = {'fullpath': os.path.realpath(page), 'type': PAGE_FILE_TYPE}
        self.pageList[name] = value

    def path(self, name):
        return self.pageList[name]['fullpath'] if name in self.pageList else None

    def page_type(self, name):
        return self.pageList[name]['type'] if name in self.pageList else None
