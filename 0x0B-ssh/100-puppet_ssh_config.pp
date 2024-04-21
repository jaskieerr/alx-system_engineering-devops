# test cmnt
$ssh_config_content = @(EOF)
PasswordAuthentication no
IdentityFile ~/.ssh/school
EOF

# Ensuring SSH client config file exists
file { '/root/.ssh/config':
  ensure  => present,
  content => $ssh_config_content,
}
