function positionFooter() {
  var $footer = $('#footerpositioner');
  $footer.removeClass('fixedfooter');
  if ($(document.body).height() < $(window).height()) {
    $footer.addClass('fixedfooter');
  } else {
    $footer.removeClass('fixedfooter');
  }
}

$.fn.expander = function () {
  $(this).each(function () {
    $(this).click(function () {
      if ($(this).hasClass('expand')) {
        //hide
        $(this).removeClass('expand').addClass('collapse');
        $(this).siblings('ul').hide(200, function () {
          $(window).resize(positionFooter).resize();
        });
      } else {
        //show
        $(this).removeClass('collapse').addClass('expand');
        $(this).siblings('ul').show(200, function () {
          $(window).resize(positionFooter).resize();
        });
      }
    }).click();
  });
}


$(document).ready(function () {
  var $items = $(".sidebar .collapsed>li>a");

  $items.expander();  
  $(window).resize(positionFooter).resize();

  //preventFOUT();
});
$(window).ready(function () {
  //run _after_ images have been loaded as well.
  $(window).resize(positionFooter).resize();
});
