
$(function(){
	$('#id_is_student, #id_student_keen').removeClass("form-control")
	$('#id_is_student, #id_student_keen div').css({'justify-self': 'center'});

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

    //countdown flipper
  // $('#myFlipper').flipper('init');


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




