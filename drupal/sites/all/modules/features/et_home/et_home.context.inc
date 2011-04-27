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
        'et_blocks-et_ph_projects_count' => array(
          'module' => 'et_blocks',
          'delta' => 'et_ph_projects_count',
          'region' => 'postscript',
          'weight' => '-10',
        ),
        'et_blocks-et_ph_volunteers_count' => array(
          'module' => 'et_blocks',
          'delta' => 'et_ph_volunteers_count',
          'region' => 'postscript',
          'weight' => '-10',
        ),
        'et_blocks-et_ph_organizers_count' => array(
          'module' => 'et_blocks',
          'delta' => 'et_ph_organizers_count',
          'region' => 'postscript',
          'weight' => '-10',
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
