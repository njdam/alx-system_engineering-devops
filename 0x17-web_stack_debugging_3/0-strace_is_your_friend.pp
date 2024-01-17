# Defining a Puppet exec resources to run strace on the Apache process
exec { 'strace_apache':
  command	=> 'strace -p $(pgrep apache2) -o /tmp/strace_output.txt',
  path		=> '/bin:/usr/bin',
  user		=> 'root',
  require	=> Package['strace'],
}

# Defining a Puppet exec resource to fix the identified issue
exec { 'fix-wordpress':
  command 	=> 'sudo service apache2 restart',
  path		=> '/bin:/usr/bin',
  refreshonly	=> true,
  subscribe	=> Exec['strace_apache'],
}

# To ensure that the 'strace' package is installed
package { 'strace':
  ensure 	=> present,
}

# Notify a service restart after fixing the issue
service { 'apache2':
  ensure 	=> running,
  require	=> Exec['fix-wordpress'],
  notify	=> Service['apache2'],
}
