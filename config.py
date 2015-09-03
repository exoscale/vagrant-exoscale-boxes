#!/usr/bin/python

import os


# exoscale make Vagrant Boxes
# configuration file options


# Account access for Open Cloud to display usefull information
try:
    apikey = os.environ["APIKEY"]
except:
    print("Error missing APIKEY env variable, exiting")
    exit(1)
try:
    secretkey = os.environ["SECRETKEY"]
except:
    print("Error missing SECRETKEY env variable, exiting")
    exit(1)


path='/compute'
host='api.exoscale.ch'
port='443'
protocol='https'


# Parameters that will be put in the boxes
network='00304a04-c7ea-4e77-a786-18bc64347bf7' #default Internet network
zone='1128bd56-b4d9-4ac6-a7b9-c715b187ce11' #CH-GV2
