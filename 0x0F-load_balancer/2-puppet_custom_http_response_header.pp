#!/usr/bin/env bash
# Adding Custom header with Puppet

# Updating and Installing nginx
exec {'update':
  provider  => shell,
  command   => 'sudo apt-get -y update',
  before    => Exec['install Nginx'],
}

# Installation process and adding of header
exec {'install Nginx':
  provider  => shell,
  command   => 'sudo apt-get -y install nginx',
  before    => Exec['add_header'],
}

# Configuraring The customasation of HTTP header
exec { 'add_header':
  provider     => shell,
  environment  => ["HOST=${hostname}"],
  command      => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before       => Exec['restart Nginx'],
}

# Restarting nginx server to apply changes
exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
