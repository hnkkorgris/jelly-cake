(function() {

  var app = angular.module("jelly-cake");
  
  var dbProvider = function($http) {
    
    var getStartScreen = function() {
      return $http.get("/start")
        .then(function(response) {
          return translateJsonResponse(response.data);
        });
    }

    // TODO: also remove redundant code
    var getNextScreen = function(id, opt) {
      return $http.get("/next/" + id + "/" + opt)
        .then(function(response) {
          return translateJsonResponse(response.data);
        });
    }

    var translateJsonResponse = function(json) {
        return angular.fromJson(json).screen;
    }
    
    return {
      getStartScreen: getStartScreen,
      getNextScreen: getNextScreen
    };
  };

  app.factory("dbProvider", dbProvider);
  
}());