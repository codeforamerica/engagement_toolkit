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

  return $export;
}
