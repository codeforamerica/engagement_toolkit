<?php
/**
 * @file
 * et_projects.features.menu_links.inc
 */

/**
 * Implementation of hook_menu_default_menu_links().
 */
function et_projects_menu_default_menu_links() {
  $menu_links = array();

  // Exported menu link: menu-manage-projects:node/add/project
  $menu_links['menu-manage-projects:node/add/project'] = array(
    'menu_name' => 'menu-manage-projects',
    'link_path' => 'node/add/project',
    'router_path' => 'node/add/project',
    'link_title' => 'Create a new project',
    'options' => array(
      'attributes' => array(
        'title' => '',
      ),
    ),
    'module' => 'menu',
    'hidden' => '0',
    'external' => '0',
    'has_children' => '0',
    'expanded' => '0',
    'weight' => '0',
  );
  // Translatables
  // Included for use with string extractors like potx.
  t('Create a new project');


  return $menu_links;
}
