$(function(){
	$('#id_is_student, #id_student_keen').removeClass("form-control")
	$('#id_is_student, #id_student_keen div').css({'justify-self': 'center'});
	$('#hourly_rate').val('10');

	//slick
	$('.slick-carousel').slick({
    slidesToShow: 1,
    fade: true,
    autoplay: true,
    autoplaySpeed: 5000,
    pauseOnHover: false,
    });
	
	//replaceWith(function(){
});

$('#id_amount_paid').change(function(){
	var old_hourly_rate = $('#hourly_rate').val()
	console.log(old_hourly_rate);
	var hourly_rate =  Math.round(($('#id_amount_paid').val()/12)*2) /2
	var new_payment_breakdown_txt = $('#payment_breakdown').text().replace(old_hourly_rate, hourly_rate);
	console.log(new_payment_breakdown_txt);
	$('#payment_breakdown').text(new_payment_breakdown_txt);
	$('#hourly_rate').val(hourly_rate);

});

$('#stripe_button').click(function(){
	var token = function(res){
		var $id = $('<input type=hidden name=stripeToken />').val(res.id);
		var $email = $('<input type=hidden name=stripeEmail />').val(res.email);
		$('a').bind("click", function() { return false; });
	    $('button').addClass('disabled');
	    handler.open({closed : function(){$('#stripe_button').html('loading')}})
	// alert('here')
		$('#StripeForm').append($id).append($email).submit();
	};
	var amount = ($('#id_amount_paid').val() * 100) 
		// alert(amount)
	StripeCheckout.open({
		key: '{{ key }}',
		address: false,
		amount: amount,
		name: 'Coding Workshop',
		description: 'Register to Coding Workshop',
		panelLabel: 'Checkout',
		currency: 'AUD',
		token: token
	});
	ladda_instance.stopAll()
	return false;
});