<?php

/**
 * Implementation of hook_views_plugins().
 */

function views_number_results_views_plugins() {
  return array(
    'row' => array(
      'views_number_results_fields' => array(
        'title' => t('Total Number Results'),
        'group' => t('Global'),
        'help' => t('Displays the number of results for this view.'),
        'handler' => 'views_number_results_handler_field_counter_total',
        'uses fields' => TRUE,
        'uses options' => FALSE,
        'type' => 'normal',
        'help topic' => 'style-row-fields',
      ),
    ),
  );
}
