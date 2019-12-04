def main():
    switch = open('switch_txt', 'r')

    switch_content = switch.read()
    switch.close()
    switch_content = switch_content.splitlines()
    print(switch_content)

    for n in switch_content:
        print ('###########################')
        value = n.split (',')
        print ('Switch name: ', value[0])
        print ('Location: ', value[1])
        print ('Rack number', value[2])
        print ('vendor', value[3])
        print ('S/N', value[4])
        print ('IP address', value[5])
        print ('Model', value[6])
main()





