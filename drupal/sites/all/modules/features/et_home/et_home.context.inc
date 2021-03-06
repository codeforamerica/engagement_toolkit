<?php
/**
 * @file
 * et_home.context.inc
 */

/**
 * Implementation of hook_context_default_contexts().
 */
function et_home_context_default_contexts() {
  $export = array();

  $context = new stdClass;
  $context->disabled = FALSE; /* Edit this to true to make a default context disabled initially */
  $context->api_version = 3;
  $context->name = 'et_home';
  $context->description = 'Home Page context for blocks and similar things.';
  $context->tag = 'et';
  $context->conditions = array(
    'path' => array(
      'values' => array(
        '<front>' => '<front>',
      ),
    ),
  );
  $context->reactions = array(
    'block' => array(
      'blocks' => array(
        'views-tags-block' => array(
          'module' => 'views',
          'delta' => 'tags-block',
          'region' => 'sidebar_first',
          'weight' => '-10',
        ),
        'views-menus-block_1' => array(
          'module' => 'views',
          'delta' => 'menus-block_1',
          'region' => 'postscript',
          'weight' => '-10',
        ),
        'views-recipes-block_1' => array(
          'module' => 'views',
          'delta' => 'recipes-block_1',
          'region' => 'postscript',
          'weight' => '-9',
        ),
      ),
    ),
  );
  $context->condition_mode = 0;

  // Translatables
  // Included for use with string extractors like potx.
  t('Home Page context for blocks and similar things.');
  t('et');
  $export['et_home'] = $context;

  return $export;
}
