angular.module('echoApp', ['echoApp.app']);
var echo_app = angular.module('echoApp.app', ['aside']);

echo_app.controller('echoCtrl', ["$scope", "hooks", "events", function($scope, hooks, events) {

    $scope.onEchoClick = function() {
        params = JSON.stringify({"message": "ping"});
        hooks.call('echo', params);
    };

    $scope.onEchoObjectClick = function() {
        params = JSON.stringify({"message": "ping"});
        hooks.call('echo_obj.receiver', params);
    };

    $scope.onEchoFuncDisable = function() {
        events.unbind('echo', $scope.echoFunc);
    };

    $scope.onPageRefresh = function() {
        params = "{}";
        hooks.call('refresh', params);
    };

    $scope.echoFunc = function(params) {
        obj_params = JSON.parse(params);
        console.log("Javascript Function: Got '" + obj_params.message + "' from Python" );
    };

    events.bind("echo", $scope.echoFunc);

}]);
