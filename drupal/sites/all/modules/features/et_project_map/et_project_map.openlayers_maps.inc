<?php
/**
 * @file
 * et_project_map.openlayers_maps.inc
 */

/**
 * Implementation of hook_openlayers_maps().
 */
function et_project_map_openlayers_maps() {
  $export = array();

  $openlayers_maps = new stdClass;
  $openlayers_maps->disabled = FALSE; /* Edit this to true to make a default openlayers_maps disabled initially */
  $openlayers_maps->api_version = 1;
  $openlayers_maps->name = 'et_project_map';
  $openlayers_maps->title = 'Project Map';
  $openlayers_maps->description = 'This is a map of projects.';
  $openlayers_maps->data = array(
    'width' => 'auto',
    'height' => '400px',
    'image_path' => 'sites/all/themes/et/openlayers/img/',
    'css_path' => '',
    'proxy_host' => '',
    'hide_empty_map' => 0,
    'center' => array(
      'initial' => array(
        'centerpoint' => '0,0',
        'zoom' => '2',
      ),
      'restrict' => array(
        'restrictextent' => 0,
        'restrictedExtent' => '',
      ),
    ),
    'behaviors' => array(
      'openlayers_behavior_attribution' => array(),
      'openlayers_behavior_keyboarddefaults' => array(),
      'openlayers_behavior_layerswitcher' => array(
        'ascending' => 1,
      ),
      'openlayers_behavior_navigation' => array(
        'zoomWheelEnabled' => 1,
      ),
      'openlayers_behavior_panzoombar' => array(),
    ),
    'default_layer' => 'osm_mapnik',
    'layers' => array(
      'osm_mapnik' => 'osm_mapnik',
      'project_map_openlayers_1' => 'project_map_openlayers_1',
      'geofield_formatter' => 0,
    ),
    'layer_styles' => array(
      'project_map_openlayers_1' => 'ET_Project',
      'geofield_formatter' => '0',
    ),
    'layer_activated' => array(
      'project_map_openlayers_1' => 'project_map_openlayers_1',
      'geofield_formatter' => 0,
    ),
    'layer_switcher' => array(
      'geofield_formatter' => 0,
      'project_map_openlayers_1' => 0,
    ),
    'projection' => '900913',
    'displayProjection' => '4326',
    'styles' => array(
      'default' => 'default',
      'select' => 'default',
      'temporary' => 'default',
    ),
  );
  $export['et_project_map'] = $openlayers_maps;

  return $export;
}
