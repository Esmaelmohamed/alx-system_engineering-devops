# Modify the ULIMIT value in the Nginx default configuration file
exec { 'update-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin', '/sbin'],
  onlyif  => 'grep -q "15" /etc/default/nginx',
} ->

# Restart the Nginx service
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => ['/sbin', '/usr/sbin', '/bin', '/usr/bin'],
  require => Exec['update-nginx-ulimit'],
}

