//
  // For any unmatched url, redirect to /state1
  // $urlRouterProvider.otherwise("/home");
  //
  // Now set up the states
  // $stateProvider 
  //   .state('state1', {
  //     url: "/state1",
  //     templateUrl: "partials/state1.html"
  //   })
  // $stateProvider 
  //   .state('state1', {
  //     url: "/state1",
  //     templateUrl: "partials/state1.html"
  //   })
  //   .state('state1.list', {
  //     url: "/list",
  //     templateUrl: "partials/state1.list.html",
  //     controller: function($scope) {
  //       $scope.items = ["A", "List", "Of", "Items"];
  //     }
  //   })
  //   .state('state2', {
  //     url: "/state2",
  //     templateUrl: "partials/state2.html"
  //   })
  //   .state('state2.list', {
  //     url: "/list",
  //     templateUrl: "partials/state2.list.html",
  //     controller: function($scope) {
  //       $scope.things = ["A", "Set", "Of", "Things"];
  //     }
  //   });
}]);















/*

var myapp = angular.module('app', ["ui.router"])
    .factory("jwtToken", function jwtToken(){
        return {
          isLogged: false,
          changeStatus: function(value){
            //angular.copy(this.isLogged, value);
            this.isLogged = value;
          },
          setToken: function(new_token){
            window.localStorage.setItem("auth_token", new_token);
            this.changeStatus(true);
          },
          clearToken: function(){
            window.localStorage.clear("auth_token")
            this.changeStatus(false);
          }

        }
      })
    .factory("MyAuth", [ "$http", "jwtToken",function MyAuth($http, jwtToken){
        return {
            login: function(credentials) {
              var login = $http.post('http://localhost:5000/authenticate', credentials);
              login.success(function(result) {
                //window.localStorage.setItem('auth_token', result.token);
                jwtToken.setToken(result.token);
              });
              return login;
            },
            logout: function() {
              // The backend doesn't care about logouts, delete the token and you're good to go.
              // window.localStorage.clear('auth_token');
              jwtToken.clearToken();
            },
        }
    }])
    .controller("HomeCtrl", ["MyAuth", "$scope", "$http", "jwtToken", function HomeCtrl(MyAuth, $scope, $http, jwtToken){
        var auth = MyAuth;
        $scope.user = {};
        $scope.login = function(){
            auth.login($scope.user)
        }
        $scope.debug = function(){
            console.info($scope.user);
        }
        $scope.getDetails = function(){
          $http.get("http://localhost:5000/me")
          .success(function(data){
            $scope.details = data;
          })
        }
        $scope.logout = function(){
          auth.logout();
        }
        $scope.token = jwtToken;

    }])
    .config(['$httpProvider', function($httpProvider) {
      $httpProvider.interceptors.push(["$q", "jwtToken", function($q, jwtToken){
          return {
            request: function(config) {
              var token;
              if (window.localStorage.getItem('auth_token')) {
                token = window.localStorage.getItem('auth_token');
              }
              if (token) {
                config.headers.Authorization = 'Bearer ' + token;
              }
              return config;
            },
            responseError: function(response) {
              if (response.status === 401 || response.status === 403 || response.status === 400) {
                // window.localStorage.clear('auth_token');
                // $injector.get('$state').go('anon.login');
                jwtToken.clearToken();
              }
              return $q.reject(response);
            }
          }
      }])
    }])
    .config(function($stateProvider, $urlRouterProvider) {
      //
      // For any unmatched url, redirect to /state1
      $urlRouterProvider.otherwise("/state1");
      //
      // Now set up the states
      $stateProvider
        .state('state1', {
          url: "/state1",
          templateUrl: "partials/state1.html"
        })
        .state('state1.list', {
          url: "/list",
          templateUrl: "partials/state1.list.html",
          controller: function($scope) {
            $scope.items = ["A", "List", "Of", "Items"];
          }
        })
        .state('state2', {
          url: "/state2",
          templateUrl: "partials/state2.html"
        })
        .state('state2.list', {
          url: "/list",
          templateUrl: "partials/state2.list.html",
          controller: function($scope) {
            $scope.things = ["A", "Set", "Of", "Things"];
          }
        });
    });
*/