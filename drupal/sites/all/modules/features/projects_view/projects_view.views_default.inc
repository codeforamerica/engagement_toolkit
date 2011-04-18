<?php
/**
 * @file
 * projects_view.views_default.inc
 */

/**
 * Implementation of hook_views_default_views().
 */
function projects_view_views_default_views() {
  $export = array();

  $view = new view;
  $view->name = 'likeminded_projects';
  $view->description = 'Display projects imported from LikeMinded';
  $view->tag = 'default';
  $view->base_table = 'node';
  $view->human_name = 'Likeminded Projects';
  $view->core = 7;
  $view->api_version = '3.0-alpha1';
  $view->disabled = FALSE; /* Edit this to true to make a default view disabled initially */

  /* Display: Master */
  $handler = $view->new_display('default', 'Master', 'default');
  $handler->display->display_options['title'] = 'Projects';
  $handler->display->display_options['access']['type'] = 'perm';
  $handler->display->display_options['cache']['type'] = 'none';
  $handler->display->display_options['query']['type'] = 'views_query';
  $handler->display->display_options['exposed_form']['type'] = 'basic';
  $handler->display->display_options['pager']['type'] = 'full';
  $handler->display->display_options['pager']['options']['items_per_page'] = '20';
  $handler->display->display_options['pager']['options']['offset'] = '0';
  $handler->display->display_options['pager']['options']['id'] = '0';
  $handler->display->display_options['pager']['options']['expose']['items_per_page_options_all'] = 0;
  $handler->display->display_options['style_plugin'] = 'default';
  $handler->display->display_options['row_plugin'] = 'fields';
  $handler->display->display_options['row_options']['hide_empty'] = 0;
  /* Field: Content: Title */
  $handler->display->display_options['fields']['title']['id'] = 'title';
  $handler->display->display_options['fields']['title']['table'] = 'node';
  $handler->display->display_options['fields']['title']['field'] = 'title';
  $handler->display->display_options['fields']['title']['label'] = '';
  $handler->display->display_options['fields']['title']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['title']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['title']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['title']['alter']['external'] = 0;
  $handler->display->display_options['fields']['title']['alter']['replace_spaces'] = 0;
  $handler->display->display_options['fields']['title']['alter']['trim'] = 0;
  $handler->display->display_options['fields']['title']['alter']['nl2br'] = 0;
  $handler->display->display_options['fields']['title']['alter']['word_boundary'] = 0;
  $handler->display->display_options['fields']['title']['alter']['ellipsis'] = 0;
  $handler->display->display_options['fields']['title']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['title']['alter']['html'] = 0;
  $handler->display->display_options['fields']['title']['element_type'] = 'h3';
  $handler->display->display_options['fields']['title']['element_label_colon'] = 1;
  $handler->display->display_options['fields']['title']['element_default_classes'] = 1;
  $handler->display->display_options['fields']['title']['hide_empty'] = 0;
  $handler->display->display_options['fields']['title']['empty_zero'] = 0;
  $handler->display->display_options['fields']['title']['link_to_node'] = 1;
  /* Field: Fields: Problem */
  $handler->display->display_options['fields']['field_problem']['id'] = 'field_problem';
  $handler->display->display_options['fields']['field_problem']['table'] = 'field_data_field_problem';
  $handler->display->display_options['fields']['field_problem']['field'] = 'field_problem';
  $handler->display->display_options['fields']['field_problem']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['external'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['replace_spaces'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['trim'] = 1;
  $handler->display->display_options['fields']['field_problem']['alter']['nl2br'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['max_length'] = '140';
  $handler->display->display_options['fields']['field_problem']['alter']['word_boundary'] = 1;
  $handler->display->display_options['fields']['field_problem']['alter']['ellipsis'] = 1;
  $handler->display->display_options['fields']['field_problem']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['html'] = 0;
  $handler->display->display_options['fields']['field_problem']['element_label_type'] = 'h4';
  $handler->display->display_options['fields']['field_problem']['element_label_colon'] = 0;
  $handler->display->display_options['fields']['field_problem']['element_default_classes'] = 1;
  $handler->display->display_options['fields']['field_problem']['hide_empty'] = 0;
  $handler->display->display_options['fields']['field_problem']['empty_zero'] = 0;
  $handler->display->display_options['fields']['field_problem']['field_api_classes'] = 0;
  /* Field: Fields: Result */
  $handler->display->display_options['fields']['field_result']['id'] = 'field_result';
  $handler->display->display_options['fields']['field_result']['table'] = 'field_data_field_result';
  $handler->display->display_options['fields']['field_result']['field'] = 'field_result';
  $handler->display->display_options['fields']['field_result']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['external'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['replace_spaces'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['trim'] = 1;
  $handler->display->display_options['fields']['field_result']['alter']['nl2br'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['max_length'] = '140';
  $handler->display->display_options['fields']['field_result']['alter']['word_boundary'] = 1;
  $handler->display->display_options['fields']['field_result']['alter']['ellipsis'] = 1;
  $handler->display->display_options['fields']['field_result']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['field_result']['alter']['html'] = 0;
  $handler->display->display_options['fields']['field_result']['element_label_type'] = 'h4';
  $handler->display->display_options['fields']['field_result']['element_label_colon'] = 0;
  $handler->display->display_options['fields']['field_result']['element_default_classes'] = 1;
  $handler->display->display_options['fields']['field_result']['hide_empty'] = 0;
  $handler->display->display_options['fields']['field_result']['empty_zero'] = 0;
  $handler->display->display_options['fields']['field_result']['field_api_classes'] = 0;
  /* Sort criterion: Content: Post date */
  $handler->display->display_options['sorts']['created']['id'] = 'created';
  $handler->display->display_options['sorts']['created']['table'] = 'node';
  $handler->display->display_options['sorts']['created']['field'] = 'created';
  $handler->display->display_options['sorts']['created']['order'] = 'DESC';
  /* Contextual filter: Content: Type */
  $handler->display->display_options['arguments']['type']['id'] = 'type';
  $handler->display->display_options['arguments']['type']['table'] = 'node';
  $handler->display->display_options['arguments']['type']['field'] = 'type';
  $handler->display->display_options['arguments']['type']['default_argument_type'] = 'fixed';
  $handler->display->display_options['arguments']['type']['default_argument_skip_url'] = 0;
  $handler->display->display_options['arguments']['type']['summary']['number_of_records'] = '0';
  $handler->display->display_options['arguments']['type']['summary']['format'] = 'default_summary';
  $handler->display->display_options['arguments']['type']['summary_options']['items_per_page'] = '25';
  /* Filter criterion: Content: Published */
  $handler->display->display_options['filters']['status']['id'] = 'status';
  $handler->display->display_options['filters']['status']['table'] = 'node';
  $handler->display->display_options['filters']['status']['field'] = 'status';
  $handler->display->display_options['filters']['status']['value'] = 1;
  $handler->display->display_options['filters']['status']['group'] = 0;
  $handler->display->display_options['filters']['status']['expose']['operator'] = FALSE;

  /* Display: Page */
  $handler = $view->new_display('page', 'Page', 'page');
  $handler->display->display_options['path'] = 'likeminded-projects';
  $translatables['likeminded_projects'] = array(
    t('Master'),
    t('Projects'),
    t('more'),
    t('Apply'),
    t('Reset'),
    t('Sort by'),
    t('Asc'),
    t('Desc'),
    t('Items per page'),
    t('- All -'),
    t('Offset'),
    t('Problem'),
    t('Result'),
    t('All'),
    t('Page'),
  );
  $export['likeminded_projects'] = $view;

  return $export;
}
