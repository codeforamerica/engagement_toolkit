<?php
/**
 * @file
 * likemindedimport.features.inc
 */

/**
 * Implementation of hook_ctools_plugin_api().
 */
function likemindedimport_ctools_plugin_api() {
  list($module, $api) = func_get_args();
  if ($module == "feeds" && $api == "feeds_importer_default") {
    return array("version" => 1);
  }
}

/**
 * Implementation of hook_views_api().
 */
function likemindedimport_views_api() {
  list($module, $api) = func_get_args();
  if ($module == "views" && $api == "views_default") {
    return array("version" => 3.0);
  }
}
