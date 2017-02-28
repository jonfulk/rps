$( document ).ready(function() {

    // - highlight on hover
    $( "a > img" ).hover(
        function() {$( this ).addClass( 'outline' )},
        function() {$( this ).removeClass( 'outline' )}
    );

    // // - slow down transition from selection to results
    // - use AJAX to do this in only 1 view?
    // - hide divs of what is not chosen before displaying computer choice


});
