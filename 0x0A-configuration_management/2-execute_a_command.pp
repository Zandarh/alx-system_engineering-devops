# manifest that kills a process named killnow

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}

