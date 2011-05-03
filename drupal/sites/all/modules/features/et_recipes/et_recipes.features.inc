<?php
/**
 * @file
 * et_recipes.features.inc
 */

/**
 * Implementation of hook_ctools_plugin_api().
 */
function et_recipes_ctools_plugin_api() {
  list($module, $api) = func_get_args();
  if ($module == "strongarm" && $api == "strongarm") {
    return array("version" => 1);
  }
}

/**
 * Implementation of hook_node_info().
 */
function et_recipes_node_info() {
  $items = array(
    'recipe' => array(
      'name' => t('Recipe'),
      'base' => 'node_content',
      'description' => t('Recipes are context filled collection of knowledge (ie Q+A)'),
      'has_title' => '1',
      'title_label' => t('Title'),
      'help' => '',
    ),
  );
  return $items;
}
