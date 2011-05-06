
(function ($) {
Drupal.behaviors.acquia_marinaRoundedCorners = {
  attach: function (context, settings) {
    // Rounded corners - Inner background
    $(".inner .marina-rounded-corners .inner-wrapper .inner-inner").corner("bottom 7px"); 
    $(".inner .marina-title-rounded-blue h2.block-title").corner("top 5px"); 
    $(".inner .marina-title-rounded-green h2.block-title").corner("top 5px"); 
    $("#comments h2.comments-header").corner("top 5px"); 
  }
};
})(jQuery);

(function ($) {
Drupal.behaviors.acquia_marinaPanelsEditFix = {
  attach: function (context, settings) {
    // Sets the .row class to have "overflow: visible" if editing Panel page
    $("#panels-edit-display-form").parents('.row', '.nested').css("overflow", "visible")
    $("#page-manager-edit").parents('.row', '.nested').css("overflow", "visible")
  }
};
})(jQuery);