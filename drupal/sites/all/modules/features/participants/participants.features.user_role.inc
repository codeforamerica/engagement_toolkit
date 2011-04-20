<?php
/**
 * @file
 * participants.features.user_role.inc
 */

/**
 * Implementation of hook_user_default_roles().
 */
function participants_user_default_roles() {
  $roles = array();

  // Exported role: leader
  $roles['leader'] = array(
    'name' => 'leader',
    'weight' => '6',
  );

  // Exported role: participant
  $roles['participant'] = array(
    'name' => 'participant',
    'weight' => '4',
  );

  // Exported role: skill participant
  $roles['skill participant'] = array(
    'name' => 'skill participant',
    'weight' => '7',
  );

  return $roles;
}
