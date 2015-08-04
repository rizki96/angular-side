(function () { // workaround for pouchdb in phantom.js
  'use strict';
  // minimal polyfill for phantomjs; in the future, we should do ES5_SHIM=true like pouchdb
  if (!Function.prototype.bind) {
    Function.prototype.bind = function (oThis) {
      if (typeof this !== "function") {
        // closest thing possible to the ECMAScript 5
        // internal IsCallable function
        throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");
      }

      var aArgs = Array.prototype.slice.call(arguments, 1),
          fToBind = this,
          fNOP = function () {},
          fBound = function () {
            return fToBind.apply(this instanceof fNOP && oThis
                   ? this
                   : oThis,
                   aArgs.concat(Array.prototype.slice.call(arguments)));
          };

      fNOP.prototype = this.prototype;
      fBound.prototype = new fNOP();

      return fBound;
    };
  }

})();

angular.module('aside', ['aside.hooks', 'aside.events']);

angular.module('aside.hooks', [])
.service('asideHooks', function($q, $timeout) {
    var call_hooks = function(name, params) {
        try {
            var bridge = eval("py_bridge");
            bridge.call(name, params);
            var retval = eval("window.py_result");
            return retval;
        } catch (e) {
            if (e instanceof SyntaxError) {
            }
        }
        $timeout(function() {call_hooks(name, params)}, 500);
    };

    var promise_hooks = function(name, params) {
        var deferred = $q.defer();

        try {
            var bridge = eval("py_bridge");
            bridge.call(name, params);
        } catch (e) {
            if (e instanceof SyntaxError) {
                deferred.reject({error: "promise_hooks call syntax error"});
            } else {
                deferred.reject({error: "promise_hooks call unknown error"});
            }
        }
        $timeout(function() { var retval = eval("window.py_result"); deferred.resolve(retval); }, 500);

        return deferred.promise;
    }

    return {
        call: function(name, params) {
            return call_hooks(name, params);
        },
        promise: function(name, params) {
            return promise_hooks(name, params);
        }
    };
});

angular.module('aside.events', [])
.service('asideEvents', function($timeout) {

    var connect_event = function(name, func) {
        try {
            var sig = eval(name); // eval mungkin harus diganti
            if (sig !== undefined) {
                sig.py_event.connect(func);
                return;
            }
        } catch (e) {
            if (e instanceof SyntaxError) {
            }
        }
        $timeout(function() {connect_event(name, func)}, 500);
    };

    var disconnect_event = function(name, func) {
        var sig = eval(name); // eval mungkin harus diganti
        if (sig !== undefined) {
            sig.py_event.disconnect(func);
        }
    };

    return {
        bind: function(name, func) {
            if (func === undefined)
                console.log('func undefined');
            connect_event(name, func);
        },
        unbind: function(name, func) {
            if (func === undefined)
                console.log('func undefined');
            disconnect_event(name, func);
        }
    };
});
