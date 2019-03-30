var app = angular.module('bookings', []).config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrtoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CRSFToken';
});

function allLetters(word){
	var letters = /^[A-Za-z]+$/;
	if(word.match(letters)){
		return true;
	}else {
		return false;
	}
}

function ValidateEmail(inputText){
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(inputText.match(mailformat)){return true;}else{return false;}
}


function phonenumber(inputtxt){
	if (inputtxt.length==10){
		var phoneno = /^\(?([0-9]{10})\)?/
		if((inputtxt.match(phoneno))){
	      return true;
		} else{
			return false;
		}
	} else if (inputtxt.length == 13){
	  var phoneno = /^\(?([0-9]{4})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{3})$/;
	  if((inputtxt.match(phoneno))){
	      return true;
	        } else{
	        return false;
				}
	    } else{
	    	return false
	    }
}

function validator($scope, $rootScope){
	var validationArray = [];
	var valid;
	first_name = $scope.first_name;
	last_name = $scope.last_name;
	email = $scope.email;
	phone_number = $scope.phone_number;

	//first name
	if (!(first_name)){
		validationArray.push('Could I ask that you please fill in your first name?');
	}else{
		if (!(allLetters(first_name))){
				validationArray.push(
					"Please make sure your first name is made up of letters only. Robots haven't quite taken over yet...")
			}
	}
	//last name
	if (!(last_name)){
		validationArray.push('Could I ask that you please fill in your last name? Thanks!');
	}else{
		if (!(allLetters(last_name))){
				validationArray.push(
					"Please make sure your last name is made up of letters only. We're not all robots yet...")
			}
	}

	//email
	if (!(email)){
		validationArray.push("Could I ask that you please fill in your email address? My telepathic skils aren't up to sratch and I'd love to follow up.");
	}else{
		if (!(ValidateEmail(email))){
			validationArray.push("Please double check your email, I'd hate to be contacting the wrong person.")
		}
	}

	//phone number
	if (!(phone_number)){
		validationArray.push("Could I ask that you please fill in your phone number? I find it just makes it easier if all goes horribly and quick communication is needed.");
	
	}else{
		if (!(phonenumber(phone_number))){
			validationArray.push(
				"Terribly sorry, but my program only accepts the following phone number formats: XXXXXXXXXX or XXXX XXX XXX. Would you mind double checking what you gave me? It also helps if a phone number is made up of numbers.")
		}
	}
	if (validationArray!=0){
		$rootScope.error_array= validationArray;
		console.log($rootScope.error_array);
		return false;
	}else{
		return true;
	}
}



app.controller('bookingsController', function($scope, $http, $window, CSRF_TOKEN, $rootScope){
	$http.get('/meeting/api/meeting//').then(function(response){
		$rootScope.new_var = 'HEY';

		$scope.datesList = [];
		$scope.messageList = [];
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
		if (validator($scope, $rootScope)){
			$http({
		    method: 'patch',
		    url: '/meeting/api/meeting//' + String(id) + '/',
		    data: data,
		    headers: {
		    	'Content-Type': 'application/x-www-form-urlencoded',
		    	'X-CSRFToken' : CSRF_TOKEN,
		    }
			}).then(function successCallback(response) {
				console.log('success 2');
				$scope.messageList.push('success');

	       		$scope.bookingForm.$setPristine();
	       		$scope.bookingForm.$setSubmitted();
	       		$rootScope.new_var = 'HEY';
	       		$rootScope.$broadcast('success');
	       		//$location.path('YourRoute');
	    }, function errorCallback(response) {
   				$scope.messageList.push('submition error');



	});

		}else{
   			$scope.messageList.push('Validation error');
   			console.log('validation error');

		}

	}

	});
	
});
