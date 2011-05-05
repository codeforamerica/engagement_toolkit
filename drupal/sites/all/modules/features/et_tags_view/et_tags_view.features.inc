<?php
/**
 * @file
 * et_tags_view.features.inc
 */

/**
 * Implementation of hook_views_api().
 */
function et_tags_view_views_api() {
  list($module, $api) = func_get_args();
  if ($module == "views" && $api == "views_default") {
    return array("version" => 3.0);
  }
}
