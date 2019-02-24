var app = angular.module('bookings', []).config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrtoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CRSFToken'
});

app.controller('meetingController', function($scope, $http){
	$http.get('/meeting/api/meeting/').then(function(response){
		$scope.datesList = [];
		for (var index = 0; index < response.date.length; index++){
			// creating a new dictionary for each object in the data set
			var meeting = {};
			//apending renamed data to meeting {}
			meeting.meetingEmail = response.data[index].email;
			meeting.meetingName = response.data[index].name;
			meeting.meetingPhone_Number = response.data[index].phone_number;
			meeting.meetingDay_Time = response.data[index].day_time;
			meeting.id = response.data[index].id;
			$scope.datesList.push(meeting)
		}
	});

	$scope.saveBooking = function(){
		//puts to link, data = data you're passing to api
		var data = {
			name: $scope.meetingNameInput, 
			email: $scope.meetingEmailInput,
			phone_number: $scope.meetingPhone_NumberInput
			day_time: $scope.meetingDay_TimeInput
		}		
		$http.put
	}

})