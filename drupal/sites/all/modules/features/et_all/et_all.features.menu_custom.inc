<?php
/**
 * @file
 * et_all.features.menu_custom.inc
 */

/**
 * Implementation of hook_menu_default_menu_custom().
 */
function et_all_menu_default_menu_custom() {
  $menus = array();

  // Exported menu: menu-et-menu
  $menus['menu-et-menu'] = array(
    'menu_name' => 'menu-et-menu',
    'title' => 'ET Menu',
    'description' => 'This is the main menu for the ET.',
  );
  // Translatables
  // Included for use with string extractors like potx.
  t('ET Menu');
  t('This is the main menu for the ET.');


  return $menus;
}
