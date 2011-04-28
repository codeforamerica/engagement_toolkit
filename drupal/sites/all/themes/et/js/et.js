(function ($) {
Drupal.behaviors.homepageMoreLink = {
  attach: function (context, settings) {
    $('body.front .postscript-container .block').each(function(){
        var markup = $(this).find('.more-link a');
        var link =  $(this).find('.more-link a').attr("href");
        $(this).find('.more-link').hide();
        $(this).click(function(){
          document.location.href = link;
        });
    });
  }
};

})(jQuery);