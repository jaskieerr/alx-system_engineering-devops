# Defining SSH configuration as variable
$ssh_config_content = @(EOF)
PasswordAuthentication no
IdentityFile ~/.ssh/school
EOF

# Ensuring SSH client configuration file exists
file { '/root/.ssh/config':
  ensure  => present,
  content => $ssh_config_content,
}
