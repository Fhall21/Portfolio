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

	var stripe_pk = $('#stripe_pk').text()
	if (!(stripe_pk)){
		$('#stripe_button').addClass('disabled');
		$('#stripe_button').addClass('bg-secondary');
		$('#stripe_button').text('Please refresh the page')
		$('#payment_success_banner').removeClass('vanished');

	}
	
	//replaceWith(function(){
});

$('#id_amount_paid').change(function(){
	var old_hourly_rate = $('#hourly_rate').val()
	var hourly_rate =  Math.round(($('#id_amount_paid').val()/12)*2) /2
	var new_payment_breakdown_txt = $('#payment_breakdown').text().replace(old_hourly_rate, hourly_rate);
	$('#payment_breakdown').text(new_payment_breakdown_txt);
	$('#hourly_rate').val(hourly_rate);

});

$('#stripe_button').click(function(){

	
	if ($('#stripe_button').hasClass('disabled')){
		window.location.href=window.location.href
		// history.go(0)
		// location.reload(true);
	} 

	var stripe_pk = $('#stripe_pk').text()
	var token = function(res){
		var $id = $('<input type=hidden name=stripeToken />').val(res.id);
		var $email = $('<input type=hidden name=stripeEmail />').val(res.email);
		$('a').bind("click", function() { return false; });
	    $('button').addClass('disabled');
		$('#stripe_button').addClass('bg-secondary');
		$('#stripe_button').text('Please refresh the page');
	    // handler.open({closed : function(){$('#stripe_button').html('loading')}})
		$('#StripeForm').append($id).append($email).submit();
	};
	var amount = ($('#id_amount_paid').val() * 100) 
		// alert(amount)
	// Stripe.setPublishableKey(stripe_pk);
	StripeCheckout.open({
		key: stripe_pk,
		amount: amount,
		name: 'Python Course',
		description: 'Felix Hall Beginner Python Course',
		panelLabel: 'Checkout',
		currency: 'AUD',
		token: token
	});
	// ladda_instance.stopAll()
	return false;
});

//animation
$('.has-animation').each(function(index) {
  		if($(window).scrollTop() + $(window).height() > $(this).offset().top + $(this).outerHeight() ){ 
  			$(this).delay($(this).data('delay')).queue(function(){
      			$(this).addClass('animate-in');
    		});    
  		}   
	});  


$(window).scroll(function() { 
	$('.has-animation').each(function(index) {
  		if($(window).scrollTop() + $(window).height() > $(this).offset().top ){ 
  			$(this).delay($(this).data('delay')).queue(function(){
      			$(this).addClass('animate-in');
    		});    
  		}   
	});   
});
