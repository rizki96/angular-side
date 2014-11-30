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
.service('hooks', function() {
    return {
        call: function(name, params) {
            return py_bridge.call(name, params);
        }
    };
});

angular.module('aside.events', [])
.service('events', function() {
    return {
        bind: function(name, func) {
            if (func === undefined)
                console.log('func undefined');
            var sig = eval(name); // eval mungkin harus diganti
            sig.py_event.connect(func);
        }
    };
});
