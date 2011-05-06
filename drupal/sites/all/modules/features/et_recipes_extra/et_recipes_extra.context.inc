<?php
/**
 * @file
 * et_recipes_extra.context.inc
 */

/**
 * Implementation of hook_context_default_contexts().
 */
function et_recipes_extra_context_default_contexts() {
  $export = array();

  $context = new stdClass;
  $context->disabled = FALSE; /* Edit this to true to make a default context disabled initially */
  $context->api_version = 3;
  $context->name = 'et_recipes';
  $context->description = 'Context for recipes';
  $context->tag = 'et';
  $context->conditions = array(
    'node' => array(
      'values' => array(
        'recipe' => 'recipe',
      ),
      'options' => array(
        'node_form' => '0',
      ),
    ),
  );
  $context->reactions = array();
  $context->condition_mode = 0;

  // Translatables
  // Included for use with string extractors like potx.
  t('Context for recipes');
  t('et');
  $export['et_recipes'] = $context;

  return $export;
}
