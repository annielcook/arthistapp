(function($, window) {
    $('.jumbotron').each(function() {
        $(this).click(function() {
            $('#text-'+$(this).attr('id')).toggleClass('hidden-lg')
        })
    })

}).call(this, jQuery, window);
