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
        'views--exp-likeminded_projects-page' => array(
          'module' => 'views',
          'delta' => '-exp-likeminded_projects-page',
          'region' => 'content',
          'weight' => '-10',
        ),
        'views-likeminded_projects-block' => array(
          'module' => 'views',
          'delta' => 'likeminded_projects-block',
          'region' => 'postscript',
          'weight' => '-7',
        ),
        'views-volunteers-block' => array(
          'module' => 'views',
          'delta' => 'volunteers-block',
          'region' => 'postscript',
          'weight' => '-6',
        ),
        'views-participants-block' => array(
          'module' => 'views',
          'delta' => 'participants-block',
          'region' => 'postscript',
          'weight' => '-5',
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
