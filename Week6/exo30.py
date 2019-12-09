# Dictionaries::

apogee={"Empolyee":200, 'address':"Kramer in", 'phone':"512-44-404"}
print(apogee)

network={"switch":"sw1","router":"rt1","vpnrtr":"vpn1"}
person={"firstname":"b","name":"aaaa","age":100}
site={"bldg":{"idf":5,"cs":"cs1"},"ap":200}
print(network["switch"]) # Display me the value of switch
print(site["bldg"])
print(site["bldg"]['idf']) # how to shoe disctionary nested inside another 

if "router" in site:
    print(site["router"])
else:
    print("not exist")