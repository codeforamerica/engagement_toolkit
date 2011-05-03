<?php

/**
 * Stub functions, taken from Fusion Core.
 */

/**
 * HTML preprocessing
 */
function et_preprocess_html(&$vars) {

}


/**
 * Page preprocessing
 */
function et_preprocess_page(&$vars) {
  // Create some resource variables
  $vars['logo_image'] = theme('image', array(
    'path' => drupal_get_path('theme', 'et') . '/images/header_logo.gif', 
    )
  );
  $vars['logo_image_link'] = l($vars['logo_image'], '<front>', array('html' => TRUE));
  
  // Create login link
  $account_text = t('Sign in');
  global $user;
  if ($user->uid > 0) {
    // User is logged in
    $account_text = t('My Account');
  }
  $vars['account_link'] = l($account_text, 'user', array(
    'attributes' => array(
      'id' => 'signin',
    )
  ));
  
  // Temp for wireframing or MVP
  $vars['submit_btn'] = url(drupal_get_path('theme', 'et') . '/images/submit-large-overlay.gif');
  
  // Hardcoded site names
  switch ($_SERVER['HTTP_HOST']) {
    case 'philly.et.codeforamerica.org':
      $vars['sub_site_name'] = t('Philadelphia');
      break;
      
    case 'seattle.et.codeforamerica.org':
      $vars['sub_site_name'] = t('Seattle');
      break;
      
    case 'sf.et.codeforamerica.org':
      $vars['sub_site_name'] = t('San Francisco');
      break;
      
    case 'staging.et.codeforamerica.org':
      $vars['sub_site_name'] = t('Staging');
      break;
      
    case 'et.codeforamerica.org':
      $vars['sub_site_name'] = t('Main ET');
      break;
      
    default:
      $vars['sub_site_name'] = t('Development');
      break;
  }
  
  // Facebook Like link (TODO: Use module)
  // Make URL, Facebook is not ok with a "localhost" URL.
  $url = ($_SERVER['SERVER_PORT'] == '443') ? 'https' : 'http';
  $url .= '://';
  $url .= ($_SERVER['HTTP_HOST'] == 'localhost') ? 'localhost.com' : $_SERVER['HTTP_HOST'];
  $url .= $_SERVER['REQUEST_URI'];
  $vars['fb_like'] = '<script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script><fb:like href="' . urlencode($url) . '" send="true" width="200" show_faces="false" font=""></fb:like>';
}


/**
 * Region preprocessing
 */
function et_preprocess_region(&$vars) {

}


/**
 * Block preprocessing
 */
function et_preprocess_block(&$vars) {

}


/**
 * Node preprocessing
 */
function et_preprocess_node(&$vars) {

}


/**
 * Comment preprocessing
 */
function et_preprocess_comment(&$vars) {

}


/**
 * Views preprocessing
 * Add view type class (e.g., node, teaser, list, table)
 */
function et_preprocess_views_view(&$vars) {

}

/**
 * Implements hook_form_alter().
 */
function et_form_alter(&$form, &$form_state, $form_id) {
  // Add appropriate title for search form
  if ($form_id == 'search_block_form') {
    $form['search_block_form']['#title'] = t('What do you care about?');
    unset($form['search_block_form']['#title_display']);
  }
}