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
    type: ""
  }

  $scope.removeArg = function(index){
    $scope.addSurvey.args.splice(index, 1);
  }

  $scope.addArgument = function(addArg_){
    $scope.addSurvey.args.push(addArg_);
    $scope.addArg = {
      name: "",
      type: ""
    }
    // return true;
  }

  $scope.validateData = function(){
    if($scope.addSurvey.title === "" || $scope.addSurvey.picUrl === "" || $scope.addSurvey.args === []){
      return false;
    }
    return true;
  }

  $scope.argTypes = ['float', 'int']

  $scope.submitData = function(aS){
    if(aS.title === ""){
      return false;
    }
    else if(aS.picUrl === ""){
      return false;
    }
    var argsDict = {};
    // Begin to validate args
    $('.arg').each(function(ind, dom) {
      field = $(dom);
      argsDict[field.children().first().html()] = field.children().first().next().html();
    });
    // POST ML 
    $.post({
      url: "/ecsdee",
      cache: false,
      contentType: false,
      processData: false,
      data: {
        'file': new FormData($('#file')[0])
      },
      success: function(data) {
        // POST DATAS
        $.post({
          url: "/ecsdee2",
          data: {
            'title': $('#title').val(),
            'description': $('#description').val(),
            'picUrl': $('#image').val(),
            'args': argsDict
          },
          success: function(data) {
            console.log("Closing the loading dots that bae made <3");
          }
        });
      }
    })

    console.log(argsDict);
    return true;
  }

});
