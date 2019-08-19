from cvplibrary import CVPGlobalVariables, GlobalVariableNames
from cvplibrary import Device

device_ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
dev_user = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_USERNAME)
dev_pass = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_PASSWORD)

cmdList = ['show hostname']
device = Device(device_ip,dev_user,dev_pass)

dict_resp = device.runCmds(cmdList)
device_hostname = dict_resp[0]['response']['hostname']
mlag_ip = "192.0.0.1/24"
mlag_ip_peer = "192.0.0.2"
domain_id = "1000"
peer_name = device_hostname[:-1] + "B"

if device_hostname.endswith('B'):
  mlag_ip = "192.0.0.2/24"
  mlag_ip_peer = "192.0.0.1"
  peer_name = device_hostname[:-1] + "A"

print "vlan 4094"
print "name MLAGPEER"
print "trunk group MLAGPEER"
print "!"
print "no spanning-tree vlan 4094"
print "!"
print "interface Vlan4094"
print "description MLAG PEER SYNC"
print "no autostate"
print "ip address " + mlag_ip
print "!"
print "interface Port-Channel1000"
print "description MLAG PEER-LINK"
print "switchport mode trunk"
print "switchport trunk group MLAGPEER"
print "!"
print "mlag configuration"
print "domain-id " + domain_id
print "local-interface Vlan4094"
print "peer-address " + mlag_ip_peer
print "peer-link port-channel 1000"
print "!"
print "Interface Ethernet5"
print "description MLAG Link to " + peer_name
print "channel-group 1000 mode active"
print "no shutdown"
print "!"
print "Interface Ethernet6"
print "description MLAG Link to " + peer_name
print "channel-group 1000 mode active"
print "no shutdown"
