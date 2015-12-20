# add jenkins PGP KEY
wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins

#
#2015-10-07 06:28:35 ☆  jenkins100 in ~/JENKINS
#○ → /etc/init.d/jenkins start
#* Starting Jenkins Continuous Integration Server jenkins

# Jenkins failed to start

#○ → /etc/init.d/jenkins status
#Jenkins Continuous Integration Server is not running

#○ → cat jenkins/jenkins.log
#Jenkins requires Java7 or later, but you are running 1.6.0_36-b36 from /usr/lib/jvm/java-6-openjdk-i386/jre
#java.lang.UnsupportedClassVersionError: 50.0
#at Main.main(Main.java:90)

# We require java7 or later

#○ → java -version
#java version "1.6.0_36"
#OpenJDK Runtime Environment (IcedTea6 1.13.8) (6b36-1.13.8-0ubuntu1~12.04)
#OpenJDK Client VM (build 23.25-b01, mixed mode, sharing)

# Installing Java 8 on Ubuntu

#First you need to add webupd8team Java PPA repository in your system and install Oracle Java 8 using following set of commands.

$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer


