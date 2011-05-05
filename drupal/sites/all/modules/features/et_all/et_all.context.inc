<?php
/**
 * @file
 * et_all.context.inc
 */

/**
 * Implementation of hook_context_default_contexts().
 */
function et_all_context_default_contexts() {
  $export = array();

  $context = new stdClass;
  $context->disabled = FALSE; /* Edit this to true to make a default context disabled initially */
  $context->api_version = 3;
  $context->name = 'et_all';
  $context->description = 'Context for all pages.';
  $context->tag = 'et';
  $context->conditions = array(
    'sitewide' => array(
      'values' => array(
        1 => 1,
      ),
    ),
  );
  $context->reactions = array(
    'block' => array(
      'blocks' => array(
        'menu-menu-et-menu' => array(
          'module' => 'menu',
          'delta' => 'menu-et-menu',
          'region' => 'header_menu',
          'weight' => '-21',
        ),
        'search-form' => array(
          'module' => 'search',
          'delta' => 'form',
          'region' => 'header_gap',
          'weight' => '-10',
        ),
      ),
    ),
  );
  $context->condition_mode = 0;

  // Translatables
  // Included for use with string extractors like potx.
  t('Context for all pages.');
  t('et');
  $export['et_all'] = $context;

  return $export;
}
