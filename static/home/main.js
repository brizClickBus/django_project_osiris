function show_money(){
  
  var display_value = document.getElementById("show_value").style.display;
  var display_eye = document.getElementById("show").style.display;

  if(display_value == "block" && display_eye){
      document.getElementById("show_value").style.display = 'none';
      document.getElementById("show").style.display = 'none';
      document.getElementById("hide_value").style.display = 'block';
      document.getElementById("hide").style.display = 'block';
  }else{
    document.getElementById("show_value").style.display = 'block';
    document.getElementById("show").style.display = 'block';
    document.getElementById("hide_value").style.display = 'none';
    document.getElementById("hide").style.display = 'none';
  }
}

$(function() {
    $('.toggle').click(function() {
      $('.nav-item').toggleClass('slide-out');
      $('.hamburger-1').toggleClass('cross-right');
      $('.hamburger-2').toggleClass('cross-hide');
      $('.hamburger-3').toggleClass('cross-left');
      $('.wobble').addClass('ripple');
      setTimeout(function(){
      $('.wobble').removeClass('ripple');
      }, 1000);
    });
  });