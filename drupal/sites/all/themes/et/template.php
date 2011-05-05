<?php

// Include preprocessing functions
include('et.preprocess.inc');

/**
 * Implements hook_form_alter().
 */
function et_form_alter(&$form, &$form_state, $form_id) {
  // Add appropriate title for search form
  if ($form_id == 'search_block_form') {
    $form['search_block_form']['#title'] = '';
    unset($form['search_block_form']['#title_display']);
  }
}

/**
 * Header region override
 * Prints header blocks without region wrappers
 */
/*
function et_region__header($vars) {
  return $vars['content'];
}
*/


/**
 * File element override
 * Sets form file input max width
 */
function et_file($element) {
  $element['#size'] = ($element['#size'] > 40) ? 40 : $element['#size'];
  return theme_file($element);
}

