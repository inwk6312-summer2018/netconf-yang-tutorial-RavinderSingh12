from ncclient import manager
import sys
import xml.dom.minidom


HOST='10.0.131.205'

PORT=830
	
USER='cisco'
PASS='cisco'

FILE='get_interface_gigabit3.xml



def get_configured_interfacs(xml_filter):
 

 with manager.connect(host=HOST,port=PORT,username=USER,
 
      password=PASS,hostkey_verify=False,
      device_params={'name':'default'},
      allow_agent=Fals,look_for_keys=fals)as m:
   with open(xml_filter) as f:
    return(m.get_config('running',f.read()))


def main():



 interfaces=get_configured_interfaces(FILE)
 interfaces=xml.minidom.parseString(interface.xml)
 interface=interfaces.getElementsBytagname("interfaces")
 print(interfces[0].toprettyxml())
 


if__name__=='__main__':
  sys.exit(main()) 
