(function ($) {
Drupal.settings.views = Drupal.settings.views || {'ajax_path': '/views/ajax'};

Drupal.behaviors.quicktabs = {
  attach: function (context, settings) {
    $.extend(true, Drupal.settings, settings);
    $('.quicktabs_wrapper:not(.quicktabs-processed)', context).addClass('quicktabs-processed').each(function(){
      Drupal.quicktabs.prepare(this);
    });
  }
}

Drupal.quicktabs = Drupal.quicktabs || {};

// setting up the inital behaviours
Drupal.quicktabs.prepare = function(el) {
  // el.id format: "quicktabs-$name"
  var name = el.id.substring(el.id.indexOf('-') +1);
  var $ul = $(el).find('ul.quicktabs_tabs:first');
  $ul.find('li a').each(function(){this.name = name}).each(Drupal.quicktabs.initialiseLink);

  // Search for the active tab.
  //var $active_tab = $(el).children('.quicktabs_tabs').find('li.active a');
  //if ($active_tab.hasClass('qt_tab') || $active_tab.hasClass('qt_ajax_tab')) {
  //  $active_tab.trigger('click');
  //}
  //else {
  //  // Click on the first tab.
  //  $(el).children('.quicktabs_tabs').find('li.first a').trigger('click');
  //}
}

Drupal.quicktabs.initialiseLink = function(index, element, tab) {
  if (!element.myTabIndex) {
    element.myTabIndex = index;
  }
  if (!tab) {
    tab = new Drupal.quicktabs.tab(element);
  }
  if (tab.tabpage.hasClass('quicktabs_tabpage') || tab.tabObj.type != 'view') {
    $(element).bind('click', {tab: tab}, Drupal.quicktabs.clickHandler);
  }
  else {
    Drupal.quicktabs.ajaxView(tab, element);
  }
}

Drupal.quicktabs.clickHandler = function(event) {
  var tab = event.data.tab;

  // Set clicked tab to active.
  $(this).parents('li').siblings().removeClass('active');
  $(this).parents('li').addClass('active');

  // Hide all tabpages.
  tab.container.children().addClass('quicktabs-hide');

  // Show the active tabpage.
  if (tab.tabpage.hasClass('quicktabs_tabpage')) {
    tab.tabpage.removeClass('quicktabs-hide');
  }
  else {
    if ($(this).hasClass('qt_ajax_tab')) {
      // construct the ajax path to retrieve the content, depending on type
      var qtAjaxPath = Drupal.settings.basePath + 'quicktabs/ajax/' + tab.tabObj.type + '/';
      switch (tab.tabObj.type) {
        case 'node':
          qtAjaxPath +=  tab.tabObj.nid + '/' + tab.tabObj.teaser + '/' + tab.tabObj.hide_title;
          break;
        case 'block':
          qtAjaxPath +=  tab.tabObj.bid + '/' + tab.tabObj.hide_title;
          break;
        case 'qtabs':
          qtAjaxPath +=  tab.tabObj.machine_name;
          break;
      }

      $.ajax({
        url: qtAjaxPath,
        type: 'GET',
        data: null,
        beforeSend: function (xmlhttprequest) {
          var $progress = $('<div class="ajax-progress ajax-progress-throbber"><div class="throbber">&nbsp;</div></div>');
          $(tab.element).after($progress);
        },
        success: tab.options.success,
        complete: tab.options.complete,
        dataType: 'json'
      });
    }
  }
  return false;
}

// constructor for an individual tab
Drupal.quicktabs.tab = function (el) {
  this.element = el;
  this.tabIndex = el.myTabIndex;
  this.name = el.name;
  var qtKey = 'qt_' + this.name;
  var i = 0;
  for (var key in Drupal.settings.quicktabs[qtKey].tabs) {
    if (i == this.tabIndex) {
      this.tabObj = Drupal.settings.quicktabs[qtKey].tabs[key];
      this.tabKey = key;
    }
    i++;
  }
  this.tabpage_id = 'quicktabs_tabpage_' + this.name + '_' + this.tabKey;
  this.container = $('#quicktabs_container_' + this.name);
  this.tabpage = this.container.find('#' + this.tabpage_id);
  // The 'this' variable will not persist inside of the options object.
  var tab = this;
  this.options = {
    success: function(response) {
      return tab.success(response);
    },
    complete: function(response) {
      return tab.complete();
    }
  }
}

// ajax callback for non-views tabs
Drupal.quicktabs.tab.prototype.success = function(response) {
  this.container.append(Drupal.theme('quicktabsResponse', this, response.data));
  this.tabpage = this.container.find('#' + this.tabpage_id);
  Drupal.attachBehaviors(this.container, response.settings);
}


Drupal.quicktabs.tab.prototype.complete = function() {
  $(this.element).parent().find('.ajax-progress').remove();
}

Drupal.quicktabs.view_dom_id = 0; // keeps track of ids to use for ajax-loaded views

Drupal.quicktabs.ajaxView = function(tab, element) {
  
  var ajax_path = Drupal.settings.views.ajax_path;
   //If there are multiple views this might've ended up showing up multiple times.
  if (ajax_path.constructor.toString().indexOf("Array") != -1) {
    ajax_path = ajax_path[0];
  }
  var args;
  if (tab.tabObj.args != '') {
    args = tab.tabObj.args.join('/');
  } else {
    args = '';
  }
  var dom_id = 0;
  if (Drupal.quicktabs.view_dom_id > 0) {
    dom_id = Drupal.quicktabs.view_dom_id;
  }
  else {
    $('div.view').each(function(){
      var classList = $(this).attr('class').split(/\s+/);
      $.each(classList, function(index, item){
        if (item.match(/^view\-dom-\id\-\d+/)) {
          var this_dom_id = item.split(/\-/)[3];
          if (this_dom_id > dom_id) {
            dom_id = this_dom_id;
          }
        }
      });
    });
  }

  dom_id++;
  Drupal.quicktabs.view_dom_id = dom_id;

  var viewData = {
    'view_name': tab.tabObj.vid,
    'view_display_id': tab.tabObj.display,
    'view_args': args,
    'view_dom_id': dom_id
  }
  tab.dom_id = dom_id;
  var element_settings = {};
  element_settings.url = ajax_path;
  element_settings.event = 'click';
  element_settings.progress = { 'type': 'throbber' };
  element_settings.submit = viewData;
  
  var ajax = new Drupal.ajax(false, element, element_settings);
  // Override HTTP method type and the beforeSerialize and success methods.
  ajax.options.type = 'GET';
  ajax.beforeSerialize = function(element_settings, options) { return; };
  ajax.old_success = ajax.success;
  ajax.success = function(response, status) {
    // Set clicked tab to active.
    $(element).parents('li').siblings().removeClass('active');
    $(element).parents('li').addClass('active');
    tab.container.children().addClass('quicktabs-hide');
    tab.container.append(Drupal.theme('quicktabsResponse', tab, null));
    tab.tabpage = tab.container.find('#' + tab.tabpage_id);
    $(element).unbind();
    this.old_success(response, status);
    Drupal.quicktabs.initialiseLink(element.myTabIndex, element, tab);
  }
}

// theme function for ajax response
Drupal.theme.prototype.quicktabsResponse = function(tab, new_content) {
  var newDiv = tab.tabObj.type == 'view' ? '<div id="' + tab.tabpage_id + '" class="quicktabs_tabpage"><div class="view-dom-id-' + tab.dom_id + '"></div></div>' : '<div id="' + tab.tabpage_id + '" class="quicktabs_tabpage">' + new_content + '</div>';
  return newDiv;
};
})(jQuery);
