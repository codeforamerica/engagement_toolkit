<?php
/**
 * @file
 * et_project_map.openlayers_styles.inc
 */

/**
 * Implementation of hook_openlayers_styles().
 */
function et_project_map_openlayers_styles() {
  $export = array();

  $openlayers_styles = new stdClass;
  $openlayers_styles->disabled = FALSE; /* Edit this to true to make a default openlayers_styles disabled initially */
  $openlayers_styles->api_version = 1;
  $openlayers_styles->name = 'ET_Project';
  $openlayers_styles->title = 'ET_Project';
  $openlayers_styles->description = '';
  $openlayers_styles->data = array(
    'pointRadius' => 6,
    'fillColor' => '#000000',
    'strokeColor' => '#ffffff',
    'strokeWidth' => 1,
    'fillOpacity' => 1,
    'strokeOpacity' => 1,
    'strokeLinecap' => 'round',
    'strokeDashstyle' => 'solid',
    'graphicOpacity' => 1,
    'labelAlign' => 'cm',
  );
  $export['ET_Project'] = $openlayers_styles;

  return $export;
}
