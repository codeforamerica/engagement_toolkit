<?php
/**
 * @file
 * et_project_map.features.inc
 */

/**
 * Implementation of hook_ctools_plugin_api().
 */
function et_project_map_ctools_plugin_api() {
  list($module, $api) = func_get_args();
  if ($module == "openlayers" && $api == "openlayers_maps") {
    return array("version" => 1);
  }
  list($module, $api) = func_get_args();
  if ($module == "openlayers" && $api == "openlayers_styles") {
    return array("version" => 1);
  }
}

/**
 * Implementation of hook_views_api().
 */
function et_project_map_views_api() {
  list($module, $api) = func_get_args();
  if ($module == "views" && $api == "views_default") {
    return array("version" => 3.0);
  }
}
