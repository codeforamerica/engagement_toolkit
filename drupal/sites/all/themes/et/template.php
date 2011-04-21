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
  $vars['logo_image'] = theme('image', array(
    'path' => drupal_get_path('theme', 'et') . '/images/header_logo.gif', 
    )
  );
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