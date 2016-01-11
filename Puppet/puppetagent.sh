#!/bin/bash
echo "Performing apt-get"
sudo apt-get update -y
echo "Adding puppet labs repo"
sleep 5;
sudo wget http://apt.puppetlabs.com/puppetlabs-release-trusty.deb
sudo dpkg -i puppetlabs-release-trusty.deb
echo "Performing apt-get update again"
sleep 5;
sudo apt-get update -y
echo "Install Puppet Agent"
sleep 5;
sudo apt-get -y install puppet

#After agent is installed, it must be informed about its master. For this purpose, edit /etc/puppet/puppet.conf and add the following line under [main] section,
#server = puppet.example.com
#By default puppet agent is not configured to start, So, At puppet agent, also edit /etc/default/puppet and set start = yes.

