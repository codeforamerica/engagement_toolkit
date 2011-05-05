<?php
/**
 * @file
 * et_clone_feature.context.inc
 */

/**
 * Implementation of hook_context_default_contexts().
 */
function et_clone_feature_context_default_contexts() {
  $export = array();

  $context = new stdClass;
  $context->disabled = FALSE; /* Edit this to true to make a default context disabled initially */
  $context->api_version = 3;
  $context->name = 'et_clone';
  $context->description = 'Cloning contexts';
  $context->tag = 'et';
  $context->conditions = array(
    'node' => array(
      'values' => array(
        'project' => 'project',
        'recipe' => 'recipe',
      ),
      'options' => array(
        'node_form' => '0',
      ),
    ),
  );
  $context->reactions = array(
    'block' => array(
      'blocks' => array(
        'et_clone-et_clone_block' => array(
          'module' => 'et_clone',
          'delta' => 'et_clone_block',
          'region' => 'sidebar_first',
          'weight' => '-10',
        ),
      ),
    ),
  );
  $context->condition_mode = 0;

  // Translatables
  // Included for use with string extractors like potx.
  t('Cloning contexts');
  t('et');
  $export['et_clone'] = $context;

  return $export;
}
