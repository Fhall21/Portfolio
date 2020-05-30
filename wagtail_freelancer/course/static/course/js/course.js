
$(function(){
	$('#id_is_student, #id_student_keen').removeClass("form-control")
	$('#id_is_student, #id_student_keen div').css({'justify-self': 'center'});

  //if mobile make the student quote go last
  let isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;
  if (isMobile){

    //create clones and get el
    let recommendation = $('#past-student-recommendation');
    let recommendation_clone = recommendation.clone();

    let quote = $('#past-student-quote');
    let quote_clone = quote.clone();
    
    // replace the appropriate ones
    recommendation.replaceWith(quote_clone);
    quote.replaceWith(recommendation_clone);
    
  }

  //if tablet fix up some styling
  let isTablet = window.matchMedia("only screen and (max-width: 760px min-width:575)").matches;
  if (isTablet){
    alert("tablet");
  }

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




