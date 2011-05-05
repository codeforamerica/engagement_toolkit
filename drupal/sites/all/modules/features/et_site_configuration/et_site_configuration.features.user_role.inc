<?php
/**
 * @file
 * et_site_configuration.features.user_role.inc
 */

/**
 * Implementation of hook_user_default_roles().
 */
function et_site_configuration_user_default_roles() {
  $roles = array();

  // Exported role: content manager
  $roles['content manager'] = array(
    'name' => 'content manager',
    'weight' => '3',
  );

  // Exported role: developer
  $roles['developer'] = array(
    'name' => 'developer',
    'weight' => '2',
  );

  // Exported role: pre-authenticated
  $roles['pre-authenticated'] = array(
    'name' => 'pre-authenticated',
    'weight' => '5',
  );

  return $roles;
}
