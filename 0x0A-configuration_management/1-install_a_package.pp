# using Puppet to install flask from pip3

pacakage { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
