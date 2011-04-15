<?php
	require "lib/api.class.php";

	$APIKEY = '9533c6694573d9328ad90f37009da995';
	
	$lm_api = new Api($APIKEY);
	
	$result = $lm_api->search('Training');
	echo "result = " . print_r($result, true) . "\n";
	
?>