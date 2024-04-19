# homocide

exec {'pkill killmenow':
  onlyif   => 'test `pgrep killmenow`',
  provider => 'shell',
  }
