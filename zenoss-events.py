#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import urllib2
import re
import subprocess
from bs4 import BeautifulSoup
from subprocess import call
import os
import mechanize
url = 'https://zenoss.xxxxxxx.com/zport/dmd/Events/evconsole'
mech = mechanize.Browser()
mech.set_handle_robots(False)
mech.open(url)
mech.select_form(nr=0)
mech["__ac_name"] = "username"
mech["__ac_password"] = "password"
results = mech.submit().read()
f = file('events-zenoss.txt', 'w')
f.write(results)
f.close()

os.system("sed -e 's/asof/eventClassKey/g' events-zenoss.txt > /Users/abhinoc/zenoss.txt")

html = urllib2.urlopen("file:///Users/abhinoc/zenoss.txt")
soup = BeautifulSoup(html)
data = soup.prettify()
info = re.findall(r'\"dedupid\"\:\s*\"\w+.*?\"eventClassKey\"+', data, re.IGNORECASE)
ackdevents = re.findall(r'ownerid\"\:\s\"\w+.*evid\"', data, re.IGNORECASE)
sep = "_" * 155
sep1 = "*" * 60

count = re.findall(r'totalCount\"\:\s*\w+', data, re.IGNORECASE)

chost = []


print "%s \n" %(count)

for summary in info:
	host = re.findall(r'dedupid\"\:\s*\"[\w.-]+', summary, re.IGNORECASE)
	host = [w.replace('dedupid', 'HostName') for w in host]
	ahost = [w.replace('HostName": "', '') for w in host]
	pstate = re.findall(r'prodState\"\:\s*\"\w+/\w+', summary, re.IGNORECASE)	
	pstate = [w.replace('prodState', 'Production State') for w in pstate]
        collector = re.findall(r'monitor\"\:\s*\"\w+\.\w+', summary, re.IGNORECASE)
        collector = [c.replace('monitor": "', 'Collector: ') for c in collector]
	component = re.findall(r'component\"\:\s\{.*?text\"\:\s*\"[\w.-]+', summary, re.IGNORECASE)
	component = re.findall(r'text\":\s\"[\w.-]+', summary, re.IGNORECASE)
	component = [w.replace('text', 'Component') for w in component]
	issue = re.findall(r'summary\"\:\s*\"\w+.*?\"eventState"', summary, re.IGNORECASE)
	location = re.findall(r'.location\"\:\s*\[\"\/[\w.-]+', summary, re.IGNORECASE)
	groups = re.findall(r'.groups\"\:\s*\[\"\/[\w.-]+', summary, re.IGNORECASE)
	systems = re.findall(r'.systems\"\:\s*\[\"\/[\w.-]+', summary, re.IGNORECASE)	
	ip = re.findall(r'ipAddress\"\:\s*\[\"\w+.\w+.\w+.\w+', summary, re.IGNORECASE)
	alertcount = re.findall(r'count\"\:\s*\w+', summary, re.IGNORECASE)
	ax = alertcount[0][8:]
	x = int(ax)
	firstseen = re.findall(r'stateChange\"\:\s*\"\d+\-\d+\-\d+\s*\d+\:\d+\:\d+', summary, re.IGNORECASE)
	firstseen = [w.replace('stateChange', 'First Seen:') for w in firstseen]
	lastseen = re.findall(r'lastTime\"\:\s*\"\d+\-\d+\-\d+\s*\d+\:\d+\:\d+', summary, re.IGNORECASE)
	lastseen = [w.replace('lastTime', 'lastseen') for w in lastseen]
	sev = re.findall(r'severity\"\:\s*\w', summary, re.IGNORECASE)
	
	if x < 5 :	
		chost.extend([ahost])
	elif x > 5 and x < 11:
		chost.extend([ahost])
		print "Alert not taken care for More than 30 min \n"
		print "Alert Count %s" %(x)
		print host
		print ip
		print issue
		print pstate
		print groups
		print collector
		print component
		print location
		print systems
		print alertcount
		print "%s %s" % (firstseen, lastseen)
		print "\n %s \n" % sep

	else:
                chost.extend([ahost])
		print "Alert not take care for More than an hour \n"
		print "Alert Count %s" %(x)
                print host
                print ip
                print issue
                print pstate
                print groups
                print collector
                print component
                print location
                print systems
                print alertcount
                print "%s %s" % (firstseen, lastseen)
                print "\n %s \n" % sep

print "Following Hosts are showing UP in zenoss \n"
for h in chost:
	print h
