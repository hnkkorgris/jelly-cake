(function() {

  var app = angular.module("jelly-cake");

  var GameCtrl = function($scope, $http) {

    // TODO: maybe move this to a service
    var loadCurrentScreen = function($http) {
      return $http.get("/currentScreen")
        .then(function(response) {
          var jsonResponse = angular.fromJson(response.data);
          return jsonResponse.screen;
        });
    }

    // TODO: same with this, and also remove redundant code
    var loadNextScreen = function($http, id, opt) {
      return $http.get("/nextScreen/" + id + "/" + opt)
        .then(function(response) {
          var jsonResponse = angular.fromJson(response.data);
          return jsonResponse.screen;
        });
    }

    var populateScreen = function(screen) {
      $scope.id = screen.key;
      $scope.question = screen.text;
      $scope.ans1 = screen.navs[0];
      $scope.ans2 = screen.navs[1];
      $scope.ans3 = screen.navs[2];
    }

    $scope.navigate = function(opt) {
      loadNextScreen($http, $scope.id, opt)
        .then(function(response) {
          populateScreen(response);
        })
    }

    loadCurrentScreen($http).then(function(response) {
      populateScreen(response)
    })
  }

  app.controller("GameCtrl", GameCtrl);

})();