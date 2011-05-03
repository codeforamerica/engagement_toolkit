<?php
/**
 * @file
 * et_qa.features.inc
 */

/**
 * Implementation of hook_ctools_plugin_api().
 */
function et_qa_ctools_plugin_api() {
  list($module, $api) = func_get_args();
  if ($module == "strongarm" && $api == "strongarm") {
    return array("version" => 1);
  }
}

/**
 * Implementation of hook_node_info().
 */
function et_qa_node_info() {
  $items = array(
    'qa' => array(
      'name' => t('Q+A'),
      'base' => 'node_content',
      'description' => t('A bit of knowledge usually in the format of a question and answer.'),
      'has_title' => '1',
      'title_label' => t('Question'),
      'help' => '',
    ),
  );
  return $items;
}
