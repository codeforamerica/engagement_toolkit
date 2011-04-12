<?php
/**
 * @file
 * et_projects.strongarm.inc
 */

/**
 * Implementation of hook_strongarm().
 */
function et_projects_strongarm() {
  $export = array();

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'node_options_project';
  $strongarm->value = array(
    0 => 'status',
    1 => 'promote',
  );
  $export['node_options_project'] = $strongarm;

  $strongarm = new stdClass;
  $strongarm->disabled = FALSE; /* Edit this to true to make a default strongarm disabled initially */
  $strongarm->api_version = 1;
  $strongarm->name = 'pathauto_node_project_pattern';
  $strongarm->value = 'projects/[node:title]';
  $export['pathauto_node_project_pattern'] = $strongarm;

  return $export;
}
