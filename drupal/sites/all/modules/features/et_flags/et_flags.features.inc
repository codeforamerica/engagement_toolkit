<?php
/**
 * @file
 * et_flags.features.inc
 */

/**
 * Implementation of hook_flag_default_flags().
 */
function et_flags_flag_default_flags() {
  $flags = array();
  // Exported flag: "Join".
  $flags['join'] = array(
    'content_type' => 'node',
    'title' => 'Join',
    'global' => '0',
    'types' => array(
      0 => 'project',
    ),
    'flag_short' => 'Join',
    'flag_long' => 'Join this project',
    'flag_message' => 'You joined this project.',
    'unflag_short' => 'Leave Project',
    'unflag_long' => 'Leave the project.',
    'unflag_message' => 'You left the project.',
    'unflag_denied_text' => '',
    'link_type' => 'confirm',
    'roles' => array(
      'flag' => array(
        0 => '2',
      ),
      'unflag' => array(
        0 => '2',
      ),
    ),
    'show_on_page' => 1,
    'show_on_teaser' => 1,
    'show_on_form' => 0,
    'access_author' => '',
    'i18n' => 0,
    'flag_confirmation' => 'Are you sure you want to join this project?',
    'unflag_confirmation' => 'Are you sure you want to leave this project?',
    'api_version' => 2,
    'module' => 'et_flags',
    'locked' => array(
      0 => 'name',
    ),
  );
  // Exported flag: "Like".
  $flags['like'] = array(
    'content_type' => 'node',
    'title' => 'Like',
    'global' => '0',
    'types' => array(
      0 => 'project',
    ),
    'flag_short' => 'Like',
    'flag_long' => 'You like this project.',
    'flag_message' => 'You like this project.',
    'unflag_short' => 'Unlike',
    'unflag_long' => 'You unliked this project.',
    'unflag_message' => 'You unliked this project.',
    'unflag_denied_text' => '',
    'link_type' => 'toggle',
    'roles' => array(
      'flag' => array(
        0 => '2',
      ),
      'unflag' => array(
        0 => '2',
      ),
    ),
    'show_on_page' => 1,
    'show_on_teaser' => 1,
    'show_on_form' => 0,
    'access_author' => '',
    'i18n' => 0,
    'api_version' => 2,
    'module' => 'et_flags',
    'locked' => array(
      0 => 'name',
    ),
  );
  return $flags;
}
