function positionFooter() {
  var $footer = $('#footer');
  $footer.removeClass('fixedfooter');
  if ($(document.body).height() < $(window).height()) {
    $footer.addClass('fixedfooter');
  } else {
    $footer.removeClass('fixedfooter');
  }
}

$(document).ready(function () {
  $(window).resize(positionFooter).resize();
  console.log('yay');
  //preventFOUT();
});
$(window).ready(function () {
  //run _after_ images have been loaded as well.
  $(window).resize(positionFooter).resize();
});
