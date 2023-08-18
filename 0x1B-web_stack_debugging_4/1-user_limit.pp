# Script to change the OS configuration so that it is possible to
# login with the holberton user and open a file without any error message
exec { 'Change_OS_config':
  command  => 'sudo sed -i "s/4/40000/" /etc/security/limits.conf; sudo sed -i "s/5/50000/" /etc/security/limits.conf',
  provider => shell,
  returns  => [0, 1]
}
