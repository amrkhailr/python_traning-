site={"bldg":{"idf":100,"cs":"cs1"},"ap":200}

site["addr"]="Krmaer Ln" # just added 
if "router" not in site:
    site['router']="9500"
for key in site:
    print(site[key])   # will print both dictionay name and key names inside the disc