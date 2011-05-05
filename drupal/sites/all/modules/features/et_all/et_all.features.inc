<?php
/**
 * @file
 * et_all.features.inc
 */

/**
 * Implementation of hook_ctools_plugin_api().
 */
function et_all_ctools_plugin_api() {
  list($module, $api) = func_get_args();
  if ($module == "context" && $api == "context") {
    return array("version" => 3);
  }
}
