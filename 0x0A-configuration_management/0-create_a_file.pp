# Create a file in /tmp with specific permissions, owner, and group
file { '/tmp/school':
  ensure  => file,                # Ensure that it's a file
  content => 'I love Puppet',    # Specify the content of the file
  mode    => '0744',             # Set file permissions to 0744
  owner   => 'www-data',         # Set owner to www-data
  group   => 'www-data',         # Set group to www-data
}
