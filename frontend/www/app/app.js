
'use strict'
angular.module('app', ["ui.router", "ui.bootstrap"])


/* -- service -- */

/* -- factory -- */

/* -- directive -- */

/* -- controller -- */
.controller("NavbarCtrl", ["$scope", function($scope){
    
}])
.controller("SignUpCtrl", ["$scope", function($scope){
    $scope.user= {}
    $scope.formDesign = {
        inputs: [
            {"label": "Name", "type": "text", "model": $scope.user.name},
            {"label": "Email", "type": "email", "model": $scope.user.email},
            {"label": "Password", "type": "password", "model": $scope.user.password},
        ],
        submit: function(){
            console.log($scope.user)
        },
        reset: function(){

        }
    }
}])
/* -- config -- */

// route config
.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {
    //
    $urlRouterProvider.otherwise("/home");
    //
    $stateProvider 
    .state('home', {
      url: "/home",
      templateUrl: "partials/home.html"
    })
    .state('signup', {
      url: "/signup",
      controller: "SignUpCtrl",
      templateUrl: "partials/signup.html"
    })
    .state('login', {
      url: "/login",
      templateUrl: "partials/login.html"
    })
}])



    