# Scripts for fixing nginx failed to handle concurrent requests

exec { 'fix--for-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*:/ULIMIT=\\\"\'-n 8192\\\"/' \
/etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
