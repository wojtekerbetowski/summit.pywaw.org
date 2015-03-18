jQuery(document).ready(function(){

    /* Mobile sidebar menu */

    var opened = false;

    $('#js-menu-button').bind('click', function(){

        if( opened ) {
            $('.sidebar-nav').removeClass('sidebar-nav--opened');
            opened = false;
        }else{
            $('.sidebar-nav').addClass('sidebar-nav--opened');
            opened = true;
        }
    });

    $( document ).on( "click", ".container", function() {
        $('.sidebar-nav').removeClass('sidebar-nav--opened');
        opened = false;
    });

});
