(function() {

  var app = angular.module("jelly-cake");

  var GameCtrl = function($scope, $http) {
    
    var getCurrentScreen = function($http) {

      return $http.get("/currentScreen")
        .then(function(response) {
          $scope.q = response.q;
          $scope.a1 = response.a1;
          $scope.a2 = response.a2;
          $scope.a3 = response.a3;
        });
    }

     $scope.q = "Help";
    // $scope.a1 = "Answer 1";
    // $scope.a2 = "Answer 2";
    // $scope.a3 = "Answer 3";
    getCurrentScreen($http);
  }

  app.controller("GameCtrl", GameCtrl);

})();