jQuery(document).ready(function(){
    $('.navigation__link, .sidebar__menu__link').bind('click', function(e) {
        if( $(this).data('target') !== undefined) {
            e.preventDefault();
            $('.sidebar-nav').removeClass('sidebar-nav--opened');
            opened = false;
            $('body').scrollTo('.' + $(this).data('target'), 1000, {offset: -40});
        }
    });
});
