(function() {

  var app = angular.module("jelly-cake");

  var GameCtrl = function($scope, $http) {

    var loadCurrentScreen = function($http) {

      return $http.get("/currentScreen")
        .then(function(response) {
          var jsonResponse = angular.fromJson(response.data);
          return jsonResponse.screen;
        });
    }

    loadCurrentScreen($http).then(function(response) {
      $scope.question = response.text
      $scope.ans1 = response.navs[0].text
      $scope.ans2 = response.navs[1].text
      $scope.ans3 = response.navs[2].text
    })
  }

  app.controller("GameCtrl", GameCtrl);

})();