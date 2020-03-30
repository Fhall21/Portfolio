function display_stripe_btn() {
	var name_review_comment_display = $('#name_review_comment').css('display')
	var price_review_comment_display = $('#price_review_comment').css('display')
	if ((name_review_comment_display == 'none') && (price_review_comment_display == 'none')){
		$('#stripe_button').show();
	} else{
		$('#stripe_button').hide();
	}
}
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

	$('.slick-carousel-words').slick({
	arrows: false,
	swipe: false,
    slidesToShow: 1,
    slidesToScroll:1,
    // fade: true,
    autoplay: true,
    autoplaySpeed: 2000,
    pauseOnHover: false,
    });

    $('.slick-carousel-icons').slick({
	arrows: false,
    slidesToShow: 1,
    slidesToScroll:1,
    // fade: true,
    autoplay: true,
    autoplaySpeed: 4000,
    pauseOnHover: false,
    });

    //form validation
    // function validate_form(this) {
    // 	this.validate({
    // 		rules: {
    // 			amount_paid: {
    // 				required: true,
    // 				min: 20
    // 			},
    // 			first_name
    // 		}
    // 	})
    // }

 //    $('#StripeForm').validate({
	// 	rules: {
 //    			amount_paid: {
 //    				required: true,
 //    				min: 20
 //    			}
 //    		}
	// })



	var stripe_pk = $('#stripe_pk').text()
	if (!(stripe_pk)){
		$('#stripe_button').addClass('disabled');
		$('#stripe_button').addClass('bg-secondary');
		$('#stripe_button').text('Ahh... Stripe was not ready, please refresh the page')
		// $('#payment_success_banner').removeClass('vanished');
	}
	$('#name_review_comment').hide()
	$('#price_review_comment').hide()

	if (($('#id_first_name').val().length < 1) || ($('#id_last_name').val().length < 1)){
		$('#stripe_button').hide();
		$('#name_review_comment').show();
	}

	
	//replaceWith(function(){
});

$('#id_amount_paid').change(function(){
	var old_hourly_rate = $('#hourly_rate').val()
	var hourly_rate =  Math.round(($('#id_amount_paid').val()/12)*2) /2
	var new_payment_breakdown_txt = $('#payment_breakdown').text().replace(old_hourly_rate, hourly_rate);
	$('#payment_breakdown').text(new_payment_breakdown_txt);
	$('#hourly_rate').val(hourly_rate);
	if ($('#id_amount_paid').val() < 0.99){
		// alert('yess!')
		$('#id_amount_paid').popover("toggle");
		$('#price_review_comment').show()

		// $('#stripe_button').hide()
		// $('#stripe_button').off('click');
		// $('#stripe_button').addClass('bg-secondary');
		// $('#stripe_button').text('Mm... please review your price.');

	} else{
		$('#price_review_comment').hide()

		// $('#stripe_button').on('click');
		// $('#stripe_button').addClass('bg-primary');
		// $('#stripe_button').text("Finalise Payment");
	}
	//check if both text revewers are hidden, alter stripe button
	display_stripe_btn();

});


$('#id_first_name, #id_last_name').change(function(){
	first_name = $('#id_first_name').val();
	last_name = $('#id_last_name').val();
	regex_test = /^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$/;
	if ((first_name.length < 1) || (last_name.length < 1)){
		$('#name_review_comment').show();
	} else if ((regex_test.test(first_name)) && (regex_test.test(last_name))){
		$('#name_review_comment').hide();		
	}

	//check if both text revewers are hidden, alter stripe button
	display_stripe_btn(); 
})

$('#stripe_button').click(function(){
	if ($('#stripe_button').hasClass('disabled') && ($('#id_amount_paid').val() > 0.99)){
		window.location.href=window.location.href
		// history.go(0)
		// location.reload(true);
	}else if ($('#id_amount_paid').val() < 0.99){
		// alert('yess!'
		$('#stripe_button').hide()
		$('#stripe_button').off('click');
		$('#stripe_button').addClass('bg-secondary');
		$('#stripe_button').text('Mm... please review your price.');
		$('#id_amount_paid').popover("toggle");
	} else{
	
		var stripe_pk = $('#stripe_pk').text()
		var token = function(res){
			var $id = $('<input type=hidden name=stripeToken />').val(res.id);
			var $email = $('<input type=hidden name=stripeEmail />').val(res.email);
			$('a').bind("click", function() { return false; });
		    $('button').addClass('disabled');
			$('#stripe_button').addClass('bg-secondary');
			$('#stripe_button').text('Please wait');
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
}
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


