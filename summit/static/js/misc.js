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



    $('.navigation__link, .sidebar__menu__link').bind('click', function(e) {
        e.preventDefault();
        if( $(this).data('target') !== undefined) {
            $('.sidebar-nav').removeClass('sidebar-nav--opened');
            opened = false;
            $('body').scrollTo('.' + $(this).data('target'), 1000, {offset: -40});
        }
    });

});
