#!/usr/bin/env bash
# A bash script to use puppet to make changes to our configuration file.

# To make sure if client configuration file is present
file { '/etc/ssh/ssh_config':
  ensure => present,  # To Ensure if file is present
}

# To turn off password authentication
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',  # Path to SSH client configuration file
  line  => 'PasswordAuthentication no',  # Disable passwod authentication
  match => '^#?PasswordAuthentication',  # re if this line exists to replace
}

# To declare identity file containing private key
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',  # Path to SSH client configuration file
  line  => 'IdentityFile ~/.ssh/school',  # Specifying private key file
  match => '^#?IdentityFile',  # re if this line exists must be replaced
}
