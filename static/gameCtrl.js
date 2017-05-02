(function() {

  var app = angular.module("jelly-cake");

  var GameCtrl = function($scope, $filter, dbProvider) {

    var populateScreen = function(screen) {
      $scope.id = screen.key;
      $scope.question = screen.text;
      $scope.ans1 = screen.navs[0];
      $scope.ans2 = screen.navs[1];
      $scope.ans3 = screen.navs[2];

      $scope.fg = generateUrl(getAsset($filter, screen.assets, "fg").path);
      $scope.bg = generateUrl(getAsset($filter, screen.assets, "bg").path);
    }

    var generateUrl = function(relPath) {
      return "url(/static/assets/" + relPath + ")";
    }

    var getAsset = function($filter, list, search) {
      console.log(list);
      return $filter('filter')(list, {'type': search})[0];
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
          populateScreen(response);
      })
    }

    $scope.reset();
  }

  app.controller("GameCtrl", GameCtrl);

})();