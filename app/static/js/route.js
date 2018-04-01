var webApp=angular.module('NewsApp', ["ui.router"]);
webApp.controller('loginController', ['$scope', function($scope){
	console.log('this is login l');
}]);
webApp.controller('signupController', ['$scope', function($scope){
    console.log('this is login s');
}]);
webApp.controller('menuController', ['$scope', function($scope){
    console.log('this is login m');
}]);
webApp.config(['$stateProvider','$urlRouterProvider','$locationProvider',function($stateProvider,$urlRouteProvider,$locationProvider) {
	// $locationProvider.hashPrefix('');
    $locationProvider.html5Mode(true)
    $urlRouteProvider.otherwise('/menu');
	// .when('/login',{
	// 	templateUrl:'./pages/login.html',
	// 	controller:'loginController'
	// })
 //    .when('/signup',{
 //        templateUrl:'./pages/signup.html',
 //        controller:'signupController'
 //    })
	// .when('/user',{
	// 	templateUrl:'./pages/userview.html',
 //        controller:'userController'
	// })
    $stateProvider 
    .state('login',{
        url:'/login',
        views:{
            "main":{
                templateUrl:'login'
            }
        }
    })
    .state('signup',{
        url:'/signup',
         views:{
            "main":{
                templateUrl:'signup'
            }
        }
    })
    .state('menu',{
        url:'/menu',
        // templateUrl:''
    })
    .state('menu.mainland',{
        url:'/mainland',
        templateUrl:'menu/mainland'
    })
    .state('menu.one',{
        url:'/newscontent',
        templateUrl:'menu/newscontent'
    })

}]);