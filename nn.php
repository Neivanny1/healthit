<?php

// Token
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1IiwianRpIjoiZTY5N2EzZmM3NTdjNjQ0MTdiNTU1ZmUyNzIxZTA4OTFmMjZkMDQwMWE4ZDlhM2M3YzhkYTA3OGQ1NDM3YzM5YTQzOTEyYTVjZWMwMzM4NzYiLCJpYXQiOjE3MTE2OTI5NDcuNTk4NTIxLCJuYmYiOjE3MTE2OTI5NDcuNTk4NTIyLCJleHAiOjE3MTE3MDAxNDcuNTk0MjQzLCJzdWIiOiIyMTA3NjkiLCJzY29wZXMiOltdfQ.Ml31RCoVC4urOltwj2lqy5ZBo_S1VW8yV28A8qB65KSRsdJ62DDBMJlrPfP87NfuZ-IAM7M3Wqand8AeAZgAbUN7xr3nCVHR-yCCVPBIog632zaDO-LHBlDigtc0L_tXUORBGThdHen1Is2K_q45NJg1zDSGHtyGI7G__z_jUYa7_jK2OxM7CudYDcggmkFovBk9W1teMYrzuNaFvf34N7veStcXz_F9xJVjNbY-O_W9KEUUX8WWYVn88D5dYC4G0pohzoeSuH8VHfAlMaBQz6dXqbL5Ujdbhl7KF_sNzsLeO8s18yEdjkb4N5u4VBw5WTVLeLMv4SPuCn92f273CyHJPZ9Et7uVE4Dhtlwrtw-Te0HgPbeC4VbWOYhcPmH78YHFqx49d93gZIDFZokKT5ISgJGGGjjDn0exoHOlxp2n69MjgGShDVq8jhDCaIGlk3YDDanrgr9zc9DHqzE5qf69KjLWqD7sr9MrF6-bsyQJ1xRDWuun1kF0FnnxiSFE1lTFvwiied_lVkvY4GXitIs6Qhlcxby_puBU0fCpu-oslEaIMxeggpufAUA4a8Wa_8BvwWP473nCMpqSSeK4ZSf59b2dBaBDmYGIzV6-6ry5liK3Tr9potZSWPnWKSRrJHxtioxUccYOtf5h_6M129CynsUyWvry_EOX2s6yK-E';

// URL
$url = 'https://training.digimal.uonbi.ac.ke/api/administrative_unit';

// Initialize cURL session
$ch = curl_init();

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Authorization: Bearer ' . $token,
    'Content-Type: application/json'
));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute cURL session
$response = curl_exec($ch);

// Check for cURL errors
if ($response === false) {
    echo "Error: " . curl_error($ch);
    curl_close($ch);
    exit;
}

// Close cURL session
curl_close($ch);

// Decode JSON response
$data = json_decode($response, true);

// Check if JSON decoding was successful
if ($data === null) {
    echo "Error: Unable to decode JSON response";
    exit;
}

// Save JSON response to file
$jsonFile = 'response.json';
file_put_contents($jsonFile, $response);

echo "Response saved to '$jsonFile'";
?>




CREATE DATABASE IF NOT EXISTS `cordinates`;
CREATE USER IF NOT EXISTS 'healthit'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
GRANT ALL PRIVILEGES ON `cordinates`.* TO 'healthit'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'healthit'@'localhost';
FLUSH PRIVILEGES;