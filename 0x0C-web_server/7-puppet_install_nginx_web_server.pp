# Puppet Manifest to Set Up Ubuntu Server with Nginx

# Execute a command to update the system's package list
exec { 'update system':
    command => '/usr/bin/apt-get update',
}

# Ensure that Nginx is installed on the server
package { 'nginx':
    ensure => 'installed',
    require => Exec['update system'],
}

# Create a basic HTML file with "Hello World!" content
file { '/var/www/html/index.html':
    content => 'Hello World!',
}

# Modify the Nginx configuration file to set up a redirection
exec { 'redirect_me':
    command => 'sed -i "24i\  rewrite ^/redirect_me https://www.youtube.com/@EsmaelLab permanent;" /etc/nginx/sites-available/default',
    provider => 'shell',
}

# Ensure that the Nginx service is running
service { 'nginx':
    ensure => running,
    require => Package['nginx'],
}

