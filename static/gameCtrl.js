(function() {

  var app = angular.module("jelly-cake");

  var GameCtrl = function($scope, $http) {
    
    var loadCurrentScreen = function($http) {

      return $http.get("/currentScreen")
        .then(function(response) {
          var jsonResponse = angular.fromJson(response.data);
          $scope.currentScreen = jsonResponse;
        });
    }

    loadCurrentScreen($http);
  }

  app.controller("GameCtrl", GameCtrl);

})();