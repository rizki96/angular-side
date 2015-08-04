__author__ = 'rizki'

import puremvc.patterns.proxy

import facade

HOOK_OBJECT_TYPE = "hookObjectType"
HOOK_FUNCTION_TYPE = "hookFunctionType"


def register_function(name, func, inject):
    _proxy().install(name, func, typ=HOOK_FUNCTION_TYPE, inject=inject)


def register_object(name, obj):
    _proxy().install(name, obj, typ=HOOK_OBJECT_TYPE)


def invoke(name, **kwargs):
    return _proxy().invoke(name, **kwargs)


def _proxy():
    hook_proxy = facade.AsideFacade.getInstance().retrieveProxy(HookProxy.NAME)
    if not hook_proxy:
        facade.AsideFacade.getInstance().registerProxy(HookProxy())
        hook_proxy = facade.AsideFacade.getInstance().retrieveProxy(HookProxy.NAME)
    return hook_proxy


class HookProxy(puremvc.patterns.proxy.Proxy):
    NAME = "HookProxy"
    hooks = {}

    def __init__(self):
        super(HookProxy, self).__init__(HookProxy.NAME, [])

    def install(self, name, func_obj, typ=None, inject=None):
        self.hooks[name] = {"hook": func_obj, "type": typ, "inject": inject}

    def invoke(self, name, **kwargs):
        if self.get_type(name) == HOOK_FUNCTION_TYPE:
            if name in self.hooks:
                kwargs.update({'inject': self.hooks[name]['inject']})
                return self.hooks[name]['hook'](**kwargs)
        else:
            try:
                obj, method = name.split(".")
                if obj in self.hooks and self.get_type(obj) == HOOK_OBJECT_TYPE:
                    func = getattr(self.hooks[obj]['hook'], method)
                    return func(**kwargs)
            except ValueError:
                pass
        return None

    def get_type(self, name):
        if name in self.hooks:
            return self.hooks[name]['type']
        return None