# install install flask version 2.1.0 from pip3 using puppet
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin'],
  environment => 'PATH=/usr/bin:$PATH',
  creates     => '/usr/local/lib/python3.8/dist-packages/flask/__init__.py',
}
