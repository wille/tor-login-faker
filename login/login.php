<?php

require_once "config.php";

if (RUNNING) {
	if (isset($_POST['username']) && isset($_POST['password'])) {
		$login = $_POST['username'];
		$pass = $_POST['password'];
	
		foreach (file(MAPFILE) as $line) {
	
		}
	}
}