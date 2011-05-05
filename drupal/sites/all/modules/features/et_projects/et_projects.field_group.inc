<?php
/**
 * @file
 * et_projects.field_group.inc
 */

/**
 * Implementation of hook_field_group_info().
 */
function et_projects_field_group_info() {
  $export = array();

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_backstory|node|project|form';
  $field_group->group_name = 'group_backstory';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'form';
  $field_group->parent_name = 'group_plan';
  $field_group->data = array(
    'label' => 'Backstory',
    'weight' => '18',
    'children' => array(
      0 => 'field_problem',
      1 => 'field_result',
    ),
    'format_type' => 'tab',
    'format_settings' => array(
      'formatter' => 'closed',
      'instance_settings' => array(
        'classes' => '',
        'required_fields' => 1,
      ),
    ),
  );
  $export['group_backstory|node|project|form'] = $field_group;

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_general|node|project|form';
  $field_group->group_name = 'group_general';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'form';
  $field_group->parent_name = 'group_plan';
  $field_group->data = array(
    'label' => 'General',
    'weight' => '10',
    'children' => array(
      0 => 'body',
      1 => 'field_categories',
      2 => 'field_link',
      3 => 'field_image',
      4 => 'title',
    ),
    'format_type' => 'tab',
    'format_settings' => array(
      'formatter' => 'closed',
      'instance_settings' => array(
        'classes' => '',
        'required_fields' => 1,
      ),
    ),
  );
  $export['group_general|node|project|form'] = $field_group;

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_location|node|project|form';
  $field_group->group_name = 'group_location';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'form';
  $field_group->parent_name = 'group_plan';
  $field_group->data = array(
    'label' => 'Location',
    'weight' => '19',
    'children' => array(
      0 => 'field_city',
      1 => 'field_state',
      2 => 'field_county',
      3 => 'field_area_code',
      4 => 'field_location',
      5 => 'field_location_text',
      6 => 'field_neighborhood',
    ),
    'format_type' => 'tab',
    'format_settings' => array(
      'formatter' => 'closed',
      'instance_settings' => array(
        'classes' => '',
        'required_fields' => 1,
      ),
    ),
  );
  $export['group_location|node|project|form'] = $field_group;

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_plan|node|project|form';
  $field_group->group_name = 'group_plan';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'form';
  $field_group->parent_name = '';
  $field_group->data = array(
    'label' => 'What are you doing?',
    'weight' => '1',
    'children' => array(
      0 => 'group_location',
      1 => 'group_general',
      2 => 'group_backstory',
      3 => 'group_process',
    ),
    'format_type' => 'tabs',
    'format_settings' => array(
      'formatter' => NULL,
      'instance_settings' => array(
        'classes' => '',
      ),
    ),
  );
  $export['group_plan|node|project|form'] = $field_group;

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_process|node|project|form';
  $field_group->group_name = 'group_process';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'form';
  $field_group->parent_name = 'group_plan';
  $field_group->data = array(
    'label' => 'How are you doing it?',
    'weight' => '17',
    'children' => array(
      0 => 'field_process',
      1 => 'field_recipes',
      2 => 'field_ingredients',
    ),
    'format_type' => 'tab',
    'format_settings' => array(
      'formatter' => 'closed',
      'instance_settings' => array(
        'classes' => '',
        'required_fields' => 1,
      ),
    ),
  );
  $export['group_process|node|project|form'] = $field_group;

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_recipe|node|project|default';
  $field_group->group_name = 'group_recipe';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'default';
  $field_group->parent_name = '';
  $field_group->data = array(
    'label' => 'Recipe',
    'weight' => '5',
    'children' => array(
      0 => 'field_recipes',
    ),
    'format_type' => 'div',
    'format_settings' => array(
      'formatter' => 'collapsible',
      'instance_settings' => array(
        'effect' => 'none',
        'speed' => 'fast',
        'classes' => '',
      ),
    ),
  );
  $export['group_recipe|node|project|default'] = $field_group;

  $field_group = new stdClass;
  $field_group->api_version = 1;
  $field_group->identifier = 'group_stats|node|project|default';
  $field_group->group_name = 'group_stats';
  $field_group->entity_type = 'node';
  $field_group->bundle = 'project';
  $field_group->mode = 'default';
  $field_group->parent_name = '';
  $field_group->data = array(
    'label' => 'Details',
    'weight' => '6',
    'children' => array(
      0 => 'field_categories',
      1 => 'field_city',
      2 => 'field_state',
      3 => 'field_location_text',
      4 => 'field_neighborhood',
    ),
    'format_type' => 'div',
    'format_settings' => array(
      'label' => 'Details',
      'instance_settings' => array(
        'classes' => '',
        'description' => '',
        'effect' => 'none',
        'speed' => 'fast',
      ),
      'formatter' => 'open',
    ),
  );
  $export['group_stats|node|project|default'] = $field_group;

  return $export;
}
