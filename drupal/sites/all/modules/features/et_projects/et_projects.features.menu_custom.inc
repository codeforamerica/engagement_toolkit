<?php
/**
 * @file
 * et_projects.features.menu_custom.inc
 */

/**
 * Implementation of hook_menu_default_menu_custom().
 */
function et_projects_menu_default_menu_custom() {
  $menus = array();

  // Exported menu: menu-manage-projects
  $menus['menu-manage-projects'] = array(
    'menu_name' => 'menu-manage-projects',
    'title' => 'Manage Projects',
    'description' => 'This menu contains the options for creating, deleting, and editing a project.',
  );
  // Translatables
  // Included for use with string extractors like potx.
  t('Manage Projects');
  t('This menu contains the options for creating, deleting, and editing a project.');


  return $menus;
}
