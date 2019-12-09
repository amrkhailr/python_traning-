apogee={"Empolyee":200, 'address':"Kramer in", 'phone':"512-44-404"}
print(apogee)

network={"switch":"sw1","router":"rt1","vpnrtr":"vpn1"}
person={"firstname":"b","name":"aaaa","age":100}
site={"bldg":{"idf":100,"cs":"cs1"},"ap":200}
site["addr"]="Krmaer Ln" # just added 
#num=float(input("Give a number :"))

print(site)
if "router" not in site:
    site['router']="9500"
print(site)

del site['ap'] # Delete the ap from site dictionary 
print(site)