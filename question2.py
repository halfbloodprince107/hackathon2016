import json
reader = open("sample.json")
data = reader.read()
dict_data = eval(json.loads(json.dumps(data)))

# Change firewall - protocol - from tcp to udp
dict_data["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["application"]["service"][0]["protocol"] = "udp"




# Change 3rd vnics- portgroup name to EXT_VLAN_201b
dict_data["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_201b"


# Change ospf- enabled = false to true
dict_data["featureConfigs"]["features"][5]["bgp"]["redistribution"]["rules"]["rules"][0]["from"]["ospf"] = True


#  Update holddowntimer = holddowntimer +keepalivetimer
print dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"]

for i in range(len(dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"])) :
    dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["holdDownTimer"] += dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i]["keepAliveTimer"]

print dict_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"]

reader.close()

writer = open("sample.json",'w')
writer.write(str(dict_data))