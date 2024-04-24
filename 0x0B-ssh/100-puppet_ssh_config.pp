#!/usr/bin/env puppet

# Puppet script to configure SSH for passwordless authentication.

# Including the standard library module for Puppet
include stdlib

# Ensure the SSH private key file is specified for authentication.
file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]*[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# Regular Expression Explanation:
# - ^: Matches the beginning of the line
# - [#]*: Matches zero or more hash characters
# - [\s]*: Matches zero or more whitespace characters
# - (?i)IdentityFile: Performs a case-insensitive match for "IdentityFile"
# - [\s]+: Matches one or more whitespace characters
# - ~/.ssh/id_rsa: Specifies the path to the SSH private key file to be replaced
# - $: Matches the end of the line

# Ensure password authentication is disabled.
file_line { 'Deny Password Authentication':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]*[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

# Regular Expression Explanation:
# - ^: Matches the beginning of the line
# - [#]*: Matches zero or more hash characters
# - [\s]*: Matches zero or more whitespace characters
# - (?i)PasswordAuthentication: Performs a case-insensitive match for "PasswordAuthentication"
# - [\s]+: Matches one or more whitespace characters
# - (yes|no): Matches either "yes" or "no" for password authentication
# - $: Matches the end of the line

