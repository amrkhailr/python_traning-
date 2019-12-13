def main():
    switch = open('switch_txt', 'r')

    switch_content = switch.read()
    switch.close()
    switch_content = switch_content.splitlines()
    print(switch_content)

    network={}
    for n in switch_content:
        switch={}
        value = n.split (',')
        switch['Switchname']= value[0]
        switch['Location']=value[1]
        switch['Racknumber']= value[2]
        switch['vendor']= value[3]
        switch['SN']= value[4]
        switch['IPaddress']=value[5]
        switch['Model']=value[6]
        network.append(switch)
    print(network)
main()