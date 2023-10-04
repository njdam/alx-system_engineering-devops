# Configuring Nginx server with puppet instead of Bash to save time
#
# Updating the package for ubuntu machines
exec { 'Update the apt repository':
  command => 'apt update',
  path    => '/usr/bin:/usr/sbin:/bin'
}

# Setting up Package to be installed in ubuntu machines if not
package { 'The web server':
  ensure          => installed,
  name            => 'nginx',
  provider        => 'apt',
  install_options => ['-y']
}

# To write "Hello World!\n" in /var/www/html/index.html of ubuntu server
file { 'The home page':
  ensure  => file,
  path    => '/var/www/html/index.html',
  mode    => '0744',
  owner   => 'www-data',
  content => "Hello World!\n"
}

# Setting up the Error code to return "Ceci n'est pas une page\n"
file { 'The 404 page':
  ensure  => file,
  path    => '/var/www/error/404.html',
  mode    => '0744',
  owner   => 'www-data',
  content => "Ceci n'est pas une page\n"
}

# Setting up the nginx web server to redirect http request to another site
file { 'Nginx server config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  mode    => '0744',
  owner   => 'www-data',
  content =>
  "server {
  	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
]		try_files \$uri \$uri/ =404;
	}

	if (\$request_filename ~ redirect_me){
		rewrite ^https://github.com/njdam/ permanent;
	}

	error_page 404 /404.html;
	location = /404.html {
		root /var/www/error/;
		internal;
	}
  }"
}

# Restarting the nginx web server
exec { 'Start the server':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin'
}
