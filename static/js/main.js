$(document).ready(function() {

  function play(url) {
      $.ajax({
      url: url
    })
    .done(function(html) {
      $('#results').html(html).fadeIn(1000);
    });
  };

    // - slow down transition from selection to results
    // - hide divs of what is not chosen before displaying computer choice

  $('.choice').on('click', function(e) {
    e.preventDefault();
    var url = $(this).attr('href');
    $('.removable').fadeOut(1000, function() {
      play(url);
    });
  });

});
