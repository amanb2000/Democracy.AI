app.controller("control", function($scope, $interval) {
  $scope.test = "Heck world";

  $scope.addSurvey = {};
  $scope.addSurvey.title = "";
  $scope.addSurvey.description = "";
  $scope.addSurvey.picUrl = "";
  $scope.addSurvey.script = {};
  $scope.addSurvey.args = [];

  $scope.addArg = {
    name: "",
    type: "",
  }

  $scope.argTypes = ['float', 'int']

  $scope.validate = function(aS){
    if(aS.title === ""){
      return false;
    }
    else if(aS.picUrl === ""){
      return false;
    }
    return true;
  }

});
