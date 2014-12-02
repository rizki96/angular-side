angular.module('echoApp', ['echoApp.app']);
var echo_app = angular.module('echoApp.app', ['aside']);

echo_app.controller('echoCtrl', ["$scope", "asideHooks", "asideEvents", function($scope, asideHooks, asideEvents) {

    $scope.onEchoClick = function() {
        params = JSON.stringify({"message": "ping"});
        asideHooks.call('echo', params);
    };

    $scope.onEchoObjectClick = function() {
        params = JSON.stringify({"message": "ping"});
        asideHooks.call('echo_obj.receiver', params);
    };

    $scope.onEchoFuncDisable = function() {
        asideEvents.unbind('echo', $scope.echoFunc);
    };

    $scope.onPageRefresh = function() {
        params = "{}";
        asideHooks.call('refresh', params);
    };

    $scope.echoFunc = function(params) {
        obj_params = JSON.parse(params);
        console.log("Javascript Function: Got '" + obj_params.message + "' from Python" );
    };

    asideEvents.bind("echo", $scope.echoFunc);

}]);
