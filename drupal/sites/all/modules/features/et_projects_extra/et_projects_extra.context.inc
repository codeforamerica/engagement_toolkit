<?php
/**
 * @file
 * et_projects_extra.context.inc
 */

/**
 * Implementation of hook_context_default_contexts().
 */
function et_projects_extra_context_default_contexts() {
  $export = array();

  $context = new stdClass;
  $context->disabled = FALSE; /* Edit this to true to make a default context disabled initially */
  $context->api_version = 3;
  $context->name = 'et_projects';
  $context->description = 'Context for project pages.';
  $context->tag = 'et';
  $context->conditions = array(
    'node' => array(
      'values' => array(
        'project' => 'project',
      ),
      'options' => array(
        'node_form' => '0',
      ),
    ),
  );
  $context->reactions = array(
    'block' => array(
      'blocks' => array(
        'et_blocks-et_ph_project_supported' => array(
          'module' => 'et_blocks',
          'delta' => 'et_ph_project_supported',
          'region' => 'sidebar_second',
          'weight' => '-10',
        ),
        'et_blocks-et_ph_project_location' => array(
          'module' => 'et_blocks',
          'delta' => 'et_ph_project_location',
          'region' => 'sidebar_second',
          'weight' => '-9',
        ),
        'views-et_projects_supporters-block' => array(
          'module' => 'views',
          'delta' => 'et_projects_supporters-block',
          'region' => 'sidebar_second',
          'weight' => '-8',
        ),
        'et_blocks-et_custom_facebook_like' => array(
          'module' => 'et_blocks',
          'delta' => 'et_custom_facebook_like',
          'region' => 'sidebar_second',
          'weight' => '-7',
        ),
      ),
    ),
  );
  $context->condition_mode = 0;

  // Translatables
  // Included for use with string extractors like potx.
  t('Context for project pages.');
  t('et');
  $export['et_projects'] = $context;

  return $export;
}
