exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  path    => '/bin/',
}

