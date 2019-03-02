var app = angular.module('bookings', []).config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrtoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CRSFToken';
});



app.controller('bookingsController', function($scope, $http, $window, CSRF_TOKEN, $rootScope){
	$http.get('/meeting/api/meeting//').then(function(response){
		$scope.datesList = [];
		for (var index = 0; index < response.data.length; index++){
			// creating a new dictionary for each object in the data set
			var meeting = {};
			//apending renamed data to meeting {}
			meeting.meetingEmail = response.data[index].email;
			meeting.meetingName = response.data[index].name;
			meeting.meetingPhone_Number = response.data[index].phone_number;
			meeting.meetingDay_Time = response.data[index].day_time;
			meeting.id = response.data[index].id;
			meeting.meetingDay_Time_id = response.data[index].day_time + "T" + (response.data[index].id)
			if (!(meeting.meetingEmai || meeting.meetingName || meeting.meetingPhone_Number)){
				$scope.datesList.push(meeting)
			}
		}
		//console.log($scope.datesList);


	$scope.saveBooking = function(){
		var	day_time = $scope.date + 'T' + $scope.time + "Z";
		var id = $window._date_id;
		console.log(id);

		//puts to link, data = data you're passing to api
		var data = {
			id: id,
			name: $scope.first_name + ' ' + $scope.last_name, 
			email: $scope.email,
			phone_number: $scope.phone_number,
			//day_time: day_time,
			csrfmiddlewaretoken: CSRF_TOKEN,
		};
		//console.log(data);
		//${data.id};
		$http({
	    method: 'patch',
	    url: '/meeting/api/meeting//' + String(id) + '/',
	    data: data,
	    headers: {
	    	'Content-Type': 'application/x-www-form-urlencoded',
	    	'X-CSRFToken' : CSRF_TOKEN,
	    }
		}).then(function successCallback(response) {
       		$rootScope.success_message= 'Success'; 
            //$location.path('YourRoute');


    }, function errorCallback(response) {
       $rootScope.error_message= 'Error';

});
	}

	});
	
});
