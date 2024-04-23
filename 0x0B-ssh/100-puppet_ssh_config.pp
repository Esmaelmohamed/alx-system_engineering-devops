# 100-puppet_ssh_config.pp

# Ensure the SSH client configuration file exists
file { '/home/your_username/.ssh/config':
  ensure => present,
  owner  => 'your_username',
  group  => 'your_username',
  mode   => '0600',
}

# Ensure the SSH client is configured to use the private key
file_line { 'Declare identity file':
  path  => '/home/your_username/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
}

# Ensure the SSH client is configured to refuse password authentication
file_line { 'Turn off passwd auth':
  path  => '/home/your_username/.ssh/config',
  line  => 'PasswordAuthentication no',
}

