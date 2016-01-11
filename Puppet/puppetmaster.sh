#!/bin/bash
echo "Performing apt-get update..."
sleep 5;
sudo apt-get update -y
echo "Adding puppet labs repo"
sleep 5;
sudo wget http://apt.puppetlabs.com/puppetlabs-release-trusty.deb
sudo dpkg -i puppetlabs-release-trusty.deb
echo "Performing apt-get update again"
sudo apt-get update -y
echo "Install Puppet Master"
sudo apt-get -y install puppetmaster

#After installing master, we need to make some configuration changes in /etc/puppet/puppet.conf file. The file is in INI format. We will add following line in [master] block of configuration file,
#certname = puppet.example.com

#Create an small manifest file

root@puppet:/home/ubuntu# cat /etc/puppet/manifests/site.pp
file{'/tmp/puppetfile':
ensure => present,
content => "This is first file created by puppet\n"
}

