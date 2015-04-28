<?php

require_once "config.php";

if (RUNNING) {
	if (isset($_POST['username']) && isset($_POST['password'])) {
		$login = $_POST['username'];
		$pass = $_POST['password'];
	
		foreach (file(MAPFILE) as $line) {
			if (substr($line, 0, 1) != "#") {
				$raw = explode("=", trim($line));
			
				$fingerprint = $raw[0];
				$password = $raw[1];
			}
		}
	}
}