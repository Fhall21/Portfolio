var app = angular.module('bookings', []).config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrtoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CRSFToken';
});

function allLetters(word){
	var letters = /^[A-Za-z]+$/;
	if(word.value.match(letters)){
		return true;
	}
	else{
		alert("message");
		return false;
	}
}

function ValidateEmail(inputText){
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(inputText.value.match(mailformat)){
		return true;
	}else{
		return false;
	}
}


function phonenumber(inputtxt)
{
	if (inputtxt.length==10){
		var phoneno = /^\(?([0-9]{10})\)?/
		if((inputtxt.value.match(phoneno))){
	      return true;
		} else{
			return false;
		}
	} else if (inputtxt.length == 13){
	  var phoneno = /^\(?([0-9]{4})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{3})$/;
	  if((inputtxt.value.match(phoneno))){
	      return true;
	        } else{
	        return false;
				}
	    } else{
	    	return false
	    }
}

function validator($scope){
	var validationArray = [];
	var valid;
	first_name = $scope.first_name;
	last_name = $scope.last_name;
	email = $scope.email;
	phone_number = $scope.phone_number;

	//checking if a field is empy
	var inputArray = [first_name, last_name, email, phone_number]

	for (i = 0; i < inputArray.length; i++){
		if (!(inputArray[i])){
			validationArray.pop(
				'You forgot to fill in your ' + inputArray[i])
		}
	} else{
	//if they are not empty:
		//checking if name fields are only letters
		if (!(allLetters(first_name))){
				validationArray.pop(
					'Please make sure your first name is made up of letters only.')
			}
		if (!(allLetters(last_name))){
				validationArray.pop(
					'Please make sure your last name is made up of letters only.')
			}
		if (!(ValidateEmail(email))){
			validationArray.pop('Please double check your email.')
		}

		if (!(phonenumber(phone_number))){
			validationArray.pop(
				'Please double check your email. Accepted formats are XXXXXXXXXX or XXXX XXX XXX')
		}


	}


}



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
			if (!(meeting.meetingEmail || meeting.meetingName || meeting.meetingPhone_Number)){
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
