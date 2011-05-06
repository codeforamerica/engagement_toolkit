<?php
/**
* Implements hook_skinr_skin_info().
*/
function acquia_marina_skinr_skin_info() {
  $skins['acquia_marina_text_color'] = array(
    'title' => t('Text color'),
    'type' => 'select',
    'attached' => array('css' => array('css/skins.css')),
    'default status' => TRUE,
    'group' => 'typography',
    'options' => array(
      'color_1' => array('title' => t('Red'), 'class' => array('red')),
      'color_2' => array('title' => t('Orange'), 'class' => array('orange')),
      'color_3' => array('title' => t('Yellow'), 'class' => array('yellow')),
      'color_4' => array('title' => t('Green'), 'class' => array('green')),
      'color_5' => array('title' => t('Blue'), 'class' => array('blue')),
      'color_6' => array('title' => t('Violet'), 'class' => array('violet')),
    ),
  );

$skins['acquia_marina_general_styles'] = array(
    'title' => t('General Styles'),
    'type' => 'select',
    'attached' => array('css' => array('css/skins.css')),
    'default status' => TRUE,
    'group' => 'general',
    'options' => array(
      'rounded_corner' => array('title' => t('Rounded_Corner'), 'class' => array('marina-rounded-corners')),

    ),
  );

$skins['acquia_marina_search_block'] = array(
    'title' => t('Search Block'),
    'type' => 'radios',
    'attached' => array('css' => array('css/skins.css')),
    'default status' => TRUE,
    'group' => 'general',
    'options' => array(
      'search_block' => array('title' => t('Gray_Search_Block'), 'class' => array('gray-search-box ')),

    ),
  );

$skins['acquia_marina_lists'] = array(
    'title' => t('Lists Styles'),
    'type' => 'radios',
    'attached' => array('css' => array('css/skins.css')),
    'default status' => TRUE,
    'group' => 'box',
    'options' => array(
      'lists_1' => array('title' => t('List_Style'), 'class' => array('marina-list-raquo')),
      'lists_2' => array('title' => t('List2_Style'), 'class' => array('marina-list-arrow-green')),  

    ),
  );  

$skins['acquia_marina_block_titles'] = array(
    'title' => t('Block Titles'),
    'type' => 'select',
    'attached' => array('css' => array('css/skins.css')),
    'default status' => TRUE,
    'group' => 'typography',
    'options' => array(
      'block_title_1' => array('title' => t('Blue_rounded_title_background_with_white_text'), 'class' => array('marina-title-rounded-blue')),
      'block_title_2' => array('title' => t('Green_rounded_title_background_with_white_text'), 'class' => array('marina-title-rounded-green')),
'block_title_3' => array('title' => t('Green_title'), 'class' => array('marina-title-green')),


    ),
  );

  $skins['acquia_marina_block_title_icon_styles'] = array(
    'title' => t('Block Icons'),
    'type' => 'select',
    'attached' => array('css' => array('css/skins.css')),
    'default status' => TRUE,
    'group' => 'box',
    'options' => array(
      'icon_1' => array('title' => t('Bubble'), 'class' => array('icon-bubble', 'title-icon')),
      'icon_2' => array('title' => t('Calendar'), 'class' => array('icon-calendar', 'title-icon')),
      'icon_3' => array('title' => t('Chalkboard'), 'class' => array('icon-chalkboard', 'title-icon')),
      'icon_4' => array('title' => t('Chat_bubbles'), 'class' => array('icon-chatbubbles', 'title-icon')),
      'icon_5' => array('title' => t('Color_chart'), 'class' => array('icon-colorchart', 'title-icon')),
      'icon_6' => array('title' => t('Flag'), 'class' => array('icon-flag', 'title-icon')),
      'icon_7' => array('title' => t('Gears'), 'class' => array('icon-gears', 'title-icon')),
      'icon_8' => array('title' => t('Home'), 'class' => array('icon-home', 'title-icon')),
      'icon_9' => array('title' => t('Keys'), 'class' => array('icon-keys', 'title-icon')),
      'icon_10' => array('title' => t('Newspaper'), 'class' => array('icon-newspaper', 'title-icon')),
      'icon_11' => array('title' => t('Notepad'), 'class' => array('icon-notepad', 'title-icon')),
      'icon_12' => array('title' => t('Photo'), 'class' => array('icon-photo', 'title-icon')),
      'icon_13' => array('title' => t('RSS'), 'class' => array('icon-rss', 'title-icon')),
      'icon_14' => array('title' => t('Search'), 'class' => array('icon-search', 'title-icon')),
      'icon_15' => array('title' => t('Star'), 'class' => array('icon-star', 'title-icon')),






    ),
  );





return $skins;
}