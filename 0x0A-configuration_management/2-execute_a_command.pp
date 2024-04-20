# Puppet script to kill a process named "killmenow"

# Define the exec resource to run the pkill command to kill the process named "killmenow"
exec { 'kill_killmenow_process':
  command  => 'pkill killmenow',  # Command to kill the process
  provider => 'shell',             # Use shell provider to execute the command
}
