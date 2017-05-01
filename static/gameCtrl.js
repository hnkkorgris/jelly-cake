(function() {

  var app = angular.module("jelly-cake");

  var GameCtrl = function($scope, dbProvider) {

    var populateScreen = function(screen) {
      $scope.id = screen.key;
      $scope.question = screen.text;
      $scope.ans1 = screen.navs[0];
      $scope.ans2 = screen.navs[1];
      $scope.ans3 = screen.navs[2];
    }

    $scope.navigate = function(opt) {
      dbProvider.getNextScreen($scope.id, opt)
        .then(function(response) {
          populateScreen(response);
        })
    }

    $scope.reset = function() {
      dbProvider.getStartScreen()
        .then(function(response) {
          console.log("Here");
          populateScreen(response);
      })
    }

    $scope.reset();
  }

  app.controller("GameCtrl", GameCtrl);

})();