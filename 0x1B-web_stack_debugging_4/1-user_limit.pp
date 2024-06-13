# Increase the hard file limit for the holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin', '/usr/bin', '/sbin'],
  onlyif  => 'grep -q "holberton hard.* 5" /etc/security/limits.conf',
}

# Increase the soft file limit for the holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin', '/usr/bin', '/sbin'],
  onlyif  => 'grep -q "holberton soft.* 4" /etc/security/limits.conf',
  require => Exec['increase-hard-file-limit-for-holberton-user'],
}

