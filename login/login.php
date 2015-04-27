<?php

require_once "config.php";

if (isset($_POST['username']) && isset($_POST['password'])) {
	$login = $_POST['username'];
	$pass = $_POST['password'];
}