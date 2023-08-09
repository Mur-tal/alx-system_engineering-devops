# find out why Apache is returning a 500 error using trace
# and fix it using Puppet

exec { 'fix-bug':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin/:/usr/local/bin/'
}
