<?php
/**
 * @file
 * likemindedimport.strongarm.inc
 */

/**
 * Implementation of hook_strongarm().
 */
function likemindedimport_strongarm() {
  $export = array();

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_anonymous_likemindedsource';
  $strongarm->value = 0;
  $export['comment_anonymous_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_default_mode_likemindedsource';
  $strongarm->value = 1;
  $export['comment_default_mode_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_default_per_page_likemindedsource';
  $strongarm->value = '50';
  $export['comment_default_per_page_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_form_location_likemindedsource';
  $strongarm->value = 1;
  $export['comment_form_location_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_likemindedsource';
  $strongarm->value = '2';
  $export['comment_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_preview_likemindedsource';
  $strongarm->value = '1';
  $export['comment_preview_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'comment_subject_field_likemindedsource';
  $strongarm->value = 1;
  $export['comment_subject_field_likemindedsource'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'node_options_likemindedsource';
  $strongarm->value = array(
    0 => 'status',
    1 => 'promote',
  );
  $export['node_options_likemindedsource'] = $strongarm;

  return $export;
}
