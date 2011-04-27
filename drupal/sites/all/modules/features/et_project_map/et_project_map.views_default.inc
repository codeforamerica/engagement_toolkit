<?php
/**
 * @file
 * et_project_map.views_default.inc
 */

/**
 * Implementation of hook_views_default_views().
 */
function et_project_map_views_default_views() {
  $export = array();

  $view = new view;
  $view->name = 'project_map';
  $view->description = '';
  $view->tag = 'default';
  $view->base_table = 'node';
  $view->human_name = 'Project Map';
  $view->core = 7;
  $view->api_version = '3.0-alpha1';
  $view->disabled = FALSE; /* Edit this to true to make a default view disabled initially */

  /* Display: Master */
  $handler = $view->new_display('default', 'Master', 'default');
  $handler->display->display_options['title'] = 'Project Map';
  $handler->display->display_options['access']['type'] = 'perm';
  $handler->display->display_options['cache']['type'] = 'none';
  $handler->display->display_options['query']['type'] = 'views_query';
  $handler->display->display_options['exposed_form']['type'] = 'basic';
  $handler->display->display_options['pager']['type'] = 'full';
  $handler->display->display_options['pager']['options']['items_per_page'] = '10';
  $handler->display->display_options['style_plugin'] = 'openlayers_map';
  $handler->display->display_options['style_options']['map'] = 'et_project_map';
  /* Field: Content: Title */
  $handler->display->display_options['fields']['title']['id'] = 'title';
  $handler->display->display_options['fields']['title']['table'] = 'node';
  $handler->display->display_options['fields']['title']['field'] = 'title';
  $handler->display->display_options['fields']['title']['label'] = '';
  $handler->display->display_options['fields']['title']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['title']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['title']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['title']['alter']['trim'] = 0;
  $handler->display->display_options['fields']['title']['alter']['word_boundary'] = 0;
  $handler->display->display_options['fields']['title']['alter']['ellipsis'] = 0;
  $handler->display->display_options['fields']['title']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['title']['alter']['html'] = 0;
  $handler->display->display_options['fields']['title']['hide_empty'] = 0;
  $handler->display->display_options['fields']['title']['empty_zero'] = 0;
  $handler->display->display_options['fields']['title']['link_to_node'] = 1;
  /* Field: Fields: Location */
  $handler->display->display_options['fields']['field_location']['id'] = 'field_location';
  $handler->display->display_options['fields']['field_location']['table'] = 'field_data_field_location';
  $handler->display->display_options['fields']['field_location']['field'] = 'field_location';
  $handler->display->display_options['fields']['field_location']['label'] = '';
  $handler->display->display_options['fields']['field_location']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['external'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['replace_spaces'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['trim'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['nl2br'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['word_boundary'] = 1;
  $handler->display->display_options['fields']['field_location']['alter']['ellipsis'] = 1;
  $handler->display->display_options['fields']['field_location']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['field_location']['alter']['html'] = 0;
  $handler->display->display_options['fields']['field_location']['element_label_colon'] = 0;
  $handler->display->display_options['fields']['field_location']['element_default_classes'] = 1;
  $handler->display->display_options['fields']['field_location']['hide_empty'] = 0;
  $handler->display->display_options['fields']['field_location']['empty_zero'] = 0;
  $handler->display->display_options['fields']['field_location']['click_sort_column'] = 'wkt';
  $handler->display->display_options['fields']['field_location']['type'] = 'geofield_lat';
  $handler->display->display_options['fields']['field_location']['settings'] = array(
    'data' => 'full',
    'format' => 'decimal_degrees',
  );
  $handler->display->display_options['fields']['field_location']['field_api_classes'] = 0;
  /* Field: Fields: Problem */
  $handler->display->display_options['fields']['field_problem']['id'] = 'field_problem';
  $handler->display->display_options['fields']['field_problem']['table'] = 'field_data_field_problem';
  $handler->display->display_options['fields']['field_problem']['field'] = 'field_problem';
  $handler->display->display_options['fields']['field_problem']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['external'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['replace_spaces'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['trim'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['nl2br'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['word_boundary'] = 1;
  $handler->display->display_options['fields']['field_problem']['alter']['ellipsis'] = 1;
  $handler->display->display_options['fields']['field_problem']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['field_problem']['alter']['html'] = 0;
  $handler->display->display_options['fields']['field_problem']['element_label_colon'] = 1;
  $handler->display->display_options['fields']['field_problem']['element_default_classes'] = 1;
  $handler->display->display_options['fields']['field_problem']['hide_empty'] = 0;
  $handler->display->display_options['fields']['field_problem']['empty_zero'] = 0;
  $handler->display->display_options['fields']['field_problem']['field_api_classes'] = 0;
  /* Field: Fields: Location */
  $handler->display->display_options['fields']['field_location_1']['id'] = 'field_location_1';
  $handler->display->display_options['fields']['field_location_1']['table'] = 'field_data_field_location';
  $handler->display->display_options['fields']['field_location_1']['field'] = 'field_location';
  $handler->display->display_options['fields']['field_location_1']['label'] = '';
  $handler->display->display_options['fields']['field_location_1']['alter']['alter_text'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['make_link'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['absolute'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['external'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['replace_spaces'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['trim'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['nl2br'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['word_boundary'] = 1;
  $handler->display->display_options['fields']['field_location_1']['alter']['ellipsis'] = 1;
  $handler->display->display_options['fields']['field_location_1']['alter']['strip_tags'] = 0;
  $handler->display->display_options['fields']['field_location_1']['alter']['html'] = 0;
  $handler->display->display_options['fields']['field_location_1']['element_label_colon'] = 0;
  $handler->display->display_options['fields']['field_location_1']['element_default_classes'] = 1;
  $handler->display->display_options['fields']['field_location_1']['hide_empty'] = 0;
  $handler->display->display_options['fields']['field_location_1']['empty_zero'] = 0;
  $handler->display->display_options['fields']['field_location_1']['click_sort_column'] = 'wkt';
  $handler->display->display_options['fields']['field_location_1']['type'] = 'geofield_lon';
  $handler->display->display_options['fields']['field_location_1']['settings'] = array(
    'data' => 'full',
    'format' => 'decimal_degrees',
  );
  $handler->display->display_options['fields']['field_location_1']['field_api_classes'] = 0;
  /* Sort criterion: Content: Post date */
  $handler->display->display_options['sorts']['created']['id'] = 'created';
  $handler->display->display_options['sorts']['created']['table'] = 'node';
  $handler->display->display_options['sorts']['created']['field'] = 'created';
  $handler->display->display_options['sorts']['created']['order'] = 'DESC';
  /* Filter criterion: Content: Published */
  $handler->display->display_options['filters']['status']['id'] = 'status';
  $handler->display->display_options['filters']['status']['table'] = 'node';
  $handler->display->display_options['filters']['status']['field'] = 'status';
  $handler->display->display_options['filters']['status']['value'] = 1;
  $handler->display->display_options['filters']['status']['group'] = 0;
  $handler->display->display_options['filters']['status']['expose']['operator'] = FALSE;
  /* Filter criterion: Content: Type */
  $handler->display->display_options['filters']['type']['id'] = 'type';
  $handler->display->display_options['filters']['type']['table'] = 'node';
  $handler->display->display_options['filters']['type']['field'] = 'type';
  $handler->display->display_options['filters']['type']['value'] = array(
    'project' => 'project',
  );

  /* Display: Page */
  $handler = $view->new_display('page', 'Page', 'page');
  $handler->display->display_options['path'] = 'maps/projects';

  /* Display: Block */
  $handler = $view->new_display('block', 'Block', 'block');
  $handler->display->display_options['defaults']['pager'] = FALSE;
  $handler->display->display_options['pager']['type'] = 'full';
  $handler->display->display_options['pager']['options']['items_per_page'] = '5';
  $handler->display->display_options['defaults']['style_plugin'] = FALSE;
  $handler->display->display_options['style_plugin'] = 'default';
  $handler->display->display_options['defaults']['style_options'] = FALSE;
  $handler->display->display_options['defaults']['row_plugin'] = FALSE;
  $handler->display->display_options['row_plugin'] = 'fields';
  $handler->display->display_options['defaults']['row_options'] = FALSE;

  /* Display: OpenLayers Data Overlay */
  $handler = $view->new_display('openlayers', 'OpenLayers Data Overlay', 'openlayers_1');
  $handler->display->display_options['pager']['type'] = 'none';
  $handler->display->display_options['pager']['options']['offset'] = '0';
  $handler->display->display_options['defaults']['style_plugin'] = FALSE;
  $handler->display->display_options['style_plugin'] = 'openlayers_data';
  $handler->display->display_options['style_options']['data_source'] = array(
    'value' => 'other_latlon',
    'other_lat' => 'field_location',
    'other_lon' => 'field_location_1',
    'wkt' => 'field_location',
    'other_top' => 'title',
    'other_right' => 'title',
    'other_bottom' => 'title',
    'other_left' => 'title',
    'name_field' => 'title',
    'description_field' => 'field_problem',
  );
  $handler->display->display_options['defaults']['style_options'] = FALSE;
  $handler->display->display_options['defaults']['row_plugin'] = FALSE;
  $handler->display->display_options['defaults']['row_options'] = FALSE;
  $translatables['project_map'] = array(
    t('Master'),
    t('Project Map'),
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
    t('Page'),
    t('Block'),
    t('OpenLayers Data Overlay'),
  );
  $export['project_map'] = $view;

  return $export;
}
