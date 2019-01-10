# Creates a file
file { "/tmp/holberton":
	replace => true,
	mode => "0744",
	owner => "www-data",
	group => "www-data",
	content => "I love Puppet",
}
