#!/usr/bin/puppet
# Puppet script to install a specific version of Flask (2.1.0) using pip3

# Define the package resource to ensure Flask version 2.1.0 is installed using pip3 provider
package { 'flask':
  ensure   => '2.1.0',    # Ensure version 2.1.0 is installed
  provider => 'pip3',     # Use pip3 as the package provider
}
