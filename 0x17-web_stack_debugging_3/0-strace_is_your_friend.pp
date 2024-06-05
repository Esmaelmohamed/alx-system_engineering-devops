# 0-strace_is_your_friend.pp
file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure  => file,
  content => 'class WP_Locale {}', # Placeholder content, adjust as necessary
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/var/www/html/wp-includes/class-wp-locale.php'],
