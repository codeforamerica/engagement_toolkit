<?php
/**
 * @file
 * et_clone_feature.strongarm.inc
 */

/**
 * Implementation of hook_strongarm().
 */
function et_clone_feature_strongarm() {
  $export = array();

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'clone_omitted';
  $strongarm->value = array(
    'likemindedsource' => 'likemindedsource',
    'page' => 'page',
    'qa' => 'qa',
    'project' => 0,
    'recipe' => 0,
  );
  $export['clone_omitted'] = $strongarm;

  return $export;
}
