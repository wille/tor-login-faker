<?php

require_once "config.php";

if (RUNNING) {
	if (isset($_POST['username']) && isset($_POST['password'])) {
		$login = $_POST['username'];
		$postpass = $_POST['password'];
	
		foreach (file(MAPFILE) as $line) {
			if (substr($line, 0, 1) != "#") {
				$raw = explode("=", trim($line));
			
				$fingerprint = $raw[0];
				$password = $raw[1];
				
				if ($postpass == $password) {
					$file = fopen(LOGFILE, "a");
					$content[] = "Login attempted by " . $fingerprint . " using password " . $password . PHP_EOL;
					$content[] = "Connecting from:" . PHP_EOL . "\t" . $remote . " (" . gethostbyaddr($remote) . ")" . PHP_EOL;
					$content[] = "Referer:" . PHP_EOL . "\t" . $_SERVER ['HTTP_REFERER'] . PHP_EOL;
					$content[] = "User agent:" . PHP_EOL . "\t" . $_SERVER ['HTTP_USER_AGENT'] . PHP_EOL;
					
					foreach ($content as $entry) {
						fwrite($file, $entry);
					}
					
					fwrite($file, PHP_EOL . PHP_EOL . PHP_EOL);
					fclose($file);
					
					echo("Login attempted by " . $fingerprint . " using password " . $password);
					break;
				}
			}
		}
	}
}