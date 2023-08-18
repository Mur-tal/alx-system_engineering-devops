# a script to increase the amount of traffic an Nginx server can handle
exec { 'Increase_limit':
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
  returns  => [0, 1]
}
