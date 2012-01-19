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
  //expand menu if the page is active
  $items.siblings("ul").find('li.current').parents('li').find('a').click();

  //preventFOUT();
  //footer menu hidden for landing page !mobile
  //shown for all else
  if (window.location.pathname != '/') {
    $('#footer .navmenu').show();
  }
});
$(window).ready(function () {
  //run _after_ images have been loaded as well.
  $(window).resize(positionFooter).resize();
});
