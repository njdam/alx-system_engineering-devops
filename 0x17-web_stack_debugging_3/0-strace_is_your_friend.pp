# Defining a Puppet exec resource to fix the identified issue
exec { 'fix-wordpress':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php; service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
