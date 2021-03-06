<?php
/**
 * @file
 * et_clone_feature.features.inc
 */

/**
 * Implementation of hook_ctools_plugin_api().
 */
function et_clone_feature_ctools_plugin_api() {
  list($module, $api) = func_get_args();
  if ($module == "context" && $api == "context") {
    return array("version" => 3);
  }
  list($module, $api) = func_get_args();
  if ($module == "strongarm" && $api == "strongarm") {
    return array("version" => 1);
  }
}
