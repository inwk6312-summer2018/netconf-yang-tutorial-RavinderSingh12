from ncclient import manager
import sys
import xml.dom.minidom




HOST='10.0.131.205'


PORT=830

USER='cisco'
PASS='cisco'

def main():

 with manager.connect(host=HOST,port=PORT,username=USER,
             password=PASS,hockey_verify=False,
             device_params={'name':'default'},
             allow_agent=False,look_for_keys=False)as m:



  hostname_filter=""
	  <filter>
          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname></hostname>
          </native>
          <filter>
           """

